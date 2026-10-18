# Placa de 4 controladores PID analógicos

Placa de **una sola cara** para fabricar en baquela (transferencia de tóner o fotosensible) con **cuatro controladores PID independientes**, cada uno idéntico al circuito del informe (2 × TL074CN por módulo, 8 en total). Los cuatro módulos comparten los rieles de alimentación; cada uno tiene su propia entrada de sensor (`VSEN`) y su propia salida de control (`VPID`).

![Vista de ensamble](img/ensamble.png)

| Dato | Valor |
|---|---|
| Tamaño de la placa | **170.2 × 127.0 mm** (cabe en una baquela de 15 × 20 cm) |
| Capas | 1 (cobre inferior) + puentes de alambre en el lado de componentes |
| Pistas / pads / taladro | 0.7 mm / 2.0 mm / 0.9 mm |
| Separación mínima entre redes | 0.45 mm (medida sobre la geometría final) |
| Puentes de alambre | 40 en total (9 por módulo más 4 que unen los rieles entre módulos); los más largos miden unos 48 mm (rieles de `+5V` y `-16V`); ver [`puentes.md`](puentes.md) |

## Archivos

| Archivo | Para qué sirve |
|---|---|
| [`pid4_levitador.sch`](pid4_levitador.sch) y [`pid4_levitador.brd`](pid4_levitador.brd) | Esquemático (una hoja por módulo) y placa en formato EAGLE; Fusion los abre en Electronics |
| [`cobre_espejado_1a1.pdf`](cobre_espejado_1a1.pdf) | **Cobre espejado a escala 1:1** para imprimir y quemar la placa |
| [`ensamble_1a1.pdf`](ensamble_1a1.pdf) | Vista del lado de componentes: ubicación de cada pieza y puentes en rojo (J1 a J40) |
| [`puentes.md`](puentes.md) | Lista de los 40 puentes con red, longitud y extremos |
| [`generador/`](generador/) | Código en Python que genera todo lo anterior a partir de un módulo ruteado (`modulo_ruteado.json`) |

## Cómo usarlos

**Abrir en Fusion.** En Fusion, abrir `pid4_levitador.sch` y `pid4_levitador.brd` desde "Abrir → Abrir desde mi computadora" (se importan a un diseño de Electronics). Las piezas están en una biblioteca propia llamada `pid4`.

**Imprimir y quemar.** Imprimir `cobre_espejado_1a1.pdf` **sin escalar** ("tamaño real", sin "ajustar a página"). La regla de 50 mm al pie de la hoja sirve para comprobar la escala. La hoja ya está espejada: el tóner va contra el cobre. El punto blanco en el centro de cada pad marca dónde taladrar (0.9 mm).

**Soldar.** Soldar primero los puentes de alambre aislado en el lado de componentes (ver [`puentes.md`](puentes.md)), después las resistencias, los zócalos y al final potenciómetros y capacitores.

## Conexiones de cada módulo

| Regleta | Pines | Función |
|---|---|---|
| `J_PWR` (borde superior) | 1 · 2 · 3 · 4 | `+16V` · `-16V` · `GND` · `+5V` |
| `J_IN` (borde izquierdo) | 1 | `VSEN`, señal del sensor de posición |
| `J_OUT` (borde derecho) | 1 | `VPID`, salida del controlador (1 V a 3 V) |

Los rieles `+16V`, `-16V`, `GND` y `+5V` están unidos en toda la placa: basta alimentar una sola regleta `J_PWR`. La masa de las señales `VSEN` y `VPID` es el mismo `GND`. `+5V` solo alimenta el divisor de `V_ref` (`R13`).

## Componentes (por módulo y para toda la placa)

| Componente | Por módulo | Placa completa | Notas |
|---|:-:|:-:|---|
| TL074CN (DIP14) | 2 | 8 | Usar zócalos DIP14. Pin 1 arriba a la izquierda en todos los CI |
| 10 kΩ | 9 | 36 | R1, R2, R3, R4, R5, R7, R8, R9, R_offset |
| 1 kΩ | 2 | 8 | R6, R10 |
| 1 MΩ | 1 | 4 | R11 |
| 160 kΩ | 2 | 8 | R12, R15 |
| 240 kΩ | 1 | 4 | R13 |
| 96 kΩ | 1 | 4 | R14 (valor calculado; no es de serie, ver más abajo) |
| 4.4 kΩ | 1 | 4 | R_bias (valor de tu montaje; no es de serie, ver más abajo) |
| Potenciómetro 22 kΩ | 2 | 8 | Pot1 (Kp) y Pot3 (Kd) |
| Potenciómetro 220 kΩ | 1 | 4 | Pot2 (Ki) |
| Capacitor 1 µF | 2 | 8 | C1 (integrador) y C2 (derivador) |
| Regletas de pines | 6 pines | 24 pines | 1 × 4 (`J_PWR`) y 2 × 1 (`J_IN`, `J_OUT`) |

