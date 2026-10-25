# Plan de pruebas de la fuente ±16 V / +5 V

Los valores "esperados" salen del cálculo (`calculos/`) y de la simulación (`simulacion/`). Llene la columna "Medido" y calcule el error. La tabla vacía está también en `mediciones.csv`.

**Instrumentos:** multímetro digital (V DC, V AC, A DC hasta 10 A), osciloscopio de 2 canales con punta ×1/×10, termómetro o termopar del multímetro y un reloj.

**Cargas de prueba** (resistencias de potencia):

| Carga | Valor | Corriente | Potencia |
|---|---|---|---|
| +16 V a plena carga | 82 Ω / 5 W | 195 mA | 3,1 W |
| −16 V a plena carga | 82 Ω / 5 W | 195 mA | 3,1 W |
| +5 V a plena carga | 120 Ω / 1/2 W | 42 mA | 0,21 W |
| media carga de ±16 V | 160 Ω / 2 W | 100 mA | 1,6 W |

## P0. Inspección sin energía
1. Revisar la polaridad de C1, C2, C7–C9, C11, C13, C15 y C16, de los diodos y de los LED.
2. Medir continuidad (no debe haber corto) entre: `+16V`–`GND`, `-16V`–`GND`, `+5V`–`GND`, `V_RAW+`–`GND`, `V_RAW-`–`GND` y `+16V`–`-16V`.
3. Medir aislamiento aleta–disipador en Q1, U1, Q3 y U2 (debe ser circuito abierto).
4. Dejar RV1 y RV2 a mitad de recorrido y RV3 a mitad.

## P1. Primer encendido sin carga
1. Sin conectar las tarjetas PID, encender con F1 y F2 puestos.
2. Medir V AC entre J1‑1 y J1‑2 (esperado 18–20 V rms) y la red (esperado ≈ 115–120 V rms).
3. Medir V DC en J3: V_RAW+ y V_RAW− (esperado ±25 a ±28 V sin carga).
4. Verificar que los tres LED encienden.

## P2. Ajuste de las salidas
1. Con RV1, llevar +16 V a **16,00 V**. Con RV2, llevar −16 V a **−16,00 V**. Con RV3, llevar +5 V a **5,00 V**.
2. Anotar el rango de cada trimmer (giro completo). Esperado: +14,9 a +17,0 V, −14,9 a −17,0 V y +4,70 a +5,23 V.

## P3. Regulación de carga
1. Medir cada salida sin carga (V_ro) y con plena carga (V_r).
2. Calcular %Reg = (|V_ro| − |V_r|)/|V_r| × 100 (ec. de la monografía). Esperado ≤ 0,5 % (≈ 0,1 % típico).

## P4. Rizado
1. Osciloscopio en acople AC: medir V_pp sobre C1 (J3‑1) y sobre C2 (J3‑3) a plena carga. Esperado ≈ 1,3–1,5 V_pp en +, 1,0–1,2 V_pp en −, con frecuencia de **60 Hz** (media onda).
2. Medir V_pp en las salidas (escala de 1–2 mV/div, punta ×1). Esperado < 1 mV_pp. Si se ve más, revisar el lazo de la punta de masa.
3. Calcular el factor de rizado F_r = V_r,rms/V_DC de la salida del filtro.

## P5. Regulación de línea (si hay variac)
Variar la red de 103,5 V a 126,5 V (±10 %) y anotar cada salida. Esperado ΔV < 33 mV en ±16 V. Sin variac: anotar la tensión de red durante las pruebas y repetir P3 en otra hora del día.

## P6. Protección contra cortocircuito
1. Con la salida a probar sin carga, conectar el amperímetro (escala de 10 A) **directamente** entre la salida y GND durante 5 s. Anotar la corriente y si el LED se apaga.
2. Esperado: +16 V ≈ 0,39 A; −16 V ≈ 0,32 A; +5 V ≈ 0,14 A (y +16 V sigue en ≈ 16 V durante el corto de +5 V).
3. Quitar el corto y verificar que la salida vuelve sola a su valor.
4. Repetir el corto de +16 V durante 60 s y medir la temperatura del disipador superior. Esperado < 80 °C con disipador de 5 °C/W.

## P7. Temperatura en régimen
Con las tres cargas de plena carga durante 30 min, medir la temperatura de los dos disipadores, de R9, de R3 y R4. Esperado: disipadores < 60 °C, R9 tibia.

## P8. Conexión a las tarjetas PID
1. Con la fuente apagada, conectar J2 a `J_PWR` de una tarjeta, y la segunda tarjeta a la primera.
2. Encender **sin bobinas** y medir los rieles en los pines 4 y 11 de cada TL074CN y +5 V en R13 de cada PID.
3. Medir la corriente de cada riel con el amperímetro en serie (esperado: menos de 50 mA por PID).
