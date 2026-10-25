# Esquemáticos (circuitikz)

| Archivo | Contenido |
|---|---|
| `esq_entrada.pdf/.png` | Red, F1, S1, transformador M509, J1, F2, rectificadores D1/D2 y filtros C1/C2 |
| `esq_pos.pdf/.png` | Riel +16 V: limitador RSC1–Q1–Q2 y regulador U1 LM317 |
| `esq_neg.pdf/.png` | Riel −16 V: limitador RSC2–Q3–Q4 y regulador U2 LM337 |
| `esq_5v.pdf/.png` | Riel +5 V: R9 y regulador U3 LM317 |
| `esq_salida.pdf/.png` | Bornera de salida J2 y regleta de prueba J3 |
| `esq_completo.pdf/.png` | Todo en una hoja |

Fuentes: `etapa_*.tikz` (una por etapa), `estilo.tex` (estilo común), `wrap.tex` y `esq_completo.tex`. Para compilar una etapa:

```bash
pdflatex -jobname=esq_pos "\def\etapa{etapa_pos.tikz}\input{wrap}"
pdflatex esq_completo.tex
```
