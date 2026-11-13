# Estado del proyecto: controlador PID analógico para levitador magnético

Resumen para retomar el trabajo (actualizado 2026-11-13). Plan de trabajo para 2027 en [`plan_2027.md`](plan_2027.md) y guía de depuración en [`guia_depuracion.md`](guia_depuracion.md).

## Estado a noviembre de 2026
- **No se presentó en la 50ª muestra METIE (2026).** Los 4 PID funcionaban, pero no dio el tiempo para encontrar los `V_ref` con los que el imán quedara estable a 3 cm. Se presentó el póster ([`poster_metie/`](poster_metie/)) y quedó el montaje armado para seguir trabajando.
- **Qué funciona:** las 4 cadenas PID (error, P, I, D, sumador, `V_ref`, `V_off`), el convertidor V-I con TIP122 y la corriente por bobina (≈0,2–0,25 V en el emisor para ≈0,6–0,75 A), y la base impresa en 3D con las 4 bobinas y los 4 sensores. Fotos en [`../pruebas/montaje/`](../pruebas/montaje/).
- **Qué falta:** levitación estable. Causas identificadas:
  1. **Encontrar los `V_ref` de cada PID para 3 cm toma demasiado tiempo** con el procedimiento actual (ajuste a mano, uno por uno). Falta una forma más rápida.
  2. **Los sensores ven una variación muy pequeña del campo** (≈2,4 V con poca variación) y la configuración de las resistencias de los PID hay que modificarla para aprovechar esa señal.
- **Idea para 2027:** presentarlo en la muestra METIE como proyecto de dos materias, si es posible (por definir).

## Qué hay
- 4 PID analógicos idénticos en paralelo (U1 error, U2 P, U3 I, U4 D, U5 sumador, U6 Vref, U7 Voff, U8 convertidor V-I) con 2 × TL074CN por PID.
- Etapa de potencia por PID: TIP122 + resistencias de sensado 3 × 1 Ω / 5 W en paralelo (0,33 Ω) + diodo 1N5408 en la bobina. La consigna del U8 sale del divisor `R17` + `POT4` + `R16`; `I = V_emisor / 0,33 Ω`.
- PCB: dos tarjetas idénticas de 2 PID (170,2 × 116,8 mm), archivos y hojas de impresión en `hardware/pcb/`. Guía de colores por red: `hardware/pcb/guia_colores_conexiones.pdf`.
- Estructura: base impresa en 3D rediseñada tras las pruebas (dos placas con separadores y soportes de sensor); modelos y generador en `hardware/mecanica/`.
- Sensor: Hall SS495A (~3,1 mV/G, ~2,5 V sin campo). Vref fijo 2 V (R12 160k / R13 240k); para ajustarlo, R12 se cambia por un pot de 500k como reóstato.
- Simulación: FEM 2D/3D con solvers propios en Python (no FEMM) en `simulacion/magnetica/`; corriente de equilibrio ≈0,7 A por bobina a 30 mm (±15 %). Visualización del campo y video en [`simulacion_campo/`](simulacion_campo/).

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
- Ver [`plan_2027.md`](plan_2027.md) para el trabajo de levitación.
- Informe, lista de materiales U1–U7 y Tabla I aún dicen LM741; corregir a TL074CN.
- Aplicar la fe de erratas v1.1 del informe y comentar los resultados de la Tabla I.
- Reabrir los nuevos `.sch`/`.brd` en Fusion (borrar `pid4_levitador` y subir `pid2_levitador`).
- Vref ajustable (pot de 500k) y compensación del campo de la bobina (Rc) todavía no están en la PCB.
- Fotos de los 4 PID con el objeto levitando y `V_ref` por altura en `pruebas/levitacion/` (cuando se logre).
- Fuente ±16 V / 1,5 A y +5 V (monografía, tema 3), versión 2, en `fuente/`: transformador 18-0-18 V / 3 A (por comprar), puente 1N5408, C1 15 000 µF y 2 × 6800 µF, limitador con foldback (Darlington TIP42C/BD140) y ampliación de corriente TIP42C/TIP41C alrededor de los mismos LM317/LM337. Carga de prueba R_L = 10 Ω removible en J4/J5 (un riel a la vez). Disipador ≤ 2 °C/W por riel. Placa 190,5 × 139,7 mm con 7 puentes. Falta comprar, fabricar, montar y llenar `fuente/pruebas/mediciones.csv`.
