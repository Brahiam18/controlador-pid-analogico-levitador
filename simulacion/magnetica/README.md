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

## Resultados (4 bobinas con núcleo, FEM 3D)

Las 4 bobinas (centros en ±18,5 ; ±18,5 mm), cada una con núcleo Ø6×45 mm, todas con la misma corriente, imán centrado sobre el cuadrado. `F1` es la fuerza total por amperio (las 4 bobinas en serie o iguales), `I eq` la corriente por bobina para sostener ≈10 g. Dos mallas (`hc` = tamaño de elemento cerca del hierro y el imán); los datos crudos están en `scripts/res4coil.json`.

| Altura sobre la pestaña | F1 (gf/A) malla gruesa / fina | I eq por bobina (A) |
|---|---|---|
| 20 mm | 0,1 / 0,4 | no converge: casi no hay fuerza útil |
| 25 mm | 9,2 / 8,8 | 1,16 / 1,21 |
| 30 mm | 12,3 / 11,5 | 0,87 / 0,92 |
| 35 mm | 12,4 / 11,6 | 0,85 / 0,91 |

Lectura: con 4 bobinas fuera del eje del imán, la corriente necesaria a 30 mm es ≈0,9–1,0 A por bobina, no los 0,75 A del caso de una sola bobina sobre el eje. A 20 mm la fuerza útil casi desaparece y el resultado depende de la malla; no se debe usar esa altura. La malla fina baja F1 un 6–8 %, y en la validación con una bobina el solver 3D sobreestimó F1 ≈14 % respecto al 2D, así que la incertidumbre es de unos ±15 % y la corriente real podría ser algo mayor (≈1,0–1,1 A a 30 mm). Esto confirma que conviene alimentar con 12 V o más y verificar la corriente de despegue en el montaje real.
