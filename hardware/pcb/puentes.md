# Puentes de alambre

La placa es de **una sola cara** (cobre en el lado de soldadura). Los cruces entre pistas se resuelven con **puentes de alambre aislado** soldados en el lado de componentes, entre los agujeros indicados. En la vista de ensamble ([`ensamble_1a1.pdf`](ensamble_1a1.pdf)) aparecen en rojo con la misma numeración.

- Total: **48 puentes** (40 dentro de los módulos y 8 que unen los rieles entre módulos).
- Longitud aproximada total: **572 mm**; el más largo mide unos 28 mm.
- Usar alambre aislado (cable de *wire-wrap* o alambre esmaltado de 26 a 30 AWG, o patas de resistencias cortadas con tubo termocontráctil). Un puente puede pasar por encima de componentes, pero no debe tocar patas ajenas.
- "Agujero" es un pad sin componente, taladrado a 0.9 mm; las coordenadas son milímetros desde la esquina inferior izquierda de la placa.
- Los puentes con tres extremos (por ejemplo `P1_VE`) se hacen con dos alambres que se encuentran en la pata indicada.
- La longitud es la del trayecto dibujado; en línea recta es algo menor, así que conviene cortar con holgura.

| N.º | Red | Longitud aprox. | Extremos |
|:-:|---|--:|---|
| J1 | `+5V` | 8 mm | P1_J_PWR.4 ↔ agujero (27.9; 134.6) mm, junto a P1_J_PWR.4 |
| J2 | `+5V` | 8 mm | P2_J_PWR.4 ↔ agujero (116.8; 134.6) mm, junto a P2_J_PWR.4 |
| J3 | `-16V` | 5 mm | agujero (22.9; 121.9) mm, junto a P1_U6.1 ↔ P1_J_PWR.2 |
| J4 | `-16V` | 5 mm | agujero (111.8; 121.9) mm, junto a P2_U6.1 ↔ P2_J_PWR.2 |
| J5 | `P1_U2N` | 15 mm | P1_POT1.1 ↔ P1_U2.2 |
| J6 | `P2_U2N` | 15 mm | P2_POT1.1 ↔ P2_U2.2 |
| J7 | `-16V` | 6 mm | P1_U2.4 ↔ agujero (61.0; 113.0) mm, junto a P1_POT1.1 |
| J8 | `-16V` | 6 mm | P2_U2.4 ↔ agujero (149.9; 113.0) mm, junto a P2_POT1.1 |
| J9 | `P1_VOFFD` | 5 mm | P1_R15.1 ↔ P1_R14.2 |
| J10 | `P2_VOFFD` | 5 mm | P2_R15.1 ↔ P2_R14.2 |
| J11 | `+16V` | 15 mm | agujero (61.0; 91.4) mm, junto a P1_U3.8 ↔ P1_U4.7 |
| J12 | `+16V` | 15 mm | agujero (149.9; 91.4) mm, junto a P2_U3.8 ↔ P2_U4.7 |
| J13 | `GND` | 10 mm | agujero (17.8; 96.5) mm, junto a P1_R2.1 ↔ P1_R4.2 |
| J14 | `P1_VD` | 15 mm | P1_POT3.2 ↔ agujero (58.4; 96.5) mm, junto a P1_ROFFSET.2 |
| J15 | `GND` | 10 mm | agujero (106.7; 96.5) mm, junto a P2_R2.1 ↔ P2_R4.2 |
| J16 | `P2_VD` | 15 mm | P2_POT3.2 ↔ agujero (147.3; 96.5) mm, junto a P2_ROFFSET.2 |
| J17 | `P1_VE` | 23 mm | agujero (38.1; 83.8) mm, junto a P1_RBIAS.1 ↔ P1_R6.1 ↔ agujero (48.3; 95.2) mm, junto a P1_ROFFSET.1 |
| J18 | `P2_VE` | 23 mm | agujero (127.0; 83.8) mm, junto a P2_RBIAS.1 ↔ P2_R6.1 ↔ agujero (137.2; 95.2) mm, junto a P2_ROFFSET.1 |
| J19 | `P1_SUMN` | 5 mm | agujero (67.3; 92.7) mm, junto a P1_U5.1 ↔ P1_R8.2 |
| J20 | `P2_SUMN` | 5 mm | agujero (156.2; 92.7) mm, junto a P2_U5.1 ↔ P2_R8.2 |
| J21 | `GND` | 24 mm | agujero (48.3; 62.2) mm, junto a P3_U7.1 ↔ P1_U3.3 |
| J22 | `GND` | 22 mm | agujero (124.5; 82.5) mm, junto a P2_RBIAS.2 ↔ agujero (125.7; 62.2) mm, junto a P4_R14.1 |
| J23 | `-16V` | 28 mm | agujero (58.4; 78.7) mm, junto a P1_U3.5 ↔ agujero (61.0; 63.5) mm, junto a P3_U2.1 ↔ P1_U5.4 |
| J24 | `-16V` | 13 mm | agujero (147.3; 78.7) mm, junto a P2_U3.5 ↔ P2_U5.4 |
| J25 | `+5V` | 8 mm | P3_J_PWR.4 ↔ agujero (27.9; 68.6) mm, junto a P3_J_PWR.4 |
| J26 | `+5V` | 15 mm | agujero (104.1; 63.5) mm, junto a P4_J_PWR.1 ↔ P4_J_PWR.4 |
| J27 | `-16V` | 5 mm | agujero (22.9; 55.9) mm, junto a P3_U6.1 ↔ P3_J_PWR.2 |
| J28 | `GND` | 15 mm | P3_U2.3 ↔ agujero (66.0; 61.0) mm, junto a P3_U2.8 |
| J29 | `-16V` | 5 mm | agujero (111.8; 55.9) mm, junto a P4_U6.1 ↔ P4_J_PWR.2 |
| J30 | `P3_U2N` | 15 mm | P3_POT1.1 ↔ P3_U2.2 |
| J31 | `P4_U2N` | 15 mm | P4_POT1.1 ↔ P4_U2.2 |
| J32 | `-16V` | 6 mm | P3_U2.4 ↔ agujero (61.0; 47.0) mm, junto a P3_POT1.1 |
| J33 | `-16V` | 6 mm | P4_U2.4 ↔ agujero (149.9; 47.0) mm, junto a P4_POT1.1 |
| J34 | `P3_VOFFD` | 5 mm | P3_R15.1 ↔ P3_R14.2 |
| J35 | `P4_VOFFD` | 5 mm | P4_R15.1 ↔ P4_R14.2 |
| J36 | `GND` | 5 mm | agujero (94.0; 45.7) mm, junto a P4_R12.2 ↔ P4_R12.2 |
| J37 | `+16V` | 15 mm | agujero (61.0; 25.4) mm, junto a P3_U3.8 ↔ P3_U4.7 |
| J38 | `+16V` | 15 mm | agujero (149.9; 25.4) mm, junto a P4_U3.8 ↔ P4_U4.7 |
| J39 | `GND` | 10 mm | agujero (17.8; 30.5) mm, junto a P3_R2.1 ↔ P3_R4.2 |
| J40 | `P3_VD` | 15 mm | P3_POT3.2 ↔ agujero (58.4; 30.5) mm, junto a P3_ROFFSET.2 |
| J41 | `GND` | 10 mm | agujero (106.7; 30.5) mm, junto a P4_R2.1 ↔ P4_R4.2 |
| J42 | `P4_VD` | 15 mm | P4_POT3.2 ↔ agujero (147.3; 30.5) mm, junto a P4_ROFFSET.2 |
| J43 | `P3_VE` | 23 mm | agujero (38.1; 17.8) mm, junto a P3_RBIAS.1 ↔ P3_R6.1 ↔ agujero (48.3; 29.2) mm, junto a P3_ROFFSET.1 |
| J44 | `P4_VE` | 23 mm | agujero (127.0; 17.8) mm, junto a P4_RBIAS.1 ↔ P4_R6.1 ↔ agujero (137.2; 29.2) mm, junto a P4_ROFFSET.1 |
| J45 | `P3_SUMN` | 5 mm | agujero (67.3; 26.7) mm, junto a P3_U5.1 ↔ P3_R8.2 |
| J46 | `P4_SUMN` | 5 mm | agujero (156.2; 26.7) mm, junto a P4_U5.1 ↔ P4_R8.2 |
| J47 | `-16V` | 13 mm | agujero (58.4; 12.7) mm, junto a P3_U3.5 ↔ P3_U5.4 |
| J48 | `-16V` | 13 mm | agujero (147.3; 12.7) mm, junto a P4_U3.5 ↔ P4_U5.4 |
