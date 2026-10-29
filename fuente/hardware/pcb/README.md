# Placa de la fuente ±16 V / 1,5 A y +5 V (versión 2)

Placa de **una sola cara** (cobre inferior) de **190,5 × 139,7 mm**, que cabe en una baquela de 20 × 15 cm. Se fabrica por transferencia de tóner o con película fotosensible. Lleva **7 puentes de alambre** (P1–P7) del lado de componentes, todos en redes de señal o de baja corriente.

![Ensamble](img/ensamble.png)

| Archivo | Para qué sirve |
|---|---|
| `fuente.sch` y `fuente.brd` | Esquemático y placa en formato EAGLE. En Fusion: *Cargar* los dos archivos juntos con "Crear diseño de la electrónica" marcado. Las piezas están en la biblioteca propia `fuente16`. El esquemático conecta por **etiquetas de red**; el dibujo legible está en `../../esquematicos/` |
| `cobre_espejado_1a1.pdf` | Cara de cobre **espejada** a escala 1:1, para planchar o insolar |
| `ensamble_1a1.pdf` | Página 1: lado de componentes a 1:1 (referencias, pin 1, puentes en rojo). Página 2: vista ampliada con referencia y valor |
| `puentes.md` | Lista de los 7 puentes con red, longitud y extremos |
| `generador/` | Código en Python que hace la colocación, el ruteo, la verificación y la exportación (`python3 buscar.py 1,2,3,4 placa.json` y luego `python3 build.py placa.json ..`) |

## Reglas de diseño (verificadas por `verify.py` y `xmlcheck.py`)
- Pistas de 0,8 mm. Las redes de corriente alta (secundario `ACA`/`ACB`/`AC1`/`AC2`, `VRAWP`, `VRAWN`, `E1`, `E2`, `VA1`, `VA2`, `+16V`, `-16V`, `GND`) van en 1,6 mm.
- Pads de 2,0 mm, y de 2,6 mm en borneras, portafusibles, 1N5408, R_SC (5 W) y condensadores grandes.
- Taladros de 0,9 a 1,3 mm según la pieza (C1 de 15 000 µF: Ø ≤ 35 mm, 10 mm entre patas; C2A/C2B de 6800 µF: Ø 28 mm, 10 mm entre patas) y 3,2 mm para los 4 agujeros de montaje.
- Separación mínima entre cobres de redes distintas: **0,40 mm**, medida sobre la geometría final.
- Las 32 redes están completas, sin cortos, y el `.sch` y el `.brd` son consistentes.

## Fabricación
1. Imprimir `cobre_espejado_1a1.pdf` **sin escalar** ("tamaño real"). La regla de abajo debe medir 50 mm.
2. Transferir, atacar con cloruro férrico y taladrar. El punto blanco de cada pad marca el centro.
3. Estañar las pistas anchas (secundario, V_RAW, ±16 V y GND) para que soporten mejor los 1,6 A.
4. Revisar con el multímetro, antes de soldar, que no haya cortos: `+16V`–`GND`, `-16V`–`GND`, `+5V`–`GND`, `VRAWP`–`GND`, `VRAWN`–`GND` y `+16V`–`-16V`.
5. Soldar en este orden: primero los puentes (alambre aislado, calibre 22 AWG o más grueso), luego resistencias y diodos, después TO‑92, trimmers, condensadores pequeños, LED, borneras, portafusibles, C1, C2A y C2B, y al final los TO‑220/TO‑126 ya atornillados a su disipador.

## Disipadores (importante)
- **Q1 (TIP42C), Q2 (BD140), Q4 (TIP42C) y U1 (LM317T)** van en el borde superior; **Q5 (TIP41C), Q6 (BD139), Q8 (TIP41C) y U2 (LM337T)** en el inferior. Cada grupo comparte un disipador de **≤ 2 °C/W** (por ejemplo un perfil aletado de unos 100 × 60 × 30 mm) que sobresale del borde de la placa.
- La aleta de cada pieza está conectada eléctricamente a uno de sus pines. Por eso **cada pieza lleva mica (o silicona) y buje aislante**. Después de montarlas, comprobar con el óhmetro que entre cada aleta y el disipador haya circuito abierto.
- **U3** (+5 V) disipa unos 0,3 W y no necesita disipador.

## Guía de conexión

| Desde | Hacia | Nota |
|---|---|---|
| Red 115 V (L) | Fusible F1 T1 A → interruptor S1 → primario del transformador | Fuera de la placa, con los empalmes aislados |
| Red 115 V (N) | Otro extremo del primario | |
| Secundario 18‑0‑18 V: extremo A, toma central, extremo B | **J1‑1**, **J1‑2 (GND)**, **J1‑3** | F2 y F3 (T3,15 A) están en la placa |
| J2‑1 +16 V, J2‑2 −16 V, J2‑3 GND, J2‑4 +5 V | `J_PWR` pines 1, 2, 3 y 4 de **una** tarjeta PID; la otra tarjeta se une a la primera por su `J_PWR` | Mismo orden de pines en los dos lados |
| **J4‑1 (+16 V), J4‑2 (GND)** | Carga de prueba `R_L` = 10 Ω ≥ 30 W | **Removible**: solo durante la prueba de 1,5 A |
| **J5‑1 (−16 V), J5‑2 (GND)** | Carga de prueba `R_L` | Un riel a la vez |
| J3 (V_RAW+, GND, V_RAW−) | Osciloscopio | Medición del rizado de C1 y C2 |

**Tierras:** la tierra de esta fuente (GND) es solo de señal. La fuente de las bobinas (`VBOB`/`PGND`) va aparte. GND y PGND se unen **en un solo punto**, el puente `JP_GND` soldado en una sola de las cuatro etapas de las tarjetas PID. No unir GND y PGND en ningún otro lugar, tampoco dentro de esta fuente.
