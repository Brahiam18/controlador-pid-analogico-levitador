# Simulación (ngspice), versión 2

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
