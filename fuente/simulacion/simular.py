"""Simulaciones de la fuente ±16 V / 1,5 A y +5 V (versión 2) en ngspice.
Uso: python3 simular.py      (requiere ngspice)  ->  figuras/ y resultados_simulacion.json
"""
import subprocess, numpy as np, json, os, sys
from multiprocessing import Pool
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
FIG = os.path.join(HERE, 'figuras'); os.makedirs(FIG, exist_ok=True)
TMPL = open('fuente.cir.tmpl').read()
RV = dict(RV1VAL=109, RV2VAL=107, RV3VAL=28.3)
COLS = ['vrawp', 'vrawn', 'p16', 'n16', 'p5', 'ip', 'in', 'i5', 'va1', 'va2', 'e1', 'e2', 'ia', 'ib', 'iq', 'in1']
G_PID = 0.2/16; G_RL = 1/10.0; G5 = 0.04/5

def pwl(pts):
    if len(pts) == 1: return '%g' % pts[0][1]
    pts = list(pts) + [(100.0, pts[-1][1])]
    return 'pwl(time,%s)' % ','.join('%g,%g' % p for p in pts)

def cargas(gp, gn, g5, shorts=()):
    L = ['VMP p16 lp 0', 'VMN ln n16 0', 'VM5 p5 l5 0',
         'BLP lp 0 I = { V(lp)*%s }' % pwl(gp), 'BLN 0 ln I = { -V(ln)*%s }' % pwl(gn), 'BL5 l5 0 I = { V(l5)*%s }' % pwl(g5)]
    for i, (nd, t0, t1) in enumerate(shorts):
        L.append('BS%d %s 0 I = { V(%s)*pwl(time,0,0,%g,0,%g,20,%g,20,%g,0,100,0) }' % (i, nd, nd, t0, t0+1e-4, t1, t1+1e-4))
    return '\n'.join(L)

def run(args):
    name, kl, gp, gn, g5, tstop, shorts = args
    tm = TMPL
    if name.startswith('F_'):          # curva V-I: fuente no regulada reemplazada por DC sin rizado
        a = tm.index('VA1 '); b = tm.index('C1 vrawp')
        tm = tm[:a] + 'VRP vrawp 0 %g\nVRN 0 vrawn %g\n' % (kl, kl) + tm[b:]
        tm = tm.replace('i(VA1) i(VB1)', 'i(VRP) i(VRN)')
    net = tm.replace('{KL}', str(kl)).replace('{TSTOP}', str(tstop)).replace('{OUT}', name+'.dat')
    net = net.replace('{CARGAS}', cargas(gp, gn, g5, shorts))
    for k, v in RV.items(): net = net.replace('{%s}' % k, str(v))
    open(name+'.cir', 'w').write(net)
    r = subprocess.run(['ngspice', '-b', name+'.cir'], capture_output=True, text=True)
    if not os.path.exists(name+'.dat'): return name, None, r.stdout[-2000:]
    d = np.loadtxt(name+'.dat'); os.remove(name+'.dat'); os.remove(name+'.cir')
    D = {c: d[:, 2*i+1] for i, c in enumerate(COLS)}; D['t'] = d[:, 0]
    return name, D, ''

def win(D, t0, t1, dt=10e-6):
    """ventana remuestreada a paso uniforme (los promedios quedan ponderados en el tiempo)"""
    tu = np.arange(t0, t1, dt)
    return {k: (tu if k == 't' else np.interp(tu, D['t'], v)) for k, v in D.items()}
def st(x): return dict(mean=float(np.mean(x)), pp=float(np.ptp(x)), rms_ac=float(np.std(x)))
def rms(x): return float(np.sqrt(np.mean(x**2)))

