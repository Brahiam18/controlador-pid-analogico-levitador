# Simulación (ngspice y Proteus), versión 2.1

- `modelos.lib`: modelos de diodos (1N4007, 1N4148, 1N5408) y BJT (BC547/BC557 con parámetros publicados; TIP41C/TIP42C y BD139/BD140 genéricos), y **modelos de comportamiento propios** del LM317 y el LM337. Reproducen la referencia de 1,25 V, la corriente de ADJ, el dropout, la regulación de línea de 0,01 %/V y el límite interno de 1,5 A. No son modelos del fabricante.
- `fuente.cir.tmpl`: circuito completo (transformador 18‑0‑18 V, puente, filtros, limitadores con foldback, ampliación de corriente, reguladores), con la misma numeración que el esquemático.
- `simular.py`: corre en paralelo los casos
  - A: régimen con `R_L` = 10 Ω en +16 V y en −16 V (uno a la vez);
  - B: red al −10 % y al +10 %;
  - C: conexión y desconexión de `R_L`;
  - D: cortocircuitos sucesivos de +16, −16 y +5 V con `R_L` puesta;
  - E: arranque con `R_L` con la red alta y baja;
  - F: curva V–I del foldback para tres tensiones de entrada.

  Genera `figuras/`, `resultados_simulacion.json` y `salida_simulacion.txt`.

```bash
sudo apt install ngspice
python3 simular.py
```

## Proteus
`proteus/lab3fuenteselec2.pdsprj`: proyecto de Proteus con el circuito armado por el autor (riel +16 V completo, riel −16 V, carga de prueba con selector vacío / carga / corto). Configuración usada:

| Elemento | Valor |
|---|---|
| Fuente de red (VSINE) | Amplitude 170 V (120 V rms), 60 Hz; 153 / 187 V para red −10 % / +10 % |
| Transformador TRAN-2P3S | Primary 10H, **Total Secondary 0.52H** (Proteus reparte la inductancia por mitades: 2 × (19,4/120)² × 10 H), Coupling 0.999 |
| Resistencia de devanados | 5 A: primario 1,2 Ω, secundario 0,4 Ω (3 A: 2 Ω y 0,9 Ω) |
| Carga de prueba | 4 × 10 Ω en serie-paralelo (10 Ω) |

Resultados (riel +16 V, R5 = 330 Ω, transformador 5 A): 15,9 V / 1,59 A con R_L (15,7 V con red baja), corto 0,89 / 0,60 / 0,28 A con red baja / nominal / alta, y recuperación con R_L en los tres casos.

Los cambios de la versión 2.1 (R5 = R13 = 330 Ω, transformador de 5 A con 0,2 Ω por mitad) ya están en `fuente.cir.tmpl`.
