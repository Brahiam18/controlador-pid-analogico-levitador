import sys
def tabla(jl):
    L=['| N.º | Red | Longitud aprox. | Extremos |','|:-:|---|--:|---|']
    for k,j in enumerate(jl,1):
        L.append('| J%d | `%s` | %d mm | %s |'%(k,j['net'],round(j['length']),' ↔ '.join(j['ends'])))
    return '\n'.join(L)
