# Lista de materiales

Componentes del controlador PID analógico, con la nomenclatura vigente ([`../docs/nomenclatura.md`](../docs/nomenclatura.md)). El valor teórico es el de la primera propuesta de diseño; el valor final es el ajustado durante las pruebas. La misma tabla está en [`lista_de_materiales.csv`](lista_de_materiales.csv).

| Ref. | Descripción | Teórico | Final | Cant. | Etapa | Nota |
|---|---|---|---|:-:|---|---|
| U1 | LM741 | — | — | 1 | Diferenciador de error | — |
| U2 | LM741 | — | — | 1 | Proporcional | — |
| U3 | LM741 | — | — | 1 | Integral | — |
| U4 | LM741 | — | — | 1 | Derivativo | — |
| U5 | LM741 | — | — | 1 | Sumador | — |
| U6 | LM741 | — | — | 1 | Buffer de Vref | Seguidor de voltaje |
| U7 | LM741 | — | — | 1 | Buffer de Voff | Seguidor de voltaje |
| R1 | Resistencia | 10 kΩ | 10 kΩ | 1 | Diferenciador de error | Entrada de V_sensor |
| R2 | Resistencia | 10 kΩ | 10 kΩ | 1 | Diferenciador de error | Realimentación |
| R3 | Resistencia | 10 kΩ | 10 kΩ | 1 | Diferenciador de error | Entrada de V_ref |
| R4 | Resistencia | 10 kΩ | 10 kΩ | 1 | Diferenciador de error | Rama no inversora a GND |
| R5 | Resistencia | 10 kΩ | 10 kΩ | 1 | Proporcional | Entrada |
| Pot1 | Potenciómetro | 33 kΩ | 22 kΩ | 1 | Proporcional | Ajusta Kp (Kp = 2.2) |
| Pot2 | Potenciómetro | 12.5 kΩ | 220 kΩ | 1 | Integral | Ajusta Ki |
| Ci (C1) | Capacitor | 1 µF | 1 µF | 1 | Integral | Capacitor de integración |
| R11 | Resistencia | 1 MΩ | 1 MΩ | 1 | Integral | Fuga anti-windup en paralelo con Ci (Kmax = 4.5) |
| C2 | Capacitor | 1 µF | 1 µF | 1 | Derivativo | — |
| R6 | Resistencia | 1 kΩ | 1 kΩ | 1 | Derivativo | En serie con C2 (limita ganancia en alta frecuencia) |
| Pot3 | Potenciómetro | 22 kΩ | 22 kΩ | 1 | Derivativo | Ajusta Kd (Kd max = 22) |
| R7 | Resistencia | 10 kΩ | 10 kΩ | 1 | Sumador | Entrada desde V_P |
| R8 | Resistencia | 10 kΩ | 10 kΩ | 1 | Sumador | Entrada desde V_I |
| R9 | Resistencia | 10 kΩ | 10 kΩ | 1 | Sumador | Entrada desde V_D |
| R_offset | Resistencia | 10 kΩ | 10 kΩ | 1 | Sumador | Entrada desde V_off |
| R10 | Resistencia | 10 kΩ | 1 kΩ | 1 | Sumador | Realimentación (ganancia 0.1 por rama) |
| R_bias | Resistencia | 3.3 kΩ | 4.4 kΩ | 1 | Sumador | Valor de la Ec. (51) del informe; ver errata 5 |
| R12 | Resistencia | 160 kΩ | 160 kΩ | 1 | Divisor Vref | A GND |
| R13 | Resistencia | 240 kΩ | 240 kΩ | 1 | Divisor Vref | A +5 V |
| R14 | Resistencia | 96 kΩ | falta medir | 1 | Divisor Voff | Valor calculado |
| R15 | Resistencia | 160 kΩ | 160 kΩ | 1 | Divisor Voff | A GND |

**Total:** 7 amplificadores operacionales LM741, 3 potenciómetros, 2 capacitores y 17 resistencias fijas (incluida `R_bias`).

**Alimentación:** fuente dual de ±16 V para los operacionales (según el diseño del informe) y una referencia de +5 V para el divisor de `V_ref`.

> Pendiente: confirmar `R14` y `R_bias` con el montaje físico (ver [errata y pendientes](../docs/errata-y-pendientes.md)).