PID_P = [(0, G_PID)]; PID_N = [(0, G_PID)]; RLP = [(0, G_PID+G_RL)]; RLN = [(0, G_PID*0+G_RL)]
JOBS = [
 ('A_p', 1.0, [(0, G_RL)], PID_N, [(0, G5)], 0.6, ()),                 # RL en +16, PID en -16
 ('A_n', 1.0, PID_P, [(0, G_RL)], [(0, G5)], 0.6, ()),                 # RL en -16
 ('B_baja', 0.9, [(0, G_RL)], [(0, G_RL)], [(0, G5)], 0.6, ()),        # linea -10 %, RL en ambos (peor caso)
 ('B_alta', 1.1*1.0, [(0, G_RL)], PID_N, [(0, G5)], 0.6, ()),         # linea +10 %
 ('C_carga', 1.0, [(0, G_PID), (0.4, G_PID), (0.4001, G_PID+G_RL), (0.7, G_PID+G_RL), (0.7001, G_PID)],
                  [(0, G_PID), (0.4, G_PID), (0.4001, G_PID+G_RL), (0.7, G_PID+G_RL), (0.7001, G_PID)], [(0, G5)], 1.0, ()),
 ('D_corto', 1.0, [(0, G_RL)], [(0, G_RL)], [(0, G5)], 1.7, (('lp', 0.5, 0.7), ('ln', 0.9, 1.1), ('l5', 1.3, 1.5))),
 ('E_arranque_alta', 1.1, [(0, G_RL)], [(0, G_RL)], [(0, G5)], 0.4, ()),
 ('E_arranque_baja', 0.9, [(0, G_RL)], [(0, G_RL)], [(0, G5)], 0.4, ()),
 ('F_vi_baja', 20.3, [(0, 0), (0.15, 0.02), (0.6, 0.2), (0.85, 2), (1.0, 40)], PID_N, [(0, G5)], 1.0, ()),
 ('F_vi_nom', 23.0, [(0, 0), (0.15, 0.02), (0.6, 0.2), (0.85, 2), (1.0, 40)], PID_N, [(0, G5)], 1.0, ()),
 ('F_vi_alta', 25.6, [(0, 0), (0.15, 0.02), (0.6, 0.2), (0.85, 2), (1.0, 40)], PID_N, [(0, G5)], 1.0, ()),
]
if __name__ == '__main__':
    with Pool(4) as pool: res = dict((n, (D, e)) for n, D, e in pool.map(run, JOBS))
    for n, (D, e) in res.items():
        if D is None: print('FALLO', n, e); sys.exit(1)
    S = {n: D for n, (D, e) in res.items()}
    M = {}
    for n in ('A_p', 'A_n', 'B_baja', 'B_alta'):
        w = win(S[n], 0.5, 0.6)
        for k in ('vrawp', 'vrawn', 'p16', 'n16', 'p5', 'va1', 'va2', 'e1'): M[n+'_'+k] = st(w[k])
        for k in ('ip', 'in', 'i5', 'iq'): M[n+'_'+k] = float(np.mean(np.abs(w[k])))
        M[n+'_Irms_mitad_A'] = rms(w['ia']); M[n+'_Irms_mitad_B'] = rms(w['ib'])
        M[n+'_P_darl1'] = float(np.mean((w['e1']-w['va1'])*np.abs(w['ip']+0)))
    C = S['C_carga']
    for k in ('p16', 'n16', 'p5'):
        M['C_%s_sin_RL' % k] = float(np.mean(win(C, 0.3, 0.4)[k])); M['C_%s_con_RL' % k] = float(np.mean(win(C, 0.6, 0.7)[k]))
        M['C_%s_reg_%%' % k] = 100*(abs(M['C_%s_sin_RL' % k]) - abs(M['C_%s_con_RL' % k]))/abs(M['C_%s_con_RL' % k])
        x = win(C, 0.4, 0.45)[k]; M['C_%s_transitorio_mV' % k] = float((x.min() if k != 'n16' else x.max())*1e3 - M['C_%s_sin_RL' % k]*1e3)
    Dd = S['D_corto']
    for nm, t0, t1, ki, kv in (('p16', 0.5, 0.7, 'ip', 'p16'), ('n16', 0.9, 1.1, 'in', 'n16'), ('p5', 1.3, 1.5, 'i5', 'p5')):
        w = win(Dd, t0+0.1, t1-0.005)
        M['D_%s_Icorto' % nm] = float(np.mean(np.abs(w[ki]))); M['D_%s_Vcorto' % nm] = float(np.mean(w[kv]))
        M['D_%s_recupera_con_RL' % nm] = float(np.mean(win(Dd, t1+0.12, t1+0.19)[kv]))
    w = win(Dd, 0.6, 0.69); M['D_P_darl_p'] = float(np.mean((w['e1']-w['va1'])*np.abs(w['ip'])))
    w = win(Dd, 1.0, 1.09); M['D_P_darl_n'] = float(np.mean((w['va2']-w['e2'])*np.abs(w['in'])))
    for n in ('E_arranque_alta', 'E_arranque_baja'):
        w = win(S[n], 0.3, 0.4); M[n+'_p16'] = float(np.mean(w['p16'])); M[n+'_n16'] = float(np.mean(w['n16']))
    for n in ('F_vi_baja', 'F_vi_nom', 'F_vi_alta'):
        D = win(S[n], 0.15, 1.0, 50e-6); I = np.abs(D['ip']); V = D['p16']
        M[n+'_Imax'] = float(I.max()); M[n+'_I_a_1V'] = float(np.interp(1.0, V[::-1], I[::-1])) if V.min() < 1 else None
        M[n+'_I_a_15V9'] = float(I[np.argmax(V < 15.9)]) if (V < 15.9).any() else None
    json.dump(M, open('resultados_simulacion.json', 'w'), indent=1)
    for k, v in M.items(): print(k, v)
    # ---------------- figuras ----------------
    plt.rcParams.update({'font.size': 8, 'axes.grid': True, 'grid.alpha': 0.3, 'figure.dpi': 150})
    w = win(S['A_p'], 0.5, 0.6); tt = (w['t']-0.5)*1e3
    fig, ax = plt.subplots(3, 1, figsize=(3.4, 4.6), sharex=True)
    ax[0].plot(tt, w['vrawp'], label='$V_{RAW+}$'); ax[0].plot(tt, w['va1'], label='$V_{A1}$'); ax[0].plot(tt, w['p16'], label='+16 V')
    ax[0].set_ylabel('V'); ax[0].legend(fontsize=6, ncol=3, loc='lower right')
    ax[1].plot(tt, (w['p16']-w['p16'].mean())*1e3, label='+16 V (1,6 A)'); ax[1].plot(tt, (w['p5']-w['p5'].mean())*1e3, label='+5 V')
    ax[1].set_ylabel('rizado (mV)'); ax[1].legend(fontsize=6, ncol=2)
    ax[2].plot(tt, np.abs(w['ip']), label='$I_{+16}$'); ax[2].plot(tt, np.abs(w['iq']), label='booster Q4'); ax[2].plot(tt, np.abs(w['ip'])-np.abs(w['iq']), label='LM317 (aprox.)')
    ax[2].set_ylabel('A'); ax[2].set_xlabel('t (ms)'); ax[2].legend(fontsize=6, ncol=3)
    fig.tight_layout(); fig.savefig(FIG+'/sim_regimen.pdf'); fig.savefig(FIG+'/sim_regimen.png'); plt.close(fig)
    fig, ax = plt.subplots(3, 1, figsize=(3.4, 4.2), sharex=True); s = C['t'] >= 0.3
    ax[0].plot(C['t'][s], np.abs(C['ip'][s]), label='$I_{+16}$'); ax[0].plot(C['t'][s], np.abs(C['in'][s]), '--', label='$I_{-16}$'); ax[0].set_ylabel('A'); ax[0].legend(fontsize=6)
    ax[1].plot(C['t'][s], (C['p16'][s]-M['C_p16_sin_RL'])*1e3); ax[1].set_ylabel('Δ+16 V (mV)')
    ax[2].plot(C['t'][s], (C['n16'][s]-M['C_n16_sin_RL'])*1e3); ax[2].set_ylabel('Δ−16 V (mV)'); ax[2].set_xlabel('t (s)')
    fig.tight_layout(); fig.savefig(FIG+'/sim_carga.pdf'); fig.savefig(FIG+'/sim_carga.png'); plt.close(fig)
    fig, ax = plt.subplots(2, 1, figsize=(3.4, 3.4), sharex=True); s = Dd['t'] >= 0.4
    for k, lb in (('p16', '+16 V'), ('n16', '−16 V'), ('p5', '+5 V')): ax[0].plot(Dd['t'][s], Dd[k][s], label=lb)
    for k, lb in (('ip', '$|I_{+16}|$'), ('in', '$|I_{-16}|$'), ('i5', '$|I_{+5}|$')): ax[1].plot(Dd['t'][s], np.abs(Dd[k][s]), label=lb)
    ax[0].set_ylabel('V'); ax[0].legend(fontsize=6, ncol=3, loc='center right'); ax[1].set_ylabel('A'); ax[1].set_ylim(0, 3); ax[1].set_xlabel('t (s)'); ax[1].legend(fontsize=6, ncol=3, loc='upper right')
    for a in ax:
        for t0, t1 in ((0.5, 0.7), (0.9, 1.1), (1.3, 1.5)): a.axvspan(t0, t1, color='0.85', zorder=0)
    fig.tight_layout(); fig.savefig(FIG+'/sim_corto.pdf'); fig.savefig(FIG+'/sim_corto.png'); plt.close(fig)
    fig, ax = plt.subplots(figsize=(3.4, 2.4))
    for n, lb in (('F_vi_baja', '$V_{RAW+}$ = 20,3 V (red −10 %)'), ('F_vi_nom', '$V_{RAW+}$ = 23,0 V (nominal)'), ('F_vi_alta', '$V_{RAW+}$ = 25,6 V (red +10 %)')):
        D = win(S[n], 0.15, 1.0, 50e-6); ax.plot(np.abs(D['ip']), D['p16'], label=lb)
    ig = np.linspace(0, 1.8, 10); ax.plot(ig, ig*10, 'k:', lw=0.8, label='recta de carga $R_L$ = 10 Ω')
    ax.set_xlabel('$I_{+16}$ (A)'); ax.set_ylabel('$V_{+16}$ (V)'); ax.set_xlim(0, 3); ax.set_ylim(0, 18); ax.legend(fontsize=5.5, loc='center left', bbox_to_anchor=(0.0, 0.45))
    fig.tight_layout(); fig.savefig(FIG+'/sim_foldback.pdf'); fig.savefig(FIG+'/sim_foldback.png'); plt.close(fig)
    fig, ax = plt.subplots(figsize=(3.4, 2.1))
    for n, ls in (('E_arranque_baja', '-'), ('E_arranque_alta', '--')):
        D = S[n]; s = D['t'] <= 0.3
        ax.plot(D['t'][s]*1e3, D['p16'][s], ls, label='+16 V, red %s' % ('−10 %' if 'baja' in n else '+10 %'))
        ax.plot(D['t'][s]*1e3, D['n16'][s], ls, label='−16 V, red %s' % ('−10 %' if 'baja' in n else '+10 %'))
    ax.set_xlabel('t (ms)'); ax.set_ylabel('V'); ax.legend(fontsize=6, ncol=2); fig.tight_layout()
    fig.savefig(FIG+'/sim_arranque.pdf'); fig.savefig(FIG+'/sim_arranque.png'); plt.close(fig)
