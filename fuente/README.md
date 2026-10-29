# Fuente de alimentación ±16 V / 1,5 A y +5 V para los 4 PID del levitador

Proyecto de fuente (monografía *Electrónica Tomo II*, tema 3: reguladores de voltaje para fuentes DC). Alimenta los ocho TL074CN (±16 V), los cuatro sensores Hall y los divisores de `V_ref` (+5 V) de las dos tarjetas PID. Además, cada riel de ±16 V entrega **1,5 A** sobre una carga de prueba **removible** (`R_L` = 10 Ω en J4 o J5), para medir con y sin carga. Las bobinas usan una fuente aparte.

**Informe completo (IEEE, dos columnas):** [`informe/Informe_Fuente_Alimentacion.pdf`](informe/Informe_Fuente_Alimentacion.pdf)

![Esquemático completo](esquematicos/esq_completo.png)

## Versión 2 (especificación de 1,5 A)
La versión 1 solo alimentaba los operacionales (0,27 A por riel) con el transformador M509. Al pedirse 1,5 A en ±16 V, sin poder cambiar los reguladores LM317/LM337 y conservando las protecciones, se cambió lo siguiente:

| Bloque | Versión 2 |
|---|---|
| Transformador | **18‑0‑18 V / 3 A** (nuevo), toma central a GND |
| Rectificador | Puente D1–D4 1N5408, onda completa (120 Hz) para los dos rieles |
| Filtro | C1 = 15 000 µF (+) y C2A ‖ C2B = 2 × 6800 µF (−), todos de 50 V y ya disponibles. Rizado ≤ 1 V_pp con 1,6 A |
| Limitador | Antes de cada regulador: R_SC = 0,27 Ω / 5 W, Darlington TIP42C + BD140 (TIP41C + BD139 en −16 V) y sensor BC557 (BC547) con **foldback** (R5 = 270 Ω, R6 = 12 kΩ). Límite ≈ 2,4 A; corto 0,7–1,2 A, sin trabarse al arrancar con `R_L` |
| Ampliación de corriente | Fig. 3‑21 de la monografía: R7 = 2,7 Ω + TIP42C (R15 + TIP41C en −16 V). El LM317 lleva solo 0,26–0,39 A |
| Reguladores | U1 LM317 (+16 V), U2 LM337 (−16 V), los mismos de antes: R1 = 120 Ω, R2 = 1,3 kΩ + trimmer de 200 Ω |
| +5 V | U3 LM317 desde +16 V por R19 = 100 Ω / 3 W (sin cambios) |
| Protecciones | F1 T1 A (primario), F2 y F3 T3,15 A (cada mitad del secundario), foldback, R19, protección térmica interna, diodos OUT→IN, ADJ→OUT y de polaridad inversa |
| Disipadores | Uno de **≤ 2 °C/W por riel**, con Q1, Q2, Q4 y U1 (Q5, Q6, Q8 y U2), todos con mica y buje |

Simulación (ngspice): +15,98 / −15,98 V con 1,6 A; regulación de carga de 0,09 %; rizado de salida de 0,1 mV_pp; regula aun con la red al −10 %; cortos de 0,84 / 0,90 / 0,14 A con recuperación automática y `R_L` conectada.

**La carga de 1,5 A se prueba en un riel a la vez** (el transformador de 3 A no da para los dos a la vez con la red baja).

## Carpetas
| Carpeta | Contenido |
|---|---|
| `informe/` | Informe en LaTeX (IEEEtran) y PDF, con sus figuras |
| `calculos/` | `calculos.py`: todos los cálculos del diseño. `resultados_calculos.json`: sus resultados |
| `esquematicos/` | Esquemáticos por etapa y completo (circuitikz: PDF, PNG y fuente `.tikz`) |
| `simulacion/` | Netlist, modelos, script de ngspice, gráficas y resultados |
| `hardware/pcb/` | **EAGLE/Fusion** (`fuente.sch`, `fuente.brd`), **cobre espejado 1:1**, hoja de ensamble, puentes, guía de conexión y generador |
| `hardware/` | Lista de materiales (`.md` y `.csv`) |
| `pruebas/` | Plan de pruebas y tabla de mediciones para llenar (`mediciones.csv`) |

## Conexión rápida
- Secundario 18‑0‑18 V: extremo A a **J1‑1**, toma central a **J1‑2 (GND)** y extremo B a **J1‑3**.
- **J2** (+16 / −16 / GND / +5) va a `J_PWR` (pines 1‑2‑3‑4) de una tarjeta PID. La segunda tarjeta se une a la primera por su `J_PWR`.
- **J4** (+16 V, GND) y **J5** (−16 V, GND): carga de prueba `R_L` = 10 Ω ≥ 30 W, atornillada solo para la prueba de 1,5 A.
- GND y PGND se unen **solo** en un `JP_GND` de las tarjetas PID, nunca en esta fuente.

## Recompilar
```bash
cd calculos && python3 calculos.py
cd ../simulacion && python3 simular.py              # requiere ngspice
cd ../informe && latexmk -pdf informe_fuente.tex    # requiere IEEEtran y circuitikz
cd ../hardware/pcb/generador && python3 build.py placa_ruteada.json ..   # requiere shapely y matplotlib
```
