> *Adversarial review report (in Spanish, the program's working language). Part of the program's five-step sealing procedure: before or upon deposit, each protocol is attacked by an independent reviewer whose default verdict is BROKEN. Published so the audit itself can be audited.*

# Auditoría adversarial de los 8 papers publicados — 31/08/2026

Cuatro revisores adversariales independientes (por defecto ROTO, dos ataques
obligatorios + 8 preguntas), uno por grupo de papers. **Todo número citado abajo fue
recomputado mecánicamente por el autor desde los datos crudos antes de aceptarlo**
(`verificar_ataque_adversarial_6.py`, `_8.py`, `verificar_determinismo_rdim.py`).

Los cuatro devolvieron NO SELLABLE. Ninguno de los resultados centrales de los papers
1, 2, 3, 5 fue invalidado; los problemas son de dos clases: **claims sobrevendidos** y
**un confundidor no reportado**.

---

## 🟢 LO QUE SOBREVIVIÓ TODOS LOS ATAQUES

- **R-dim ahora TIENE banco de verdad conocida, y lo pasa.** No existía. Un revisor lo
  construyó: inyectando k direcciones coherentes sobre camas ESN reales, R-dim lee
  k=3→3.16, k=5→4.94, k=10→9.60, **y lo hace igual en orden, borde y caos**. El
  instrumento mide lo que dice medir.
- **R-dim reproduce exacto** desde la semilla (8/8; las diferencias son el redondeo a
  3 decimales del archivo).
- **La crítica al PCIst del paper 1 es irreprochable**: comparación contra el clon
  oficial sin modificar, con sus parámetros publicados, y la coincidencia es
  **bit-idéntica** (max|dif| = 0.0000) — el paper subestima su propio resultado.
- **La U invertida del paper 2 aguanta**: no es confusión duración/dimensión (test
  con soporte temporal variable a energía constante: R-dim plano), no es band-shopping
  (20 combinaciones de banda, p entre 0.0014 y 0.019 siempre en la misma dirección),
  no es energía.
- **La teoría lineal exacta del paper 8 (κ=0.378)**: orden +0.966 contra ρ sola +0.880;
  error 0.334 contra un nulo constante de 1.843 que **falla** la vara de 1.0. El
  criterio tenía poder y la teoría lo pasó limpio.
- **La ley de saturación** (papers 8/9): intervalos lejos de cero en los cuatro
  estratos, 5/5 mundos, 3/3 familias.
- **El resultado central del paper 5** (sin techo detectable): resistió el piso de
  rectificación, la cobertura de electrodos, la regresión a la media y el poder de T1
  (91% para −0.40). Corregir por el nulo lo **fortalece** (T2 de 1.8e−5 a 1.6e−8).
- **El paper 3 publicó su nulo y cambió de título.** Es el que mejor pasa la prueba de
  refutabilidad.
- **La higiene de preregistro del paper 6** es la mejor del programa: enmiendas con
  sello público ANTES de cualquier estadística confirmatoria.
- **Circularidad LFP↔spikes (paper 7): descartada.** Si el campo estuviera contaminado
  por esas neuronas, los niveles correlacionarían; no lo hacen (ρ=+0.25/+0.22).

---

## 🔴 HALLAZGO 1 (el más grave): el efecto del paper 6 está explicado por la GANANCIA

Verificado en `verificar_ataque_adversarial_6.py` sobre los MISMOS 120 ensayos:

| | |
|---|---|
| Spearman(cociente de amplitud evocada, brecha de R-dim) | **+0.648 (p = 0.0020)** |
| Ajuste | d = −0.340 + 0.969·log(γ), R² = 0.43 |
| **Efecto de estado a GANANCIA IGUAL (γ=1)** | **−0.340 ± 0.278 → indistinguible de cero** |
| Mitad de baja ganancia (γ<2.64, n=10) | mediana +0.20, **6/10, p = 0.42** |
| Mitad de alta ganancia (n=10) | mediana +0.82, 10/10, p = 0.0010 |
| Los 4 animales con signo invertido | son 4 de los 5 de **menor** ganancia |

Y el propio programa lo confirmó bajo sello después (protocolo 9be5d99, "la anestesia
como perilla de ganancia", mediana D_obs/D_pred = 1.003). **El paper 6 no lo cita.**

**Además, "nivel, no pendiente" está refutado por sus propios datos.** En un
subconjunto FIJO de 15 animales, la brecha se reduce monótonamente:

| n | 30 | 60 | 120 | 240 |
|---|---|---|---|---|
| brecha mediana | +0.784 | +0.660 | +0.535 | **+0.383** |

La curva anestesiada alcanza parcialmente a la despierta — que es exactamente la firma
del confundidor de ganancia (con más ensayos baja el piso, las componentes atenuadas
reaparecen).

**Otros dos defectos del paper 6:** el *blanking* de artefacto que declaran el prereg
y los Métodos **nunca se aplicó en el código** (`pipeline34.py` define `BLANK` y no la
usa; el filtrado es de fase cero sobre la época con artefacto), lo que invalida el
argumento diagnóstico de §3.1; y §3.4 compara el p de PCIst de una muestra (n=22,
n_max) contra el p de R-dim de otra (n=20, n=120) diciendo "on the identical matched
trials".

---

## 🔴 HALLAZGO 2: la segunda constante y la teoría efectiva del paper 8 no superan a nulos triviales

Verificado en `verificar_ataque_adversarial_8.py`:

- **El criterio de nivel no podía refutar.** La fórmula da error 1.183 (vara 1.5), pero
  un predictor que **ignora la red por completo** da **1.367 → también pasa**. La
  ventana de constantes que aprueban es c ∈ [0.431, 0.750], el 46% del rango plausible.
- **La fórmula pierde contra una constante por mundo en 5 de 6.**
- **El comparador escalar sellado es un artefacto**: el 28% de las redes está pegado al
  techo de truncamiento K=30. Excluyéndolas, el margen cae a **+0.214 — por debajo de
  la vara sellada de 0.25: la cláusula falla.**
- **Los nulos triviales le ganan a la teoría en 4 de 5 mundos:**

| mundo | teoría efectiva | ⟨g⟩ sola | −ρ sola |
|---|---|---|---|
| N128 | +0.576 | **+0.640** | +0.632 |
| **N256** | **+0.286** | **+0.696** | **+0.694** |
| dale | +0.436 | **+0.525** | +0.529 |
| ruido02 | **+0.724** | +0.664 | +0.638 |
| ruido10 | +0.509 | +0.602 | **+0.616** |

La "degradación con N" no es un borde mapeado: es la teoría siendo 2.4× peor que un
solo número leído de la red.

---

## 🟠 HALLAZGO 3 (transversal): R-dim tiene un piso de rectificación que nunca se reportó

R-dim = Σ max(corr, 0) — suma de correlaciones cruz-mitad **clipeadas en cero**. Bajo
el nulo, el clip conserva solo la mitad positiva del ruido, así que la esperanza es
estrictamente positiva y escala con el número de componentes retenidas:

| dato | piso medido |
|---|---|
| campo, 30–110 canales | ~0.44 – 1.2 |
| poblaciones de 300–1000 unidades (spikes) | **~2.5** |

Contra una mediana de isoflurano publicada de 4.69 en el paper 7, y valores
individuales que caen **en o bajo el piso** (sub-590479 campo despierto = 0.33).

**Y la herramienta pública no puede medirlo**: `null_floor()` devuelve `xv`, nunca
`rdim` (`core.py:150`), contra su propia doctrina escrita ("an estimate without its
null is not a measurement"). Ningún pipeline lo llama.

**Alcance del daño (medido, no supuesto):** el piso es **plano en cantidad de ensayos**
y **plano entre 30 y 110 canales**. Por lo tanto **NO afecta** los claims de
crecimiento (C6, C7, paper 5 entero) ni los contrastes dentro del mismo montaje. **SÍ
afecta** las comparaciones de nivel entre modalidades o entre sistemas (paper 7 "3.0×",
paper 4 C5 "techo de 9–11").

---

## 🟠 HALLAZGO 4: el paper 7 afirma más de lo que su matriz sellada autoriza

La matriz de `prereg_exp37` asigna al patrón observado (Q1 ✗, Q2 ✓) la lectura:
*"field complexity is **not** a proxy for population dimensionality"*, con Q3 marcado
"—". El paper titula *"Field-level perturbational complexity **tracks** neuronal
reproducible dimensionality"*. El test Q3 es legítimo y pasó su barra; lo que no está
autorizado es la lectura conjunta promovida al título.

Además Q3 lo sostiene un clúster: sin los 3 animales con reversión de signo, ρ pasa de
+0.636 (p=0.005) a **+0.301 (p=0.17)**. El campo acierta la **dirección**, incluso en
las reversiones; el acoplamiento **graduado** no está demostrado.

---

## 🟡 HALLAZGO 5: §3.3 del paper 5 (la auditoría del estimador) está mal en 3 de 4 afirmaciones

Son **una sola realización** de una cantidad con sd ≈ 0.2. Con 8 semillas:
- "sobre ruido sin respuesta R-dim **decrece** (0.83 → 0.09)" → **es plano en ~0.44**.
- "sobre **datos con estructura real**" → nunca se aplicó a datos reales; es simulación.
- "se mantiene bajo 1 sin crecimiento sistemático" → **crece 3.4× y supera 1 en 5/6
  semillas**.
- "con 3 componentes satura en n=30" → satura en **3.87 para una verdad de 3**.

Y las enmiendas del exp32 **no tienen sello público** (a diferencia de las del paper 6).

---

## 🟡 HALLAZGO 6: reporte selectivo en el paper 3

El control C2 (parcializar el RMS de baseline) **mata la asociación en la muestra de
descubrimiento** (+0.21, p=0.27) y sobrevive solo en la de réplica (+0.33, p=0.0012).
**El abstract cita solo la segunda.** Lo mismo con C3a (+0.15, p=0.44 en ExpA).
Y el claim vivo del sham dice "statistically indistinguishable" con p=0.09, sin test
de equivalencia: el IC95 de la diferencia admite hasta ~16% del índice.

---

## 🟡 HALLAZGO 7: errores puntuales en los papers 1, 2 y 4

- **Paper 1 §3.4: "XV remains ≤ 12 everywhere" es FALSO** (máximo real 23.1; 13/240
  realizaciones superan 12). Es la frase que autoriza usar XV sin nulo.
- **Paper 1: "statistically indistinguishable from pulsed data"** — no existe ningún
  test (n=3 redes por celda).
- **Paper 2 abstract**: empalma un número post-hoc (mediana 94, banda |λ|<0.01) con un
  p preregistrado que corresponde a otra banda (47.5); y dice n=92 donde el test usa
  **57**. El cuerpo lo dice bien; el abstract no.
- **Paper 2 §2.4**: "mediana R-dim 1.4" es la mediana de **una sola red**.
- **Paper 4 C5**: "converge a un techo de 9–11" está sobre-enunciado — el último
  doblaje todavía suma +0.28 (p=0.077) y el rango real es 3.98–11.53.
- **Paper 4 C6**: la cita apunta a preprint 3, que **no contiene ese análisis**.
- **Paper 4 P1**: "passed" sin decir que es frágil a un solo animal (jackknife peor
  caso p=0.084).

---

## PLAN DE CORRECCIÓN (por gravedad)

1. **Paper 6 → v2 sustancial.** Reportar el confundidor de ganancia con sus números,
   citar P1 (9be5d99), reescribir §3.2/§4 ("nivel, no pendiente" es insostenible),
   corregir Métodos sobre el blanking, corregir §3.4.
2. **Paper 8 → v3.** Retirar "portador esencial", rebajar "predice orden y nivel",
   reescribir la degradación con N como refutación parcial, arreglar los conteos de
   protocolos.
3. **Paper 7 → v2.** Alinear título y abstract con la matriz sellada; reportar la
   fragilidad de Q3; corregir el 3.0× por el piso.
4. **Arreglar la herramienta**: `null_floor()` debe devolver `rdim`; agregar el banco
   de verdad conocida a los tests. Esto es infraestructura y beneficia a todo el resto.
5. **Paper 5 → v2.** Rehacer §3.3 con ≥8 semillas y barras de error; sellar o declarar
   las enmiendas.
6. **Papers 1, 2, 3, 4 → correcciones puntuales** (erratas de texto, sin tocar
   resultados).
7. **Escribir `verificar_paper1/2/3.py`** — no existen; papers 1, 2 y 3 no tienen
   verificador mecánico.
