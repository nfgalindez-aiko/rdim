> *Adversarial review report (in Spanish, the program's working language). Part of the program's five-step sealing procedure: before or upon deposit, each protocol is attacked by an independent reviewer whose default verdict is BROKEN. Published so the audit itself can be audited.*

# Revisión adversarial del sello 4630a2e (exp64b — anatomía del exponente −0.56)

**Naturaleza de este documento.** Paso 3 de la regla del sello (revisión
adversarial, por defecto ROTO), ejecutado **retrospectivamente**: la regla nació
horas después de que este sello se commiteara y corriera. Todos los números fueron
**recomputados mecánicamente** por el autor
(`10-auditorias/verificar_ataque_adversarial_64.py`,
`10-auditorias/nulo_exponencial_64.py`); ninguno se cita del informe sin verificar.

**Qué NO es.** No es revisión externa ni peer review: es un adversario interno
(otro contexto y otro rol, mismo linaje de modelo). El revisor declaró por su
cuenta que su Fase A no fue ciega, porque `REGISTRO-64.md` — que se le indicó leer —
contiene el veredicto en sus líneas finales. Sus ataques se construyeron sobre la
estructura del protocolo y sobre datos quemados, y las simulaciones decisivas
corrieron antes de abrir los resultados vírgenes, pero corresponde decirlo.

---

## Veredicto del revisor: NO SELLABLE — falta la calibración del nulo de E2 y el panel de sensibilidad de E1

## Ataques que FALLARON (el revisor los descartó él mismo)

- **El estimador de γ no está sesgado.** Alimentado con exponenciales sintéticas de
  γ conocida (0.008–0.20), la pendiente ln γ̂ ~ ln γ_real es **+1.0000**, sesgo
  relativo máximo 0.00%. El estimador es exacto.
- **El ruido no pasa las barras de correlación**: P(Spearman ≥ +0.55) = 5×10⁻⁵ por
  permutación.
- **λ no está mal medido**: confiabilidad re-simulada +0.990, error relativo mediano
  3.4%; la atenuación por dilución es ~1%.
- **La compuerta no fabrica E2** — al revés, es conservadora para E2: sin compuerta
  E2 da −0.703 y también pasa.
- **La truncatura de la ventana de 600 muestras no aplana E2**: la teoría exacta de
  una exponencial truncada da −0.999.
- **No hay contaminación de semillas** (verificado): entrenamiento 820000+,
  confirmatorio 1.100.000+; ningún flujo derivado se cruza (79000+seed cae en
  1.179–1.219M). Este eje del diseño es sólido.
- **El protocolo es genuinamente refutable**, y se demuestra: E1 efectivamente falla
  bajo perturbaciones leves (ver abajo). Un criterio que falla no es infalsificable.

## Ataques que PASARON

### 1. El nulo declarado de E2 es falso para esta tubería (defecto mayor)

`DISENO-64.md` afirma: *"E2 no es tautológico (un exponencial puro forzaría −1)"*.
**Es falso.** Poblaciones **100% exponenciales** — cero cola pesada — con los `ip`
y `share` realmente observados, pasadas por el `ajustes()` congelado, dan
(verificado):

| población sintética (cola pesada = 0) | pendiente E2 |
|---|---|
| ideal: ip=0, sin pedestal | −0.957 |
| ip=1 | −0.917 |
| ip=2 | −0.881 |
| ip=3 | −0.850 |
| **con ip y share reales por red** | *(ver `nulo_exponencial_64.py`)* |

Causa: el offset del pico y el pedestal residual agregan a T_c un término
**independiente de γ**, y cualquier término aditivo independiente de γ empuja la
pendiente desde −1 hacia 0 — exactamente el lado de la banda de aceptación.

**Demostración terminante del revisor:** construyó un `resultados_exp64b.jsonl`
sintético de 48 redes en un mundo donde la tasa es sublineal pero los perfiles son
**exponenciales puros**, y corrió el **juez congelado real** sobre él: **3/3 PASA,
producto −0.564**. El juez no distingue la celda "E1✔E2✔" de "E1✔E2✘" que su matriz
de interpretación dice poder distinguir.

**Consecuencia: "el IC excluye −1, luego la cola es más pesada que exponencial" es
inferencia inválida.** El enunciado correcto se computa contra el nulo real.

### 2. E1 es marginal y no robusto

Verificado:

| muestra | pendiente | IC95 | E1 |
|---|---|---|---|
| **oficial (43 gateadas)** | +0.724 | [+0.439, **+0.998**] | **PASA** |
| sin compuerta (48) | +0.915 | [+0.584, **+1.237**] | **FALLA** |
| jackknife peor caso (sin s=1100067) | +0.846 | [+0.628, **+1.049**] | **FALLA** |

El IC excluye +1 por 0.002; el p unilateral bootstrap contra +1 es 0.0234, apenas
bajo el 0.025 que el criterio exige de hecho. `s=1100067` es un punto de
apalancamiento extremo: ρ=3.2515 (fuertemente caótica) pero el λ más bajo de las 48
(0.0106), residuo de −4.33σ en la relación λ|ρ (el siguiente es −1.85σ). No es error
de medición (λ tiene confiabilidad +0.990): es una red genuinamente atípica, pero
**el claim no debería colgar de ella**.

### 3. La compuerta se volvió λ-dependiente en las vírgenes

El chequeo de neutralidad hecho en entrenamiento **no transfirió** (verificado):

| | share vs λ |
|---|---|
| entrenamiento (24 quemadas) | +0.083 (p=0.70) — neutral |
| **confirmatorio (48 vírgenes)** | **−0.350 (p=0.015)** — λ-dependiente |

Excluyó 5 de 48, **4 de ellas en los dos estratos de λ más bajo** (composición
12/12/12/12 → 10/10/12/11; excluidas: 1100014 λ=+0.237 share=0.26, 1100056
λ=+0.070 share=0.34, 1100064 λ=+0.037 share=0.30, 1100120 λ=+0.017 share=0.19,
1100140 λ=+0.015 share=0.71). Retirar puntos de γ bajo en el extremo de λ bajo
levanta el extremo izquierdo de la regresión y aplana la pendiente. **La única
cláusula que depende de la compuerta es la que la compuerta rescata.** No hay mala
fe — la compuerta estaba congelada y se aplicó a ciegas — pero es un hecho
publicable.

### 4. E3 no es un tercer test independiente

Dado E1✔ (pendiente en (0, 0.95]) y E2✔ (en [−0.95, −0.60]), E3 solo exige que el
producto caiga en [−0.79, −0.33]: pasa en la mayor parte del rectángulo conjunto,
falla solo en dos esquinas estrechas. Las bandas se eligieron conociendo el IC
sellado. **"3/3" debe leerse como "dos tests más una verificación de consistencia
aritmética".**

### 5. Grietas menores

- **No hay celda de marginalidad pre-declarada.** La regla "no sellar al filo" se
  aplicó a las barras contra lo entrenado, nunca al resultado contra la barra. No
  existía regla previa para "el IC excluye el nulo por 0.002" — que es lo que pasó.
- **INDETERMINADO no está en la matriz de interpretación**, pese a que la tasa de
  exclusión del entrenamiento (3/10) proyectaba ~33.6 de 48 contra un umbral de 32.
- **Discrepancia de definición de la compuerta**: el entrenamiento exige share ≤
  0.15 en **ambas** verdades; el confirmatorio, en **una sola**. El techo +0.964 se
  midió bajo una compuerta más estricta que la aplicada.
- **El techo de γ (+0.964) es un Spearman sobre n=7**, dentro de la muestra en que
  se ajustó la compuerta: está sobreajustado y no puede citarse sin calificar.
- **α no tiene techo utilizable** (+0.370, nunca re-medido con compuerta): **nada
  puede afirmarse sobre la forma potencia-vs-exponencial**.
- `exp64b.py` calcula `ip` y `fin` y los descarta: sin ellos la calibración del nulo
  no es auditable por un tercero. Corregido en `10-auditorias/nulo_exponencial_64.py`.

## Preguntas donde el sello quedó BIEN

- **Condición de fracaso explícita y pre-declarada** (matriz con E1✘E2✘), con juez
  de booleanos duros.
- **Semillas limpias**, sin solape en ningún flujo derivado.
- **Reproducibilidad exacta**: ρ guardado con precisión completa; las redes se
  regeneran bit a bit.
- **Costo trivial** (~7 min en la netbook): ninguna presión computacional sobre el
  diseño.

## Consecuencia aplicada

El resultado se rebaja de **"3/3 confirmado"** a **dos cláusulas con estatus
distinto**: E2 sólido (sobrevive gateado, sin compuerta, y sin su red más
influyente) evaluado contra el nulo correcto; E1 **marginal y no robusto**; E3
verificación de consistencia, no confirmación independiente. Nada puede afirmarse
sobre α.
