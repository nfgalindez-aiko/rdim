# Preregistro — Teoría de la banda de visibilidad (P-band, P-trials)

**Sellado ANTES de ejecutar cualquiera de estos análisis.** Deriva del formalismo en
`02-apuestas/teoria-v1.md` §1b (matriz de respuesta = matriz de controlabilidad de Krylov;
banda de visibilidad cerrada por ventana y por divergencia de varianza en la marginalidad).

## Contexto: qué ya sabemos y por qué esto es riesgoso
El conteo crudo de modos marginales FALLÓ como predictor (exp25: Spearman −0.31, invertido)
y el mejor predictor conocido es el escalar −|λ_max| (+0.44). Si la teoría de la banda es
correcta, un conteo de modos **derivado de la fórmula de visibilidad** (sin parámetros libres
ajustados) debe superar a ambos. Si no lo supera, la teoría queda como descripción sin poder
predictivo y se reporta así.

## H1 (primaria, simulación) — P-band
Definición sin parámetros libres, calculada desde el espectro y el pulso:
un modo i es *visible* si  |ln|λ_i||·W < ln(SNR_i)  con  SNR_i = |w_i·p|·√n·√(1−|λ_i|²)/σ,
donde λ_i, w_i son autovalor y autovector izquierdo del jacobiano medio, p el pulso,
W la ventana en pasos, n el número de trials, σ el desvío del ruido. B = #{modos visibles}.

- **Test:** Spearman(R-dim pareada, B) en 50 redes ESN con λ_max muestreado en [−0.5, +0.15].
- **Criterio de éxito:** ρ > 0.5 con p < 0.01 **y** ρ(B) > ρ(−|λ_max|) en la misma muestra.
- **Criterio de fracaso:** cualquier otro resultado. Se publica igual.

## H2 (secundaria, simulación) — P-trials: crecimiento logarítmico sin saturación
Dos modelos rivales para R-dim(n) con n = 16, 32, 64, 128, 256 trials, en redes al borde
(|λ_max| < 0.02), ventana fija:
- **M_banda:** R-dim(n) = a + b·ln(n), b > 0, sin plateau.
- **M_fijo:** R-dim(n) = D_max·(1 − e^{−n/n₀}) — satura en la dimensión "verdadera".

- **Tests:** (i) incremento R-dim(256) − R-dim(128) > 0 (test de signos sobre 20 redes,
  una cola, α=0.05); (ii) M_banda tiene menor AIC que M_fijo en ≥ 70% de las redes.
- **Éxito:** ambos. **Fracaso parcial:** uno solo. Se reporta lo que salga.

## H3 (terciaria, humanos) — P-trials en cerebros reales
En 12 sujetos de ds008037 (CC0) con ≥120 trials válidos en el sitio prefrontal, submuestrear
n = 16, 30, 60, 120 trials (primeros n válidos, sin reordenar) y calcular R-dim y XV.
- **Test:** Spearman(ln n, R-dim) > 0 dentro de sujeto; test de signos del incremento
  120 vs 60 sobre los 12 sujetos (una cola, α=0.05).
- Es la primera vez que se preguntaría a datos humanos si la dimensión reproducible satura o
  no. Cualquier resultado es informativo y se publica.

## Reglas de ejecución (fijadas)
- Parámetros del estimador idénticos a los papers (k=1.2, min_snr=1.1, max_var=99, n_steps=50,
  4 splits). Ventana de respuesta fija en todos los n.
- Semillas fijas y declaradas en los scripts (exp26, exp27, exp28).
- Ningún análisis se mira antes de que el script complete la corrida entera.
- No se corren variantes adicionales de estas hipótesis si fallan: se reportan y se para.

## Sellado
Este archivo se publica en el repositorio público https://github.com/nfgalindez-aiko/rdim
(carpeta `preregistrations/`) ANTES de ejecutar exp26/27/28, y se depositará en Zenodo en el
próximo lote de depósitos.
