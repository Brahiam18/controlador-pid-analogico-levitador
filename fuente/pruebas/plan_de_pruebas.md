# Plan de pruebas: fuente ±16 V / 1,5 A y +5 V (versión 2)

Los valores "esperados" salen del cálculo (`calculos/`) y de la simulación (`simulacion/`). Llene la columna "Medido" de `mediciones.csv` y calcule el error.

**Instrumentos:** multímetro digital (V DC, V AC, A DC hasta 10 A), osciloscopio de 2 canales con punta ×1/×10, termómetro o termopar y un reloj.

**Carga de prueba RL (removible):** 10 Ω de al menos 30 W (resistencia de aluminio), o 4 × 39 Ω de 10 W en paralelo (9,75 Ω). Se atornilla en **J4** para probar +16 V o en **J5** para probar −16 V. Así se mide sin carga y con carga sin desoldar nada. Disipa unos 26 W y **quema**: póngala sobre una superficie que aguante el calor.

| Carga | Valor | Corriente | Uso |
|---|---|---|---|
| RL en J4 o J5 | 10 Ω / ≥ 30 W | 1,60 A | Especificación (≥ 1,5 A) |
| Media carga | 22 Ω / 25 W | 0,73 A | Regulación intermedia |
| +5 V | 120 Ω / 1/2 W | 42 mA | Plena carga de +5 V |

Los 1,5 A se prueban **en un riel a la vez**, como se definió para el transformador de 3 A.

## P0. Inspección sin energía
1. Revise la polaridad de C1, C2A, C2B, C6, C7, C9, C11, C12, C14, C15, C17 y C18, de los diodos y de los LED. En el riel negativo, el positivo de los condensadores va a GND.
2. Mida continuidad (no debe haber corto) entre: `+16V`–`GND`, `-16V`–`GND`, `+5V`–`GND`, `V_RAW+`–`GND`, `V_RAW-`–`GND` y `+16V`–`-16V`.
3. Verifique el aislamiento entre cada aleta y el disipador (Q1, Q2, Q4, U1, Q5, Q6, Q8, U2): debe ser circuito abierto.
4. Ponga RV1, RV2 y RV3 a mitad de recorrido.

## P1. Primer encendido sin carga
1. Sin RL ni tarjetas PID, encienda con F1, F2 y F3 puestos.
2. Mida V AC entre J1‑1 y J1‑2, y entre J1‑2 y J1‑3. Se esperan unos 18–20 V rms en cada mitad.
3. Mida V_RAW+ y V_RAW− en J3. Se esperan unos ±25 a ±28 V sin carga.
4. Los tres LED deben encender.

## P2. Ajuste
Con RV1, RV2 y RV3, lleve las salidas a 16,00 V, −16,00 V y 5,00 V. Anote el rango completo de cada trimmer.

## P3. Corriente nominal y regulación de carga (RL removible)
1. Mida +16 V sin RL (V_ro).
2. Atornille RL en J4 y mida +16 V (V_r) y la corriente con el amperímetro en serie con RL. Se esperan ≥ 1,5 A (1,6 A con 10 Ω).
3. Calcule %Reg = (|V_ro| − |V_r|)/|V_r| × 100. Se espera ≤ 0,5 % (simulación: 0,09 %).
4. Quite RL y verifique que la salida vuelve a V_ro.
5. Repita los pasos 1 a 4 con RL en J5 para el riel de −16 V.

## P4. Rizado a plena carga (RL conectada)
1. Con el osciloscopio en acople AC, mida V_pp sobre C1 (J3‑1) con RL en J4. Se espera ≈ 0,6–0,9 V_pp a **120 Hz** (onda completa).
2. Mida V_pp en la salida de +16 V. Se espera < 1 mV_pp.
3. Repita en el riel negativo con RL en J5.

## P5. Regulación de línea (solo si hay variac)
Varíe la red entre 103,5 y 126,5 V con RL conectada. Se espera ΔV < 33 mV. Sin variac, anote la tensión de red durante las mediciones.

## P6. Cortocircuito y foldback
1. Sin RL, conecte el amperímetro (escala de 10 A) **directamente** entre +16 V y GND durante 5 s. Se esperan ≈ 0,8–1,2 A: es la corriente de corto con foldback, **menor** que la nominal.
2. Quite el corto: la salida debe volver sola a 16 V.
3. Repita con RL conectada. Al quitar el corto, la salida debe volver a 16 V **con RL puesta** (comprobación de que el foldback no se queda trabado).
4. Haga lo mismo en −16 V y en +5 V (en +5 V se esperan ≈ 0,14 A y +16 V debe seguir en 16 V).
5. Repita el corto de +16 V durante 60 s y mida la temperatura del disipador superior. Se espera < 85 °C con un disipador de 2 °C/W.

## P7. Límite de sobrecarga (curva V–I)
Con un reóstato de potencia o varias resistencias en paralelo en J4, aumente la corriente desde 1,6 A. Anote V y I hasta que la tensión empiece a caer (se espera ≈ 2,3–2,5 A) y luego hasta el corto. Compare con la Fig. de la curva de foldback del informe.

## P8. Arranque con carga
Con RL ya conectada en J4, apague y encienda la fuente cinco veces. La salida debe subir siempre a 16 V (simulación: sube en < 100 ms también con la red al ±10 %).

## P9. Temperatura en régimen
Con RL en J4 durante 30 min, mida la temperatura del disipador superior, de RSC1 y de RL. Se espera que el disipador quede por debajo de 75 °C. Repita en el riel negativo.

## P10. Conexión a las tarjetas PID
Con la fuente apagada y **sin RL**, conecte J2 al `J_PWR` de una tarjeta, y la segunda tarjeta a la primera. Encienda sin bobinas. Mida los rieles en los pines 4 y 11 de cada TL074, y +5 V en R13 de cada PID.
