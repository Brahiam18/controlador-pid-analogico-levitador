# Errata y pendientes del informe

Revisión de consistencia del informe `Informe_PID_Analogico_Levitador.pdf` frente a la nomenclatura vigente ([`nomenclatura.md`](nomenclatura.md)). **El texto del informe se conserva como fue entregado** (solo se actualizaron la Tabla I con las mediciones prácticas y las fotografías del montaje); esta lista sirve para preparar una versión 1.1.

Las referencias de sección, ecuación y figura son las del PDF.

## A. Inconsistencias de nomenclatura

| N.º | Dónde | Observación | Corrección sugerida |
|:-:|---|---|---|
| 1 | Tabla II (nomenclatura general) | Conserva los nombres de la primera versión: `R_f1`, `R6` como fuga, `R7` en serie con `C2`, `R8`–`R12` en el sumador, `R13`/`R14` para `V_ref`, `R15`/`R16` para `V_off`. Falta `R2`, `R_offset` y `R_bias`. | Rehacer la tabla con la nomenclatura vigente. |
| 2 | Secciones II-C, II-D y III-D | II-C llama `R6` a la resistencia de fuga y escribe `τ = R6·Ci` (ahora es `R11`). II-D dice que `R7` va en serie con `C2` y III-D calcula `R7 ≤ 1/(2π·f_c·C2) = 1.06 kΩ` (ahora es `R6`). | Cambiar `R6 → R11` en II-C y `R7 → R6` en II-D y III-D. |
| 3 | Sección III-E, párrafo previo a la Ec. (35) | El texto "`R8 = R9 = R10 = R7 kΩ`" quedó sin sentido. | Escribir "`R7 = R8 = R9 = R10 = 10 kΩ`". |
| 4 | Tabla III, columna "Obs." | `R8`, `R9` y `R10` conservan los roles anteriores ("Entrada `V_P`", "Entrada `V_I`", "Entrada `V_D`"). | Vigente: `R7` ← `V_P`, `R8` ← `V_I`, `R9` ← `V_D`, `R10` = realimentación del sumador. |
| 5 | Ec. (51), `R_bias` | Cuatro resistencias de 10 kΩ en paralelo dan **2.5 kΩ**, no 4.4 kΩ (tres dan 3.3 kΩ, como en la Ec. 39). | Verificar qué valor se usó en Proteus y en el montaje y corregir la ecuación o el valor. |
| 6 | Sección III-F, Fig. 21 (manuscrita) y Tabla III / Fig. 8 | El texto y la Fig. 21 usan `R13 = 160 kΩ` (fija) y calculan `R12`; la Tabla III y el esquemático de Proteus usan `R12 = 160 kΩ` y `R13 = 240 kΩ`. Además el texto calcula con `V_CC = 16 V` (`R12 = 1.12 MΩ`) y el montaje usa 5 V (`240 kΩ`). | Unificar nombres y fuente de alimentación; luego eliminar el recuadro de "Nota de verificación". |

## B. Ecuaciones y cifras

| N.º | Dónde | Observación | Corrección sugerida |
|:-:|---|---|---|
| 7 | Ec. (46) y (48) | El término de offset está escrito como `(1/10k)(10)`; debe ser `(1k/10k)(10) = 1 V`. Además usan `13.3` para el aporte del integrador, mientras que la Ec. (45) y la Tabla I usan `13.5`. | Corregir ambos términos. |
| 8 | Ec. (2) vs. Ec. (19) y Tabla I | La Ec. (2) define `V_e = (R2/R1)(V_ref − V_sensor)`, mientras que la Ec. (19) y la Tabla I usan `V_sensor − V_ref`. | Fijar un solo convenio de signo y comprobarlo con el esquemático. |
| 9 | Ec. (24) vs. Ec. (29) y Tabla III | La Ec. (24) da `Pot2 = 10 kΩ` (con `R11 ≈ 800 kΩ`, Ec. 23); la Ec. (29) y la Tabla III usan `Pot2 = 12.5 kΩ` y `R11 = 1 MΩ`. En ambos casos `K_max = 80`, pero con valores distintos. | Unificar el diseño teórico de partida. |
| 10 | Secciones III-A y IV-A, Fig. 14 | Se mencionan alimentaciones de ±16 V (diseño) y de 18 V como máximo, y la hoja manuscrita de la Fig. 14 indica `V_CC = 18 V`. | Confirmar con qué tensión se midió el montaje y declararla una sola vez. |

## C. Figuras y redacción

| N.º | Dónde | Observación | Corrección sugerida |
|:-:|---|---|---|
| 11 | Figs. 3 y 4 | Los pies de figura están intercambiados: la Fig. 3 ("integrador") muestra el derivador (`Pot3`, `C2`, `R6`) y la Fig. 4 ("derivador") muestra el integrador (`Pot2`, `R11`, `C1`). | Intercambiar los pies. |
| 12 | Figs. 7 y 8 | Ambas tienen el pie "Esquemático en Proteus del controlador PID completo", pero muestran los buffers de `V_off` (U7) y `V_ref` (U6). | Cambiar los pies a "Divisor y buffer de `V_off`" y "Divisor y buffer de `V_ref`". |
| 13 | Varios | Ortografía y redacción: "proteous", "Esquematico", "Ecuacion", "practicos", "encuetran", "apartado IV" (es la Sección IV). En IV-A, "ganancia (la cual era de 23.24 V)" mezcla ganancia y tensión (es la salida del sumador). | Revisar. |

## D. Estado de los datos del laboratorio

- [x] **Tabla I:** la columna "Práctico" ya contiene las mediciones reales (ver [`../datos/mediciones_practicas.csv`](../datos/mediciones_practicas.csv)).
- [x] **Fotografías del montaje:** Figs. 10 a 12 del informe (ver [`../informe/figuras/pruebas/`](../informe/figuras/pruebas/)).
- [ ] **Tabla III:** `R14` figura como "falta medir".
- [ ] **Texto de la Sección V-B:** sigue sin comentar los resultados de la Tabla I (en especial, la etapa integral con error mínimo y la derivativa con error máximo).
- [ ] **Capturas de osciloscopio:** repetir con escala legible (500 mV/div o menos) y señal de 10 Hz, 1 Vpp, offset 2 V.
- [ ] **Apéndice, Tabla IV:** actualizar el índice de anexos si se agregan nuevas imágenes (las filas 2 y 14–19 siguen reservadas).
- [ ] Archivo del proyecto de **Proteus** (`.pdsprj`), aún no incluido en el repositorio.