Resistencias axiales de 1/4 W a 7.62 mm, capacitores a 5.08 mm y potenciómetros de 3 pines a 5.08 mm (pin 1 = extremo, pin 2 = cursor, pin 3 = otro extremo).

### Reparto de las etapas en los TL074CN

El TL074CN trae 4 amplificadores en un solo DIP‑14, así que las 7 etapas del informe (U1 a U7) caben en 2 integrados por controlador. Cada integrado se llama `IC1` o `IC2` en la placa (con el prefijo del módulo, por ejemplo `P1_IC1`) y en la serigrafía cada canal lleva escrita su etapa.

| Etapa del informe | Integrado | Canal | Salida (pin) | Entrada − (pin) | Entrada + (pin) |
|---|:-:|:-:|:-:|:-:|:-:|
| U6 · buffer de `V_ref` | IC1 | 1 | 1 | 2 | 3 |
| U1 · diferenciador de error | IC1 | 2 | 7 | 6 | 5 |
| U2 · proporcional | IC1 | 3 | 8 | 9 | 10 |
| U3 · integral | IC1 | 4 | 14 | 13 | 12 |
| U4 · derivativo | IC2 | 1 | 1 | 2 | 3 |
| U5 · sumador | IC2 | 2 | 7 | 6 | 5 |
| U7 · buffer de `V_off` | IC2 | 3 | 8 | 9 | 10 |
| (libre) | IC2 | 4 | 14 | 13 | 12 |

Alimentación de cada TL074CN: `+16V` en el pin 4 y `-16V` en el pin 11 (en el LM741 eran el 7 y el 4). El canal libre (IC2, pines 12 a 14) queda como seguidor: entrada `+` a masa y entrada `−` unida a la salida, para que no oscile ni se sature. Los valores de resistencias y capacitores son los mismos del informe.

## Cosas a tener en cuenta

- **Capacitores sin polaridad.** `C1` y `C2` trabajan con señales de ambos signos, por lo que conviene usar poliéster (MKT) o cerámicos de 1 µF. Con un electrolítico, la polaridad queda invertida en una parte del ciclo.
- **`R_bias` y `R14` no son valores comerciales.** Para `R_bias` sirven 4.7 kΩ o 4.3 kΩ (la corriente de polarización es muy pequeña). Para `R14`, tomar 100 kΩ o 91 kΩ más 4.7 kΩ en serie y ajustar mirando `V_off`: en la protoboard se midieron −10.21 V frente a −10.1 V calculados. El informe sigue con `R14` como "falta medir" y con la errata 5 de `R_bias` sin resolver.
- **TL074CN en lugar de LM741.** La placa está hecha para el TL074CN. El informe, la lista de materiales general y las mediciones de la Tabla I todavía nombran al LM741; con TL074CN (entradas JFET, salida de unos ±13 V con ±16 V) los offsets y los valores prácticos pueden cambiar un poco.
- **Diferenciador (U1).** La placa sigue el esquemático de Proteus y las mediciones del montaje: `R1` recibe `V_ref` (entrada inversora) y `R3` recibe `V_sensor` (entrada no inversora), así que `V_e = V_sensor − V_ref`. La tabla de nomenclatura del informe dice lo contrario para `R1` y `R3`; conviene corregirla.
- **Puentes.** Son 40 en total; los más largos (los de `+5V` y `-16V`) miden unos 48 mm de alambre y varios pasan sobre otros componentes, por eso deben ser de alambre aislado.
- **Sin decoupling.** El diseño del informe no incluye capacitores de desacople; si hay ruido, se pueden soldar 100 nF entre cada alimentación del TL074CN (pines 4 y 11) y masa por el lado de soldadura.

## Qué se verificó y qué no

Verificado con scripts incluidos en [`generador/`](generador/) (`verify.py` y `xmlcheck.py`):
- Las 80 redes de la placa están completas (ningún pad queda sin conectar a su red) y no hay cortos entre redes.
- La separación mínima entre cobre de redes distintas es de 0.45 mm.
- Los puentes no tocan pads ajenos ni se cruzan entre sí.
- El esquemático y la placa tienen las mismas piezas y las mismas conexiones.

**No** verificado: la placa no se ha fabricado ni probado. La primera versión (con LM741) sí se importó en Fusion sin errores; esta versión con TL074CN usa el mismo exportador pero con un símbolo de cuatro compuertas por integrado, y aún no se ha reabierto en Fusion. Los archivos `.sch` y `.brd` se escribieron a mano en el formato XML de EAGLE; si Fusion muestra algún aviso al importarlos, conviene revisarlo antes de quemar. Se recomienda probar un solo módulo antes de montar los cuatro.

## Regenerar

```bash
cd generador
pip install numpy matplotlib shapely
python3 build.py modulo_ruteado.json salida
```

Genera en `salida/` los archivos `.sch`, `.brd`, los dos PDF y la lista de puentes.
