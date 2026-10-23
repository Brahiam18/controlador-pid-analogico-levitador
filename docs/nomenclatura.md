# Nomenclatura de componentes

Esta es la nomenclatura **vigente**: la que usan las ecuaciones del informe, los esquemáticos de Proteus, el esquemático a mano y la Tabla III (valores finales). Los valores corresponden al diseño final ajustado durante las pruebas.

## Nomenclatura vigente

| Etapa | Ref. | Función | Valor final |
|---|---|---|---:|
| **Diferenciador (U1)** | R1 | Entrada de `V_sensor` (rama inversora) | 10 kΩ |
| | R2 | Realimentación del diferenciador | 10 kΩ |
| | R3 | Entrada de `V_ref` (rama no inversora) | 10 kΩ |
| | R4 | Rama no inversora a GND | 10 kΩ |
| **Proporcional (U2)** | R5 | Resistencia de entrada | 10 kΩ |
| | Pot1 | Potenciómetro de realimentación (ajusta `Kp`) | 22 kΩ |
| **Integral (U3)** | Pot2 | Potenciómetro de entrada (ajusta `Ki`) | 220 kΩ |
| | Ci (C1) | Capacitor de integración | 1 µF |
| | R11 | Resistencia de fuga (anti-windup) en paralelo con Ci | 1 MΩ |
| **Derivativo (U4)** | C2 | Capacitor de entrada | 1 µF |
| | R6 | En serie con C2; limita la ganancia en alta frecuencia | 1 kΩ |
| | Pot3 | Potenciómetro de realimentación (ajusta `Kd`) | 22 kΩ |
| **Sumador (U5)** | R7 | Entrada desde `V_P` | 10 kΩ |
| | R8 | Entrada desde `V_I` | 10 kΩ |
| | R9 | Entrada desde `V_D` | 10 kΩ |
| | R_offset | Entrada desde `V_off` | 10 kΩ |
| | R10 | Realimentación del sumador (ganancia 0.1 por rama) | 1 kΩ |
| | R_bias | Compensación de corriente de polarización (entrada no inversora a GND) | 4.4 kΩ ⚠️ (ver errata 5) |
| **Referencia V_ref (U6)** | R12 | Divisor, resistencia a GND | 160 kΩ |
| | R13 | Divisor, resistencia a +5 V | 240 kΩ |
| **Offset V_off (U7)** | R14 | Divisor, resistencia superior | 96 kΩ (calculada; falta medir) |
| | R15 | Divisor, resistencia a GND | 160 kΩ |

## Etapa de potencia (U8)

Nombres usados en el esquemático de Proteus de la etapa de potencia y en la PCB (ver [`../hardware/pcb/README.md`](../hardware/pcb/README.md)). No aparecen en el informe.

| Ref. | Función | Valor |
|---|---|---:|
| U8 | Convertidor tensión‑corriente (comparador de corriente) | LM741 (sim.) / TL074CN (PCB) |
| R16 | Entre la señal de entrada y la entrada + de U8 | 270 Ω |
| RBASE | Entre la salida de U8 y la base del TIP122 | 270 Ω |
| Q1 (POTENCIA) | Transistor de potencia | TIP122 |
| R_sense (R10W en Proteus) | Sensado de corriente en el emisor | 0.33 Ω (3 × 1 Ω / 5 W en paralelo) |
| D1 (PROTECCION) | Diodo en paralelo con la bobina | 1N5408 |
| R17, Pot4 | Divisor de calibración de la corriente (solo PCB) | 10 kΩ, 10 kΩ |
| D2, R18, C3 | Diodo en serie con la base, resistencia en la entrada − y capacitor opcional (solo PCB) | 1N4148, 1 kΩ, 10 nF |

## Equivalencias con la primera versión del informe

Cambios de nombre aplicados a las ecuaciones, al desarrollo del sumador y a la sección de ajustes. Renombrar no altera los valores; la última columna recuerda los ajustes teórico → final que ya figuraban en la Tabla III de la versión anterior, para que el elemento sea fácil de rastrear.

| Elemento | Nombre anterior | Nombre vigente | Ajuste teórico → final |
|---|---|---|---|
| Realimentación del diferenciador | `R_f1` | `R2` | — |
| Potenciómetro de ganancia P | `R_P1` | `Pot1` | 33 kΩ → 22 kΩ (`Kp` 3 → 2.2) |
| Potenciómetro de entrada del integrador | `R_i` | `Pot2` | 12.5 kΩ → 220 kΩ (`Ki` rediseñado) |
| Resistencia de fuga del integrador | `R6` | `R11` | 800 kΩ (Ec. 23) / 1 MΩ (Tabla III) |
| Resistencia en serie del derivador | `R7` | `R6` | — (1 kΩ) |
| Potenciómetro de ganancia D | `R_P3` | `Pot3` | — (22 kΩ) |
| Entrada de `V_P` al sumador | `R8` | `R7` | — |
| Entrada de `V_I` al sumador | `R9` | `R8` | — |
| Entrada de `V_D` al sumador | `R10` | `R9` | — |
| Entrada de `V_off` al sumador | `R11` | `R_offset` | — |
| Realimentación del sumador | `R12` | `R10` | 10 kΩ → 1 kΩ (ganancia 1 → 0.1) |
| Compensación de bias | `R8 ‖ R9 ‖ R10` = 3.3 kΩ | `R8 ‖ R9 ‖ R7` = 3.3 kΩ; luego `R8 ‖ R9 ‖ R7 ‖ R_offset` | → 4.4 kΩ (ver errata 5) |
| Divisores de `V_ref` y `V_off` | `R12`–`R15` | sin cambio de nombre | — |

## Otros cambios entre versiones del informe

- El desarrollo del **ajuste del rango de salida (1 V a 3 V)** pasó de la Sección III a la **IV-A** (saturación del sumador), ahora con la ecuación del sumador modificada y la nueva `R_bias`.
- Los **divisores de `V_ref` y `V_off`** pasaron a ser la subsección **III-F**.
- Se agregó el apartado sobre el **efecto de carga en los divisores** (IV-C) y su resumen en las conclusiones.
- Se agregaron al informe las figuras de Proteus por etapa, el esquemático a mano y el diagrama de bloques (Sección V-A).
- Los anexos pasaron de ser marcadores de posición a incluir las imágenes de los cálculos a mano (Figs. 10–22).

Las inconsistencias que quedaron entre esta nomenclatura y algunas partes del texto del informe están listadas en [`errata-y-pendientes.md`](errata-y-pendientes.md).
