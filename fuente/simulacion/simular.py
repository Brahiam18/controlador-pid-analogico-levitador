"""Corre las simulaciones de la fuente en ngspice y genera gráficas y métricas.
Uso: python3 simular.py   (requiere ngspice en el PATH)
"""
import subprocess, numpy as np, json, os, sys
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
FIG = os.path.join(HERE, 'figuras'); os.makedirs(FIG, exist_ok=True)
TMPL = open('fuente.cir.tmpl').read()
RV = dict(RV1VAL=109, RV2VAL=107, RV3VAL=28.3)       # cursores para 16.00 / -16.00 / 5.00 V

def g(pts):
    """conductancia por tramos: pts = [(t, G), ...] -> expresión pwl de ngspice"""
    if len(pts) == 1: return '%g' % pts[0][1]
    pts = list(pts) + [(100.0, pts[-1][1])]          # mantiene el último valor (pwl extrapola)
    s = ','.join('%g,%g' % (t, v) for t, v in pts)
    return 'pwl(time,%s)' % s

def cargas(gp, gn, g5, short_p=None, short_n=None, short_5=None):
    L = ['VMP p16 lp 0', 'VMN ln n16 0', 'VM5 p5 l5 0',
         'BLP lp 0 I = { V(lp)*%s }' % g(gp),
         'BLN 0 ln I = { -V(ln)*%s }' % g(gn),
         'BL5 l5 0 I = { V(l5)*%s }' % g(g5)]
    for nd, sh, nm in (('lp', short_p, 'SP'), ('ln', short_n, 'SN'), ('l5', short_5, 'S5')):
        if sh:
            t0, t1 = sh
            L.append('B%s %s 0 I = { V(%s)*pwl(time,0,0,%g,0,%g,20,%g,20,%g,0,100,0) }' % (nm, nd, nd, t0, t0+1e-4, t1, t1+1e-4))
    return '\n'.join(L)

GP = 0.2/16; G5 = 0.04/5           # 4 PID: 200 mA por riel; 4 sensores Hall: 40 mA
def run(name, kl, gp, gn, g5, tstop, rv=RV, **kw):
    net = TMPL.replace('{KLINEA}', str(kl)).replace('{TSTOP}', str(tstop)).replace('{OUT}', name+'.dat')
    net = net.replace('{CARGAS}', cargas(gp, gn, g5, **kw))
    for k, v in rv.items(): net = net.replace('{%s}' % k, str(v))
    open(name+'.cir', 'w').write(net)
    r = subprocess.run(['ngspice', '-b', name+'.cir'], capture_output=True, text=True)
    if not os.path.exists(name+'.dat'): print(r.stdout[-3000:], r.stderr[-3000:]); sys.exit(1)
    d = np.loadtxt(name+'.dat')
    t = d[:, 0]; cols = ['vrawp', 'vrawn', 'p16', 'n16', 'p5', 'ip', 'in', 'i5', 'vin1', 'vin2', 'vin3']
    D = {c: d[:, 2*i+1] for i, c in enumerate(cols)}; D['t'] = t
    return D

def win(D, t0, t1):
    m = (D['t'] >= t0) & (D['t'] <= t1); return {k: v[m] for k, v in D.items()}
def stats(x): return dict(mean=float(np.mean(x)), pp=float(np.ptp(x)), rms_ac=float(np.std(x)))

