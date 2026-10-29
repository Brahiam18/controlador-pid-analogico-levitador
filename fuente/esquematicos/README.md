# Esquemáticos (circuitikz), versión 2

| Archivo | Contenido |
|---|---|
| `esq_entrada.pdf/.png` | Red, F1, S1, transformador 18‑0‑18 V / 3 A, J1, F2/F3, puente D1–D4 y filtros C1 (15 000 µF) y C2A+C2B (2 × 6800 µF) |
| `esq_pos.pdf/.png` | Riel +16 V: limitador con foldback (RSC1, Q1–Q2 Darlington, Q3, R5–R6), ampliación de corriente (R7, Q4), U1 LM317 y J4 para `R_L` |
| `esq_neg.pdf/.png` | Riel −16 V: espejo con Q5–Q8, U2 LM337 y J5 |
| `esq_5v.pdf/.png` | Riel +5 V: R19 y regulador U3 LM317 |
| `esq_salida.pdf/.png` | Bornera de salida J2, regleta de prueba J3 y borneras J4/J5 de la carga |
| `esq_completo.pdf/.png` | Todo en una hoja |

Fuentes: `etapa_*.tikz` (una por etapa), `estilo.tex` (estilo común), `wrap.tex` y `esq_completo.tex`. Para compilar una etapa:

```bash
pdflatex -jobname=esq_pos "\def\etapa{etapa_pos.tikz}\input{wrap}"
pdflatex esq_completo.tex
```
