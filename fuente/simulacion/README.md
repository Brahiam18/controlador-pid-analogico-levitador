# Simulación (ngspice)

- `modelos.lib`: modelos de diodos y BJT (parámetros publicados) y **modelos de comportamiento propios** del LM317, el LM337 y de los TIP31C/TIP32C (genéricos). Reproducen la referencia de 1,25 V, la corriente de ADJ, el dropout, la regulación de línea de 0,01 %/V y el límite interno de 1,5 A. No son modelos del fabricante.
- `fuente.cir.tmpl`: circuito completo, con la misma numeración que el esquemático.
- `simular.py`: corre los casos A (régimen), B (línea ±10 % y trimmers al máximo), C (escalones de carga) y D (cortocircuitos). Genera `figuras/` y `resultados_simulacion.json`.

```bash
sudo apt install ngspice
python3 simular.py
```
