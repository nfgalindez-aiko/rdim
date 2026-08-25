# Preregistro — Teoría de la banda de visibilidad, CICLO 2 (enmienda consolidada)

**Contexto y disciplina.** El ciclo 1 (prereg_banda.md, sellado en commit b018c40) terminó
0/3 confirmadas, con defectos de instrumento documentados en el diario (h, i, j): H1 con
fórmula degenerada (B=0 en 50/50, test vacío), H2 con criterios no-diagnósticos en el rango
n≤256, H3 con conjunción frágil (su componente (a) dio 11/12, p=0.003). Esta es la ÚNICA
enmienda del programa de la banda: si este ciclo falla, la teoría pierde y se reporta como
perdida — sin tercer ciclo con estas hipótesis.

Todos los resultados se publican, sea cual sea el desenlace. Parámetros del estimador
idénticos a los papers. Semillas fijas declaradas en los scripts. Ningún resultado se mira
antes de que cada script complete su corrida entera.

## H1' (exp29) — El predictor por-modo, sin parámetros libres

Para cada red: A_eff = ⟨J_t⟩ (jacobiano medio sobre trayectoria ruidosa, 2000 pasos, burn 200);
autovalores λᵢ y autovectores derechos vᵢ (norma 1) / izquierdos wᵢ (biortogonales, wᵢ·vᵢ=1);
p = vector de pulso real. Con aᵢ = |wᵢ·p|, W = 598 pasos, n = 40 (trials por mitad del split),
σ = 0.05:

  Eₛᵢ = aᵢ² · min(W, 1/(1−|λᵢ|²))        [solo modos con |λᵢ| < 1]
  Eₙᵢ = 2·W·σ² / (n·(1−|λᵢ|²))
  corr_pred_i = Eₛᵢ / (Eₛᵢ + Eₙᵢ)
  **B₂ = Σᵢ corr_pred_i**   (la suma de replicabilidades predichas — comparable con R-dim,
                             que es la suma de correlaciones observadas)

- Muestra: 50 redes ESN nuevas (semillas frescas), λ_max QR ∈ [−0.5, +0.15], 80 trials + sham.
- **Éxito:** Spearman(R-dim pareada, B₂) > 0.5 con p < 0.01, **y** además supera al benchmark
  escalar Spearman(R-dim, −|λ_max QR|) en la misma muestra.
- Secundario descriptivo (no decide): correlación de Pearson entre B₂ y R-dim en valor
  absoluto (¿predice también la magnitud, no solo el orden?).

## H2' (exp30) — log vs saturación, en el rango donde divergen

- 20 redes al borde (|λ_max QR| < 0.02), n = 64, 128, 256, 512, 1024 trials (pulso + sham,
  R-dim pareada, primeros n trials, ventana fija).
- **Test primario (el diagnóstico):** incremento alto I_alto = R(1024) − R(512) vs incremento
  bajo I_bajo = R(128) − R(64), por red. M_banda (log) predice I_alto ≈ I_bajo (incrementos
  iguales por duplicación); el modelo saturante con el n0~77 ajustado en el ciclo 1 predice
  I_alto ≈ 0 << I_bajo. Criterio: mediana(I_alto) > 0 con Wilcoxon una cola p < 0.05, **y**
  mediana(I_alto / max(I_bajo, 0.1)) > 0.5.
- Secundario: AIC log vs saturante sobre los 5 puntos (se reporta, no decide).

## H3' (exp31) — humanos, con poder

- 30 sujetos de ds008037 con ≥120 trials válidos en prefrontal (orden por ID; los 12 del
  exp28 se INCLUYEN — sus curvas ya conocidas sesgarían solo si el criterio dependiera de
  ellas por poco; se reporta el resultado con y sin ellos como sensibilidad). Regla de
  reemplazo por fallo de pipeline, idéntica a exp21.
- n = 16, 30, 60, 120; primeros n válidos; pipeline exacto de exp28.
- **Primario ÚNICO:** dentro de sujeto, Spearman(ln n, R-dim) > 0; test de signos sobre los
  30 sujetos, una cola, α = 0.05.
- Secundarios (se reportan, no deciden): incremento 120>60 (signos); pendiente media b del
  ajuste R-dim = a + b·ln n con IC bootstrap.

## Sellado
Este archivo se publica en https://github.com/nfgalindez-aiko/rdim (preregistrations/)
ANTES de escribir o ejecutar exp29/30/31. El commit de sellado es el timestamp.
