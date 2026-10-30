# Lista de materiales: fuente ±16 V / 1,5 A y +5 V (versión 2)

Valores comerciales comunes en tiendas de electrónica de Colombia. Las referencias coinciden con el esquemático, la placa y el informe. LM317, LM337 y los condensadores de 15000 µF y 6800 µF ya están disponibles; el transformador hay que comprarlo. No se ponen precios porque cambian.

| Ref | Componente | Valor | Especificación / encapsulado | Cantidad | Función | Sustituto aceptable | Notas |
|---|---|---|---|---|---|---|---|
| T1 | Transformador | 18-0-18 V / 3 A | 115 V primario; 108 VA | 1 | Reducción de tensión | 18-0-18 V / 5 A | Comprar. Los extremos van a J1-1 y J1-3 y la toma central a J1-2 |
| F1 | Fusible lento + portafusible de chasis | T1 A | 5x20 mm 250 V | 1 | Protección del primario | — | Fuera de la placa |
| S1 | Interruptor | — | 250 VAC 3 A (balancín) | 1 | Encendido | — | Fuera de la placa |
| — | Cable de poder con clavija | — | 2 x 18 AWG | 1 | Entrada 115 VAC | — | Aislar con termoencogible los empalmes del primario |
| J1 | Bornera de tornillo | 3 vías | paso 5.08 mm | 1 | Secundario: A / toma central / B | 2 borneras de 2 vías |  |
| F2 F3 | Portafusible de PCB + fusible lento | T3.15 A | 5x20 mm | 2 | Protección de cada mitad del secundario | T3 A | Distancia entre clips 22.86 mm |
| D1-D4 | Diodo rectificador | 1N5408 | 3 A 1000 V DO-201 | 4 | Puente rectificador | Puente KBU/GBU de 4 A (otra huella) |  |
| D7 D10 | Diodo rectificador | 1N5408 | 3 A DO-201 | 2 | Polaridad inversa en las salidas de ±16 V |  |  |
| D5 D8 D11 D13 | Diodo | 1N4007 | 1 A DO-41 | 4 | Protección OUT-IN de los reguladores y salida de +5 V | 1N4004 |  |
| D6 D9 D12 | Diodo de señal | 1N4148 | DO-35 | 3 | Protección del pin ADJ | 1N914 |  |
| C1 | Electrolítico | 15000 µF | 50 V radial D35 mm paso 10 mm | 1 | Filtro + | — | Ya disponible |
| C2A C2B | Electrolítico | 6800 µF | 50 V radial D28 mm paso 10 mm | 2 | Filtro − (en paralelo: 13600 µF) | — | Ya disponibles |
| C3 C4 C5 C8 C10 C13 C16 C19 | Cerámico multicapa | 100 nF | 50 V (C3 y C4 de 100 V) paso 5.08 mm | 8 | Desacople | poliéster 100 nF |  |
| C6 C11 C17 | Electrolítico | 10 µF | 25 V radial D5 mm | 3 | Pin ADJ (rechazo de rizado) | 10 µF/35 V |  |
| C7 C12 C18 | Tántalo | 10 µF | 25 V gota paso 2.54 mm | 3 | Estabilidad de la salida | electrolítico 47 µF/25 V | Respetar la polaridad |
| C9 C14 | Electrolítico | 220 µF | 25 V radial D8 mm | 2 | Respuesta a escalones de 1,5 A | 220 µF/35 V |  |
| C15 | Electrolítico | 100 µF | 25 V radial D6.3 mm | 1 | Filtro RC de la rama de +5 V | 100 µF/35 V |  |
| RSC1 RSC2 | Resistencia de potencia | 0.27 Ω | 5 W cemento | 2 | Sensado del limitador con foldback | 2 x 0.56 Ω 2 W en paralelo |  |
| R3 R11 | Resistencia | 2.7 kΩ | 1 W | 2 | Polarización del Darlington |  |  |
| R4 R12 | Resistencia | 1 kΩ | 1/4 W | 2 | Base-emisor del transistor de paso |  |  |
| R5 R13 | Resistencia | 270 Ω | 1/4 W 1 % | 2 | Divisor de foldback (k') |  |  |
| R6 R14 | Resistencia | 12 kΩ | 1/4 W 1 % | 2 | Divisor de foldback (k') |  |  |
| R7 R15 | Resistencia | 2.7 Ω | 1 W | 2 | Ampliación de corriente (ec. 3.24) |  |  |
| R8 R16 R20 | Resistencia película metálica | 120 Ω | 1/4 W 1 % | 3 | Red de ajuste (R1 de la monografía) |  |  |
| R9 R17 | Resistencia película metálica | 1.3 kΩ | 1/4 W 1 % | 2 | Red de ajuste de ±16 V | 1.2 kΩ + 100 Ω en serie |  |
| R21 | Resistencia película metálica | 330 Ω | 1/4 W 1 % | 1 | Red de ajuste de +5 V |  |  |
| R19 | Resistencia de potencia | 100 Ω | 3 W | 1 | Limitación y filtro de la rama de +5 V | 100 Ω 5 W |  |
| R10 R18 | Resistencia | 2.2 kΩ | 1/4 W | 2 | LED de ±16 V |  |  |
| R22 | Resistencia | 470 Ω | 1/4 W | 1 | LED de +5 V |  |  |
| RV1 RV2 | Trimmer multivuelta | 200 Ω | 3296W | 2 | Ajuste de ±16 V |  |  |
| RV3 | Trimmer multivuelta | 50 Ω | 3296W | 1 | Ajuste de +5 V | 100 Ω 3296W |  |
| Q1 Q4 | Transistor de potencia PNP | TIP42C | TO-220 6 A 65 W | 2 | Paso del limitador (Q1) y ampliación de corriente (Q4) | TIP32C / MJE2955T | Con mica y buje |
| Q5 Q8 | Transistor de potencia NPN | TIP41C | TO-220 6 A 65 W | 2 | Paso del limitador (Q5) y ampliación de corriente (Q8) | TIP31C / MJE3055T | Con mica y buje |
| Q2 | Transistor PNP mediana potencia | BD140 | TO-126 | 1 | Driver del Darlington +16 V | BD136 / BD138 | Al disipador con mica |
| Q6 | Transistor NPN mediana potencia | BD139 | TO-126 | 1 | Driver del Darlington −16 V | BD135 / BD137 | Al disipador con mica |
| Q3 | Transistor PNP de señal | BC557 | TO-92 | 1 | Sensor de corriente +16 V | 2N3906 (girar: E-B-C) |  |
| Q7 | Transistor NPN de señal | BC547 | TO-92 | 1 | Sensor de corriente −16 V | 2N3904 (girar: E-B-C) |  |
| U1 U3 | Regulador ajustable positivo | LM317T | TO-220 | 2 | +16 V y +5 V |  | Ya disponibles; U1 con mica |
| U2 | Regulador ajustable negativo | LM337T | TO-220 | 1 | −16 V |  | Ya disponible; con mica |
| LED1-LED3 | LED | verde | 5 mm | 3 | Indicadores |  |  |
| J2 | Bornera de tornillo | 4 vías (2 x 2) | paso 5.08 mm | 1 | Salida: +16 / −16 / GND / +5 |  | Mismo orden que J_PWR de las tarjetas PID |
| J4 J5 | Bornera de tornillo | 2 vías | paso 5.08 mm | 2 | Conexión removible de la carga de prueba RL |  |  |
| J3 | Regleta macho | 1x3 | 2.54 mm | 1 | Puntos de prueba V_RAW+ / GND / V_RAW− |  |  |
| RL | Resistencia de cemento para la carga de prueba (externa) | 10 Ω | 10 W; 4 unidades en serie-paralelo (2 ramas de 2 en serie) = 10 Ω, 6.4 W cada una | 4 | Comprobar 1.6 A en cada riel | 4 x 39 Ω 10 W en paralelo (9.75 Ω) o una de 10 Ω ≥ 30 W de aluminio | Se conecta en J4 o J5 solo para la prueba; se calienta (separarlas y no tocarlas) |
| — | Disipador de aluminio aletado | ≤ 2 °C/W | para 3 TO-220 + 1 TO-126 | 2 | Uno por riel (borde superior e inferior) |  | P. ej. perfil de 100 x 60 x 30 mm |
| — | Kit de aislamiento | mica + buje + tornillo M3 | TO-220 / TO-126 | 8 | Aislar cada pieza del disipador | lámina de silicona | Comprobar aleta-disipador abierto |
| — | Grasa térmica | — | — | 1 |  |  |  |
| — | Baquela una cara | 20 x 15 cm | FR-4 o fibra | 1 | Placa de 190.5 x 139.7 mm |  |  |
| — | Separadores M3 | 10 mm | — | 4 | Agujeros de montaje |  |  |
| — | Alambre aislado | 22 AWG | — | 1 m | Puentes del lado de componentes |  |  |

**Pines:** BD139/BD140 (TO‑126): E‑C‑B con las letras al frente. BC547/BC557: C‑B‑E con la cara plana al frente; los 2N3904/2N3906 son E‑B‑C y van girados 180°.
