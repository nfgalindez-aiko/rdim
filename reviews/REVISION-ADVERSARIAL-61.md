> *Adversarial review report (in Spanish, the program's working language). Part of the program's five-step sealing procedure: before or upon deposit, each protocol is attacked by an independent reviewer whose default verdict is BROKEN. Published so the audit itself can be audited.*

# Revisión adversarial del sello 74b5407 (exp61b — ley de decaimiento caótico)

**Naturaleza de este documento.** Es el paso 3 de la regla del sello (revisión
adversarial, por defecto ROTO). Se ejecutó **retrospectivamente**: la regla nació
el 30/08/2026 después de que este sello se commiteara y corriera. El commit
74b5407 no contiene informe de revisión. Todos los números fueron **recomputados
mecánicamente** por el autor tras recibir el informe
(`10-auditorias/verificar_ataque_adversarial_61.py`,
`10-auditorias/sensibilidad61_pedestal.py`); ninguno se cita del informe sin
verificar.

**Qué NO es.** No es revisión externa ni peer review. Es un adversario interno:
otro contexto y otro rol, mismo linaje de modelo. El revisor declaró por su cuenta
una contaminación de su propia Fase A (leyó una bitácora que citaba el resultado
sellado antes de tiempo); sus ataques estaban formulados desde el código y los
datos quemados, pero corresponde decirlo. **Lección de procedimiento: la bitácora
no puede contener el veredicto, o debe existir una copia cortada en la línea del
sello, para que el revisor pueda ser ciego de verdad.**

---

## Veredicto del revisor: NO SELLABLE — falta la compuerta de calidad del blanco

## Ataques que FALLARON (el revisor los descartó él mismo)

- **La aceptación estratificada no induce la correlación.** La aceptación depende
  solo de λ, nunca de T_c. Nulo simulado: P(D1 pasa | nulo) < 5×10⁻⁴.
- **El pedestal del clip no fabrica la ley.** Ya estaba medido: share mediana 3.5%,
  no correlaciona con λ (+0.08, p=0.70), y corregirlo mueve la pendiente −0.605 →
  −0.570, *hacia* el valor sellado y lejos del −1.
- **No es artefacto de ρ.** Correlación parcial de ln T_c con ln λ controlando ln ρ:
  **r = −0.511 (p = 3.0×10⁻⁵)** — verificado. λ aporta información más allá de ρ.
- **No es una "cuerda entre dos mesetas".** Un mundo con exponente −1 exacto más un
  piso de 20–30 muestras sí produciría pendiente −0.53/−0.70 y pasaría ambas
  cláusulas — pero los datos vírgenes lo refutan: medianas por estrato 79/39/31/17
  sin piso, y el tramo superior es el más empinado.
- **La barra de D1 no está donde llega el ruido:** P(Spearman ≤ −0.50 | nulo)
  < 5×10⁻⁴ (≈3.9σ), y es una barra viva — mató el primer intento (−0.413).

## Ataques que PASARON

### 1. El blanco no se parece a sí mismo en el dominio del claim (defecto mayor)

El sello declara techo de confiabilidad **+0.976**, medido sobre una población que
abarca **orden→caos** (T_c de 3 a 300). El claim vive solo en λ ∈ (0.01, 0.30]. La
medición del propio programa *dentro de ese dominio* da **+0.103** sin compuerta
(dos redes patológicas de señal débil lo destruyen; 8/10 pares concuerdan bien) y
**+0.964** con la compuerta de pedestal.

Con techo 0.103 el límite de atenuación es √0.103 ≈ 0.32: **la barra de −0.50
estaba por encima del techo del dominio**, que es exactamente lo que la regla #2 de
la casa prohíbe. Atenuante honesto: el ruido del blanco *atenúa*, así que el pase de
D1 es conservador respecto de este defecto. Pero **el sello no puede afirmar que
cumplió la regla #2**.

### 2. Dos de las 60 "vidas coherentes" no miden vida coherente

Para un perfil dominado por pedestal plano con fracción *s*, el cuantil 80% da
T_c = 600·(0.8−(1−s))/s. Verificado:

| semilla | T_c sellado | share implicado | share medido | T_c en verdad independiente |
|---|---|---|---|---|
| 820352 | 434 | 0.72 | **0.78** | 449 (verdad A) / **5** (verdad B) |
| 820038 | 437 | 0.74 | — | ×11 la mediana de su estrato |

**El veredicto sellado gira sobre una sola red cuyo blanco no es reproducible**
(verificado):

| variante | Spearman | D1 | pendiente | IC95 |
|---|---|---|---|---|
| sellado, como cayó | −0.567 | **PASA** | −0.559 | [−0.795, −0.343] |
| 820352 leída con su verdad B | **−0.496** | **FALLA** | −0.455 | [−0.703, −0.210] |
| borrando T_c ≥ 400 (n=58) | −0.556 | PASA | −0.515 | [−0.735, −0.308] |
| borrando T_c ≥ 200 (n=53) | −0.508 | PASA | −0.386 | [−0.571, −0.199] |

La dirección sobrevive a todos los borrados; **el valor puntual del exponente no**:
rango honesto **−0.39 a −0.56**.

### 3. D2 es casi irrefutable como test de forma

El revisor predijo el SE antes de abrir el veredicto (0.111 contra 0.1158
realizado). La ventana sellada ±0.35 son **±3.0σ** alrededor del valor entrenado:
P(D2 falle | el entrenamiento es correcto) ≈ 0.3%. **D2 testeó reproducción del
propio estimador, no forma.** Contra una verdad −1 pura su potencia es ~70%.

### 4. La palanca es entre estratos, no de 60 redes independientes

Pendientes *dentro* de cada estrato (verificado): **+0.608, −0.520, −0.886,
+1.508**. Toda la información vive entre estratos (medianas 79/39/31/17). No es
anomalía dada la dispersión, pero describir el resultado como "60 redes"
sobreestima la independencia de la palanca.

## Preguntas donde el sello quedó BIEN

- **Legitimidad del segundo intento: SÍ, con margen.** El seguimiento se declaró en
  el preregistro del *primer* intento (83ae4da §5), antes de correrlo, y se
  re-declaró al fallar. Semillas sin solape. El fracaso está público. Familia de 2 →
  Bonferroni α=0.025; p observado 1.1×10⁻⁶ lo despeja por cuatro órdenes.
- **Reproducibilidad: SÍ.** El revisor replicó de forma independiente las 486
  semillas: 0 discrepancias de λ, 60/60 el mismo conjunto aceptado.
- **Costo: SÍ, con holgura** (~15 min en la netbook); el sello nunca presionó el
  diseño.
- **Zona gris declarada antes: SÍ** (matriz de interpretación con D1✓D2✗).

## Huecos de declaración detectados

- `exp61b.py` descarta en silencio redes con T_c no finito o P ≤ 0; el preregistro
  de exp46 sí declaraba esa exclusión, el de exp61 la perdió. **Disparó 0 veces**
  (verificado por replicación del muestreo): hueco real pero inerte.
- No se declara nada sobre T_c censurado o dominado por pedestal — justo la
  bifurcación que terminó importando.
- El pool de entrenamiento de exp61 **incluye las 19 caóticas del confirmatorio de
  exp46 que fallaron**: la ventana de D2 está centrada en una estimación derivada en
  parte de los datos del test fallido. Es legal (quemado) pero debe decirse.
- La factibilidad se midió con ρ ~ U(2.5, 4.0) mientras el diseño selló
  ρ ~ U(1.0, 4.0): **el muestreador sellado nunca se probó** antes de correr.

## Consecuencias aplicadas

Ver `10-auditorias/sensibilidad61_pedestal.py` (share de las 60 y D1/D2 con y sin
compuerta, post hoc declarado) y la sección correspondiente del preprint 10, que
reporta el sello como cayó y publica esta fragilidad como sensibilidad principal.
