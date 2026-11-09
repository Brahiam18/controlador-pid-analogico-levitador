# Simulación magnética del levitador

Fuerza sobre el imán (N42 Ø20×4,2 mm, ≈10 g) en repulsión con bobinas debajo: 652 espiras, devanado Ø33×23 mm, pestañas Ø36×3 mm, núcleo de hierro Ø6×45 mm centrado.

**Aviso:** las gráficas NO son de FEMM. Se calcularon con solvers propios en Python (FEMM no corre en el entorno donde se hicieron). Los scripts `femm/*.lua` permiten repetir el caso en FEMM y comparar.

| Carpeta | Contenido |
|---|---|
| `figuras/` | Mapa de campo y líneas de flujo, fuerza vs corriente, corriente de equilibrio vs altura (una bobina sobre el eje, FEM 2D axisimétrico) |
| `scripts/` | `lev.py` (Biot-Savart), `fem.py` (FEM 2D), `graf.py` (genera las figuras), `fem3d.py` y `run_4bobinas_3d.py` (FEM 3D, potencial escalar reducido, gmsh + scikit-fem + pyamg) |
| `femm/` | Scripts Lua para FEMM |

## Resultados (una bobina sobre el eje, FEM 2D)

| Altura sobre la pestaña | Corriente de equilibrio |
|---|---|
| 20 mm | 0,83 A |
| 25 mm | 0,68 A |
| 30 mm | 0,75 A |
| 35 mm | 0,98 A |

Atracción del núcleo sin corriente: ≈37 gf a 20 mm y ≈144 gf a 15 mm. Es la cota optimista; con las 4 bobinas fuera del eje del imán la corriente es mayor (ver resultados 3D cuando se agreguen).