M = {}
plt.rcParams.update({'font.size': 8, 'axes.grid': True, 'grid.alpha': 0.3, 'figure.dpi': 150})
# ------------------------------------------------------------------ A. régimen nominal
A = run('A_nominal', 1.0, [(0, GP)], [(0, GP)], [(0, G5)], 0.8)
w = win(A, 0.7, 0.8)
for k in ('vrawp', 'vrawn', 'p16', 'n16', 'p5', 'vin1', 'vin2', 'vin3'): M['A_'+k] = stats(w[k])
for k in ('ip', 'in', 'i5'): M['A_'+k] = float(np.mean(w[k]))
fig, ax = plt.subplots(3, 1, figsize=(3.4, 4.6), sharex=True)
tt = (w['t']-0.7)*1e3
ax[0].plot(tt, w['vrawp'], label='$V_{RAW+}$ (C1)'); ax[0].plot(tt, w['vin1'], label='$V_{IN}$ U1'); ax[0].plot(tt, w['p16'], label='+16 V')
ax[0].set_ylabel('V'); ax[0].legend(fontsize=6, loc='lower right', ncol=3)
ax[1].plot(tt, (w['p16']-w['p16'].mean())*1e3, label='+16 V'); ax[1].plot(tt, (w['n16']-w['n16'].mean())*1e3, label='−16 V')
ax[1].plot(tt, (w['p5']-w['p5'].mean())*1e3, label='+5 V'); ax[1].set_ylabel('rizado (mV)'); ax[1].legend(fontsize=6, ncol=3)
ax[2].plot(tt, w['vrawn'], label='$V_{RAW-}$ (C2)'); ax[2].plot(tt, w['vin2'], label='$V_{IN}$ U2'); ax[2].plot(tt, w['n16'], label='−16 V')
ax[2].set_ylabel('V'); ax[2].set_xlabel('t (ms)'); ax[2].legend(fontsize=6, loc='upper right', ncol=3)
fig.tight_layout(); fig.savefig(FIG+'/sim_regimen.pdf'); fig.savefig(FIG+'/sim_regimen.png'); plt.close(fig)
# arranque
fig, ax = plt.subplots(figsize=(3.4, 2.0))
s = A['t'] <= 0.25
for k, lb in (('vrawp', '$V_{RAW+}$'), ('p16', '+16 V'), ('p5', '+5 V'), ('n16', '−16 V'), ('vrawn', '$V_{RAW-}$')):
    ax.plot(A['t'][s]*1e3, A[k][s], label=lb)
ax.set_xlabel('t (ms)'); ax.set_ylabel('V'); ax.legend(fontsize=6, ncol=3); fig.tight_layout()
fig.savefig(FIG+'/sim_arranque.pdf'); fig.savefig(FIG+'/sim_arranque.png'); plt.close(fig)
# ------------------------------------------------------------------ B. línea ±10 %
for kl, nm in ((0.9, 'B_baja'), (1.1, 'B_alta')):
    B = run(nm, kl, [(0, GP)], [(0, GP)], [(0, G5)], 0.6)
    w = win(B, 0.5, 0.6)
    for k in ('vrawp', 'vrawn', 'p16', 'n16', 'p5', 'vin1', 'vin2'): M[nm+'_'+k] = stats(w[k])
# línea baja con los trimmers al máximo (+16.95 / -16.97 V): margen de dropout
rvmax = dict(RV1VAL=200, RV2VAL=200, RV3VAL=50)
B = run('B_baja_max', 0.9, [(0, 0.2/17)], [(0, 0.2/17)], [(0, G5)], 0.6, rv=rvmax)
w = win(B, 0.5, 0.6)
for k in ('vrawp', 'p16', 'n16', 'vin1', 'vin2', 'p5'): M['B_baja_max_'+k] = stats(w[k])
# ------------------------------------------------------------------ C. escalones de carga
C = run('C_carga', 1.0, [(0, 0), (0.4, 0), (0.4001, GP/2), (0.6, GP/2), (0.6001, GP), (0.8, GP), (0.8001, GP/2)],
        [(0, 0), (0.4, 0), (0.4001, GP/2), (0.6, GP/2), (0.6001, GP), (0.8, GP), (0.8001, GP/2)],
        [(0, 0), (0.4, 0), (0.4001, G5/2), (0.6, G5/2), (0.6001, G5), (0.8, G5), (0.8001, G5/2)], 1.0)
for k in ('p16', 'n16', 'p5'):
    M['C_'+k+'_vacio'] = float(np.mean(win(C, 0.3, 0.4)[k]))
    M['C_'+k+'_media'] = float(np.mean(win(C, 0.5, 0.6)[k]))
    M['C_'+k+'_plena'] = float(np.mean(win(C, 0.7, 0.8)[k]))
    x = win(C, 0.6, 0.62)[k]; M['C_'+k+'_transitorio_mV'] = float((x.min() if k != 'n16' else x.max())*1e3 - M['C_'+k+'_media']*1e3)
    M['C_'+k+'_reg_%'] = 100*(abs(M['C_'+k+'_vacio'])-abs(M['C_'+k+'_plena']))/abs(M['C_'+k+'_plena'])
