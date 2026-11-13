# Resumen del proyecto para el plan de posgrado

## Español
**Controlador PID analógico para un levitador magnético** · Ingeniería Electrónica, Universidad de Ibagué · 2026 · [github.com/Brahiam18/controlador-pid-analogico-levitador](https://github.com/Brahiam18/controlador-pid-analogico-levitador)

Diseñé, simulé y construí un sistema de control 100 % analógico para mantener un imán de neodimio (Ø25,4 mm, 7,9 g) suspendido sobre cuatro bobinas con núcleo de hierro. Cada bobina tiene su propio lazo: sensor Hall SS495A, amplificador de error, PID en paralelo con operacionales TL074, sumador con offset y etapa de potencia lineal (convertidor tensión-corriente con TIP122). El trabajo cubrió el cálculo a mano de cada etapa, la simulación en Proteus, un informe técnico en formato IEEE (LaTeX), el diseño de una PCB de 2 PID (Fusion/EAGLE) fabricada de forma casera, una fuente de ±16 V, una base impresa en 3D con soportes de sensor y un modelo de la fuerza magnética por elementos finitos 2D/3D con solvers propios en Python. La depuración en banco de los cuatro PID (etapas, corriente por bobina, calibración de referencias) quedó documentada.

**Resultados:** las etapas medidas coinciden con lo calculado con diferencias de hasta 2 % donde el valor es mayor de 0,5 V, y la salida del controlador se mueve en el rango de diseño de 1–3 V. La simulación estima ≈0,7 A por bobina a 30 mm (±15 %).

**Estado:** los cuatro PID funcionan por separado, pero la levitación estable a 3 cm aún no se logró: falta un método rápido para fijar las tensiones de referencia y la señal de los sensores varía muy poco. No se presentó en la muestra METIE 2026 (sí el póster); el trabajo sigue en 2027, posiblemente como proyecto de dos materias.

**Qué aprendí y cómo se relaciona con instrumentación biomédica:** acondicionamiento de señal analógica con sensores lineales, lazos de realimentación y su sensibilidad a la ganancia y al ruido, alimentación limpia, diseño y depuración de PCB, y validación con mediciones frente al modelo.

## English
**Analog PID controller for a magnetic levitator** · Electronic Engineering, Universidad de Ibagué · 2026

I designed, simulated and built a fully analog control system to hold a neodymium magnet (Ø25.4 mm, 7.9 g) above four iron-core coils. Each coil has its own loop: an SS495A Hall sensor, an error amplifier, a parallel PID built with TL074 op-amps, a summing stage with offset and a linear V-to-I power stage (TIP122). The work included hand calculations, Proteus simulation, an IEEE-style technical report (LaTeX), a 2-PID PCB designed in Fusion/EAGLE and fabricated in-house, a ±16 V supply, a 3D-printed base with sensor mounts, and a 2D/3D finite-element model of the magnetic force written with custom Python solvers. Bench debugging of the four PIDs is documented.

**Results:** measured stage outputs match the calculations within 2 % where the value exceeds 0.5 V, and the controller output stays in the 1–3 V design range. The model estimates ≈0.7 A per coil at 30 mm (±15 %).

**Status:** the four PIDs work individually, but stable levitation at 3 cm is still pending: a faster way to set the reference voltages is needed and the Hall sensors see only a very small field variation. The project was not demonstrated at the 2026 METIE student showcase (the poster was); work continues in 2027.

**Relevance to biomedical instrumentation:** analog signal conditioning with linear sensors, feedback loops and their sensitivity to gain and noise, clean power supplies, PCB design and debugging, and validating measurements against a model.
