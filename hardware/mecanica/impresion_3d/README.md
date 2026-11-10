# Base impresa en 3D

Piezas para imprimir (STL en mm, generadas por `../generador/base_3d.py`):

| Archivo | Cant. | Medidas | Qué es |
|---|---|---|---|
| `soporte_bobinas.stl` | 1 | 120 × 120 × 37 | Plantilla con 4 alojamientos Ø36,5 (centros a ±18,5 mm), 4 postes y hueco central Ø14 |
| `tapa_bobinas.stl` | 1 | 120 × 120 × 2,5 | Tapa que sujeta las pestañas de las bobinas; se atornilla a los postes (M3) |
| `bandeja_baqueta.stl` | 2 | 214 × 164 × 12 | Bandeja para una baqueta de 200 × 150 mm sobre 6 soportes de 8 mm |
| `capuchon_sensor.stl` | 4 | Ø12 × 6,5 | Capuchón aislante sobre la punta del núcleo con asiento para el sensor Hall |

## Diseño
- Las bobinas (29 mm de alto, núcleo Ø6 × 45 mm que sobresale 8 mm por lado) entran en alojamientos de 8 mm de profundidad.
  El piso es de 8 mm, de modo que el núcleo queda a ras de la cara inferior y la placa apoya plana.
- Los 4 alojamientos están unidos entre sí (sin paredes de menos de 1 mm); cada uno tiene un canal de 8 mm para sacar los cables de la bobina.
- La tapa deja libre la cara superior de cada bobina (aberturas Ø32) para poner el sensor Hall sobre el núcleo.
- Sensores: el SS495A (cuerpo 4,06 × 3,0 × 1,57 mm, medidas genéricas) va en el asiento del capuchón, que lo separa del núcleo de hierro
  para que sus terminales no hagan contacto con la barra. El canal del capuchón se gira hacia el centro del soporte.
  El sensor queda unos 2 mm más alto que si se pegara directo al núcleo: el Vref se calibra con el montaje armado.
- Cables de los sensores (4 × 3 hilos): bajan por el hueco central, siguen por un canal inferior de 12 × 5 mm y salen por una ventana
  de 24 × 6 mm al frente del soporte (con ventana igual en la tapa), donde se conecta un cabezal de 12 pines (2 × 6, paso 2,54 mm).
- Fijación del soporte al tablero: 4 tornillos M4 en (±52, ±45), con avellanado.
- Fijación de la tapa: 4 tornillos M3 en los postes (±52, 0) y (0, ±52); piloto Ø2,6 para autorroscar.
- Fijación de cada bandeja: 4 tornillos M4 en (±50, ±40), con avellanado; la baqueta se atornilla a los soportes con M3 (perforar la baqueta en las esquinas).

## Recomendaciones de impresión
- PLA o PETG, relleno 25–30 %, 3 perímetros, altura de capa 0,2 mm, **sin soportes** (cada pieza se imprime apoyada sobre su cara plana).
- Imprimir primero un alojamiento de prueba, o medir la bobina real: si la pestaña mide más de Ø36,0 o la altura no es 29 mm, hay que ajustar `D_FL` y `H_BOB` en `base_3d.py`.
- Si queda juego vertical entre bobina y tapa, calzar con cinta o espuma fina.
- Usar tornillos de **nylon o latón** cerca de los núcleos: el acero distorsiona el campo.
- Las posiciones de bobinas y sensores no cambian; la altura de levitación se ajusta solo con el Vref de cada PID.
