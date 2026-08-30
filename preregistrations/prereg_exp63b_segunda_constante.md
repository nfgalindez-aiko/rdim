# Sealed protocol — Exp63b: the second constant (universal level calibration of the effective theory)
**Author:** Nicolas Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any confirmatory network was generated.
**Design frozen (seeds):** tanh-casa 920000+, N128 930000+, dale 940000+, erf 950000+, p4 960000+, ruido10 970000+ (caps +30000; rho como exp57b/exp51; una corrida; bootstrap no requerido).
(Contenido del diseño y barras, en espanol, tal como se congelo:)

## Hallazgo de entrenamiento (1590 redes quemadas de exp54+exp57, 12 mundos)
El cociente rdim/R_diag es casi constante: mediana global 0.610, y POR MUNDO 0.48-0.69
(casi todos 0.55-0.66). La "descalibracion" de la teoria efectiva es en su mayoria UNA
segunda constante universal. Con 0.610 congelada, el error absoluto mediano en quemadas
es 1.23 (por mundo 0.95-1.95; los tamanos grandes son los peores, consistente con la
frontera del exp57). Dependencias residuales debiles (g +0.40, R2 del ajuste lineal
0.19 — no se sella estructura residual, solo la constante).

## Sello (exp63b) — barras desde el entrenamiento, reglas #1-#2 (blanco rdim ~0.8)
Seis mundos virgenes de estres: tanh-casa, N128, dale, erf, p4, ruido10 (incluido el
peor caso conocido a proposito). 30 redes por mundo (aceptacion estratificada por
lambda como exp57b, ~8 por estrato), semillas nuevas por mundo. Por red: rdim y R_diag
(maquinaria congelada de 8bf6f60, kappa=0.378).
- **C1 (nivel global):** mediana |0.610*R_diag - rdim| <= 1.5 sobre las ~180.
- **C2 (transporte de la constante):** en >= 5 de los 6 mundos, el cociente mediano
  rdim/R_diag cae en [0.46, 0.76] (0.61 +/- 0.15).
Matriz: C1^C2 = la teoria efectiva pasa a predictor ABSOLUTO con dos constantes
universales (0.378 del mundo lineal + 0.610 de la linealizacion). Parciales/muertes:
reportadas; la constante quedaria local.
