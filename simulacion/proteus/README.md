# Simulación en Proteus

| Archivo | Contenido |
|---|---|
| `EtapaPID1.pdsprj` | Proyecto de Proteus (ISIS): PID completo (U1 a U7), convertidor tensión-corriente (U8), TIP122, bobina y protección. |

Los modelos son LM741 y TIP122 de las bibliotecas de Proteus. La etapa de potencia simulada usa una **variante** (resistencia de sensado de 1 Ω / 10 W, bobina de 6 Ω, fuente de 24 V); el montaje real usa 3 × 1 Ω (0.33 Ω), una bobina de unos 4 Ω y TL074CN. Ver la explicación en el [README principal](../../README.md#etapa-de-potencia-convertidor-tensión-corriente).

Un `.pdsprj` es un archivo comprimido; se abre con Proteus 8 (Archivo → Abrir proyecto). No se incluye el archivo `.workspace`, que solo guarda la disposición de ventanas de un equipo.
