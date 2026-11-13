# Guía de depuración de un PID del levitador

Procedimientos y diagnósticos que resolvieron fallos reales del montaje (noviembre de 2026). Valores de referencia: ±16 V para los operacionales, ~9 V para la bobina, `R_sense` = 0,33 Ω. Todas las medidas son respecto a tierra con la placa encendida, salvo que se indique.

## Orden de encendido
1. Alimentar ±16 V y revisar +16 V en el pin 4 y −16 V en el pin 11 de cada TL074.
2. Con la fuente de la bobina apagada, revisar las etapas en este orden: `V_ref` (U6), `V_off` (U7, ≈ −10 V), error (U1), P, I, D y sumador (U5).
3. Encender la fuente de la bobina con límite de corriente (~1 A) y medir el emisor del TIP122.

## Referencias de un PID sano
- Sumador: `V_PID = −0,1·(V_P + V_I + V_D + V_off)`. Con error cero y `V_off` ≈ −10 V da ≈ +1 V; el pin 6 del IC2 (nodo de suma) debe estar en 0 V.
- Convertidor V-I: salida del U8 (IC2 pin 14) ≈ 1,5–2 V (V_BE del Darlington + caída en `R_sense`); pin 12 ≈ emisor del TIP; `I = V_emisor / 0,33 Ω` (≈0,2–0,25 V para 0,6–0,75 A).

## Síntomas y causas encontradas
| Síntoma | Causa | Cómo comprobarlo |
|---|---|---|
| Las ramas P, I y D no reciben la señal de error | Puente J9/J10 (red del error) sin soldar o mal puesto | Continuidad entre el agujero del pin 7 del IC1 y R2.2, R5.1, R6.1. |
| Salida del U8 pegada a ~13 V, base del TIP en ~0,7 V, 0 V en la bobina | El colector no tiene alimentación: la fuente de 9 V no llega o la bobina está abierta | Voltaje en la bornera +VBOB y resistencia de la bobina (~4 Ω). Sin colector alimentado, el colector se queda en V_base − 0,7 V. |
| Salida del U8 buena, TIP conduce, pero la bobina casi no tiene corriente | Consigna del U8 baja: divisor `R17` + `POT4` + `R16` abierto o mal soldado | Si el nodo tras `R17` mide lo mismo que `V_PID`, no hay camino a tierra por el POT4 (pata 3 sin GND o pot abierto). |
| Sospecha de integrado dañado tras un corto (por ejemplo, entrada − del U8 unida a su salida) | Los TL074 toleran cortos en la salida, pero no es seguro | Revisar continuidad entre pines adyacentes y probar con otro integrado. |
| Integrador saturado en banco sin imán | Con el lazo cerrado y error grande, `C1` se carga (τ ≈ R11·C1 ≈ 1 s) | Descargar `C1` con un puente antes de cada prueba. |

## Pruebas del TIP122 (pinout B-C-E con la cara con letras hacia ti)
Modo diodo, punta roja en el primero y negra en el segundo:
- Base → Emisor ≈ 1,2–1,4 V; Base → Colector ≈ 0,6–0,7 V; Emisor → Colector ≈ 0,5–0,7 V (diodo interno).
- Las inversas y Colector → Emisor deben dar OL.

Prueba funcional: carga de ~10 Ω entre +5 V y el colector, emisor a tierra, 1 kΩ de +5 V a la base. El colector debe bajar a ~1–1,5 V (saturado). Con la base al aire el colector queda en 5 V.

## Polaridad de bobinas e imán
- La polaridad de una bobina no afecta que circule corriente; solo cambia hacia dónde apunta el campo. Para repulsión, la cara del imán hacia las bobinas debe ser del mismo polo que la cara superior de cada bobina: probar una a una con ~0,5 A y, si atrae, invertir sus cables.
- El voltaje del SS495A debe **subir** al acercar el imán para que el lazo sea de realimentación negativa (la consigna aumenta cuando se acerca). Verificarlo acercando la cara del imán al sensor y, si baja, girar el imán. La convención de polo y cara marcada debe confirmarse en la hoja de datos de Honeywell.

## Calibración de `V_ref` por altura (procedimiento actual)
1. Poner la corriente base con `POT4` (≈0,7–0,9 A por bobina) con `V_PID` ≈ 1 V (error cero).
2. Sostener el imán en la altura deseada con un separador.
3. Medir el voltaje del sensor y ajustar `V_ref` hasta igualarlo (salida de U1 ≈ 0 V). Repetir en los 4 PID.
Con la ganancia de U1 en 1 y los sensores casi sin variación, este método es lento y poco sensible: ver [`plan_2027.md`](plan_2027.md).