fig, ax = plt.subplots(4, 1, figsize=(3.4, 4.8), sharex=True)
s = C['t'] >= 0.3
ax[0].plot(C['t'][s], C['ip'][s]*1e3, label='$I_{+16}$ (carga)'); ax[0].plot(C['t'][s], C['in'][s]*1e3, '--', label='$I_{-16}$')
ax[0].plot(C['t'][s], C['i5'][s]*1e3, label='$I_{+5}$'); ax[0].set_ylabel('mA'); ax[0].legend(fontsize=6, ncol=3)
for a, k, lb in ((ax[1], 'p16', '+16 V'), (ax[2], 'n16', '−16 V'), (ax[3], 'p5', '+5 V')):
    a.plot(C['t'][s], C[k][s]*1e3 - M['C_'+k+'_vacio']*1e3); a.set_ylabel('Δ' + lb + ' (mV)')
ax[3].set_xlabel('t (s)'); fig.tight_layout(); fig.savefig(FIG+'/sim_carga.pdf'); fig.savefig(FIG+'/sim_carga.png'); plt.close(fig)
# ------------------------------------------------------------------ D. cortocircuitos
Dd = run('D_corto', 1.0, [(0, GP)], [(0, GP)], [(0, G5)], 1.7, short_p=(0.5, 0.7), short_n=(0.9, 1.1), short_5=(1.3, 1.5))
for nm, t0, t1, ki, kv in (('p16', 0.5, 0.7, 'ip', 'p16'), ('n16', 0.9, 1.1, 'in', 'n16'), ('p5', 1.3, 1.5, 'i5', 'p5')):
    w = win(Dd, t0+0.1, t1-0.005)
    M['D_'+nm+'_Icorto'] = float(np.mean(np.abs(w[ki]))); M['D_'+nm+'_Ipico'] = float(np.max(np.abs(win(Dd, t0, t1)[ki])))
    M['D_'+nm+'_Vcorto'] = float(np.mean(w[kv]))
    M['D_'+nm+'_recupera'] = float(np.mean(win(Dd, t1+0.1, t1+0.18)[kv]))
w = win(Dd, 1.35, 1.45); M['D_p16_durante_corto_5V'] = float(np.mean(w['p16']))
w = win(Dd, 0.6, 0.69); M['D_P_Q1_W'] = float(np.mean((w['vrawp'] - 1.8*np.abs(w['ip']) - w['vin1'])*np.abs(w['ip'])))
w = win(Dd, 1.0, 1.09); M['D_P_Q3_W'] = float(np.mean((-w['vrawn'] - 2.2*np.abs(w['in']) + w['vin2'])*np.abs(w['in'])))
fig, ax = plt.subplots(2, 1, figsize=(3.4, 3.4), sharex=True)
s = Dd['t'] >= 0.4
ax[0].plot(Dd['t'][s], Dd['p16'][s], label='+16 V'); ax[0].plot(Dd['t'][s], Dd['n16'][s], label='−16 V'); ax[0].plot(Dd['t'][s], Dd['p5'][s], label='+5 V')
ax[0].set_ylabel('V'); ax[0].legend(fontsize=6, ncol=3)
ax[1].plot(Dd['t'][s], np.abs(Dd['ip'][s]), label='$|I_{+16}|$'); ax[1].plot(Dd['t'][s], np.abs(Dd['in'][s]), label='$|I_{-16}|$'); ax[1].plot(Dd['t'][s], np.abs(Dd['i5'][s]), label='$|I_{+5}|$')
ax[1].set_ylabel('A'); ax[1].set_xlabel('t (s)'); ax[1].legend(fontsize=6, ncol=3, loc='upper right'); ax[1].set_ylim(0, 0.6)
for a in ax:
    for t0, t1 in ((0.5, 0.7), (0.9, 1.1), (1.3, 1.5)): a.axvspan(t0, t1, color='0.85', zorder=0)
fig.tight_layout(); fig.savefig(FIG+'/sim_corto.pdf'); fig.savefig(FIG+'/sim_corto.png'); plt.close(fig)
json.dump(M, open('resultados_simulacion.json', 'w'), indent=1)
for k, v in M.items(): print(k, v)
