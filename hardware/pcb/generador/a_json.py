"""Convierte best_*.pkl (salida de buscar_modulo.py) a modulo_ruteado.json (entrada de build.py)."""
import pickle,json,sys
b=pickle.load(open(sys.argv[1],'rb'))
js=dict(wc=b['wc'],hc=b['hc'],assign=b['assign'],parts={k:list(v) for k,v in b['parts'].items()},
 routes={n:dict(edges=[[list(a),list(c)] for a,c in rt['edges']],vias=[list(v) for v in rt['vias']],nodes=[list(n_) for n_ in rt['nodes']]) for n,rt in b['routes'].items()})
json.dump(js,open(sys.argv[2],'w'))
print(b['assign'],b['wc'],b['hc'],'puentes',b['jumpers'],'tramos inf/sup',b['bot'],b['top'])
