# Preregistration: exp64b — the anatomy of the −0.56 decay exponent

**Status: SEALED before any virgin network was generated. Single run. All cells of
the interpretation matrix are publishable.** Judge script (tests64.py) frozen
alongside this document; quality gate (pedestal share ≤ 0.15) and all bars frozen
below. Training was performed exclusively on burned networks from exp61b and is
disclosed in full below (in Spanish, as the program's working language).

---

# Diseño exp64b — la anatomía del exponente −0.56 (confirmatorio, EN FRÍO)

## Pregunta
El sello 74b5407 dejó abierto POR QUÉ T_c ∝ λ^(−0.56) y no λ^(−1) (la derivación
naive). Hipótesis entrenada (24 redes quemadas de exp61b): la sublinealidad se
FACTORIZA en dos piezas:

1. **Tasa sublineal**: la tasa de decaimiento γ del perfil coherente e(t) crece
   sublineal con λ (entrenamiento: pendiente ln-ln +0.753, Spearman +0.763).
   Mecánica propuesta: λ es el exponente de Lyapunov MÁXIMO; la respuesta proyecta
   sobre muchas direcciones que se revuelven más despacio que la peor.
2. **Cuantil estirado**: T_c (cuantil 80% de e acumulada) escala con γ más suave que
   el −1 de un exponencial puro (entrenamiento: pendiente −0.860, Spearman −0.859),
   porque la cola de e(t) es más pesada que exponencial cerca del borde (la forma
   cruza: potencia gana con λ chico, exponencial con λ>0.13).

Producto entrenado: 0.753 × 0.860 = −0.648 ∈ IC sellado [−0.79, −0.33]. ✔

## Entrenamiento revelado (todo en redes QUEMADAS)
- Fase 1 MUERTA: distancia cruda entre gemelas inválida por construcción (escala
  coherente ~0.03/canal < piso de ruido ~0.07); REGISTRO-64.md.
- Fase 2: 24 redes, γ y α por ajuste sobre [pico, 1% del pico]; números de arriba.
- Diagnóstico: reconstruir W desde ρ redondeado (4 dec) cambia perfiles individuales
  por sensibilidad caótica (T_c 69→104); estadística equivalente; el confirmatorio
  genera ρ con precisión completa y lo guarda completo.
- Fase 3: confiabilidad split-half de γ (10 redes, dos verdades independientes
  +10..13 vs +20..23). SIN compuerta: techo γ +0.406, α +0.370, control T_c +0.103
  (¡no 0.976!) — dos redes patológicas de señal débil (820352: T_c 449 vs 5) y rango
  comprimido destruyen la confiabilidad de rango. Lección: el techo de un blanco
  depende de la POBLACIÓN; se mide en el dominio del claim. CON compuerta de calidad
  (share de pedestal ≤ 0.15): **techo γ = +0.964, techo T_c = +0.964** (7/10 pasan;
  la compuerta atrapa exactamente a las dos patológicas, con una exclusión
  colateral). Fase 2 re-entrenada con compuerta (n=20/24): tasa +0.677 (Spearman
  +0.759), cuantil −0.834 (Spearman −0.827), producto −0.565.
- El share de pedestal se definió y midió ANTES en el diagnóstico que salvó la ley
  sellada (diag64_pedestal.py: share mediano 3.5%, no correlaciona con λ, corregirlo
  acerca la pendiente al valor sellado).

## Protocolo confirmatorio (UNA corrida)
- 48 redes VÍRGENES, base de semillas 1_100_000 (rango jamás tocado; convenciones:
  seed→W, 79000+seed→ρ~U(1.0,4.0), seed+1→λ, seed+2→pulso, seed+10..13→verdad).
- Aceptación estratificada por λ medido: 4 estratos de exp61b
  {(0.01,0.03], (0.03,0.08], (0.08,0.15], (0.15,0.30]} × 12.
- Por red: perfil e(t) a escala verdad (n=2000, maquinaria entrenamiento46 exacta),
  T_c, γ y α por los ajustes de entrenamiento64b.ajustes (congelados).
- Pendientes por OLS en ln-ln; IC 95% por bootstrap de redes (10000 remuestras).

## Claims a sellar (barras CONGELADAS; entrenados gateados entre paréntesis)
Sobre las redes que pasan la compuerta congelada (share ≤ 0.15, γ > 0); si pasan
menos de 32, el protocolo es INDETERMINADO por potencia y se reporta.
- **E1 (tasa sublineal)**: Spearman(ln λ, ln γ) ≥ +0.55 (entrenado +0.759) Y el
  IC95 bootstrap (10000, semilla 64) de la pendiente OLS excluye +1.0 con pendiente
  puntual en (0, +0.95] (entrenada +0.677).
- **E2 (cuantil estirado)**: Spearman(ln γ, ln T_c) ≤ −0.65 (entrenado −0.827) Y el
  IC95 de la pendiente excluye −1.0 con pendiente puntual en [−0.95, −0.60]
  (entrenada −0.834).
- **E3 (cierre del producto)**: pendiente(E1) × pendiente(E2) ∈ [−0.79, −0.33]
  (el IC sellado de 74b5407; entrenado −0.565).
Barras bajo el techo gateado 0.964 con margen ≥0.13 respecto de lo entrenado
(lección exp61: no sellar al filo). Juez: tests64.py (congelado junto a este doc).

## Matriz de interpretación (todas las celdas publicables)
- E1✔ E2✔ E3✔: la anatomía del −0.56 queda escrita — tasa sublineal + cola pesada.
- E1✔ E2✘: la sublinealidad vive solo en la tasa; la historia del cuantil muere.
- E1✘ E2✔: la tasa es lineal en λ; toda la sublinealidad vive en la forma/cuantil.
- E1✘ E2✘: la factorización entera es un artefacto del entrenamiento; se reporta.
- E3✘ con E1✔E2✔: las piezas existen pero no cierran el número; abierto se queda
  abierto y se reporta el gap.

## Notas de honestidad
- γ y T_c salen del MISMO perfil e(t): E2 no es tautológico (un exponencial puro
  forzaría −1) pero sí comparte ruido de medición; el techo de fase 3 acota eso.
- Los estratos y el rango λ≤0.30 son los de exp61b: mismo dominio del sello original.
