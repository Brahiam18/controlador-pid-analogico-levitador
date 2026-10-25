# Estado del proyecto: controlador PID analógico para levitador magnético

Resumen para retomar el trabajo en otra conversación (actualizado 2026-10-25).

## Qué hay
- 4 PID analógicos idénticos en paralelo (U1 error, U2 P, U3 I, U4 D, U5 sumador, U6 Vref, U7 Voff, U8 convertidor V-I) con 2 × TL074CN por PID.
- Etapa de potencia por PID: TIP122 + resistencias de sensado 3 × 1 Ω / 5 W en paralelo (0,33 Ω) + diodo 1N5408 en la bobina.
- PCB: dos tarjetas idénticas de 2 PID (170,2 × 116,8 mm), archivos y hojas de impresión en `hardware/pcb/`. Guía de colores por red: `hardware/pcb/guia_colores_conexiones.pdf`.
- Sensor: Hall SS495A (~3,1 mV/G, ~2,5 V sin campo). Vref fijo 2 V (R12 160k / R13 240k); para ajustarlo, R12 se cambia por un pot de 500k como reóstato.

## Requisitos de alimentación (para diseñar la fuente)
| Riel | Uso | Corriente aproximada |
|---|---|---|
| +16 V / −16 V | TL074 (±) | decenas de mA por PID (unos 10 mA por TL074 en reposo; prever 50 mA por PID con margen) |
| +5 V | divisor de Vref (R13) y sensor Hall | unos 10 mA por PID (Hall) |
| +VBOB | bobina | I = 3·k·VPID; hasta 4,5 A con VPID = 3 V; típico 1 A por voltio |
| GND / PGND | retorno de señal / de potencia | se unen en un solo punto con JP_GND |

- Disipación del TIP122: P = (Vbob − I·(Rbobina + 0,33))·I con Vce mínimo 2 V. Ejemplos (20 V, 2 Ω): 31 W a 2 A y 39 W a 3 A, así que hace falta disipador.
- Los rieles de señal (±16 V, +5 V) deben ser limpios (bajo ruido) y la bobina puede ir con una fuente aparte, con negativo unido a PGND.

## Pendiente
- Informe, lista de materiales U1–U7 y Tabla I aún dicen LM741; corregir a TL074CN.
- Aplicar la fe de erratas v1.1 del informe y comentar los resultados de la Tabla I.
- Reabrir los nuevos `.sch`/`.brd` en Fusion (borrar `pid4_levitador` y subir `pid2_levitador`).
- Vref ajustable (pot de 500k) y compensación del campo de la bobina (Rc) todavía no están en la PCB.
- Montaje práctico: grabado de las dos tarjetas (revisar cortos +16 V / GND antes de soldar), soldadura y pruebas.
- Fuente ±16 V / +5 V (monografía, tema 3) diseñada en `fuente/`: informe, esquemáticos, simulación, PCB (EAGLE + cobre 1:1), lista de materiales y plan de pruebas. Falta fabricar, montar y llenar `fuente/pruebas/mediciones.csv`.
