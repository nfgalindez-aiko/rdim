# PLANTILLA DE PREREGISTRO — copiar y llenar antes de sellar

*Nacida el 03/09/2026. Hasta hoy cada preregistro se escribía desde cero y la forma salía
por costumbre: pregunta, entrenamiento, protocolo, claims, matriz, honestidad. Esa forma
era buena pero no tenía casilleros para siete de las once reglas de la casa — las que se
chequean justo al sellar. Por eso la §7 del paper 8 se publicó con criterios que una
constante pasaba: nadie ignoró la regla, el formulario no tenía dónde escribirla.*

**Regla de uso: ninguna celda se deja vacía.** "NO APLICA, porque X" es una respuesta
válida y a veces la correcta. Vacío no lo es. Una celda vacía es la que después se
racionaliza.

**Qué hacer con esta plantilla:** copiarla a `prereg_expNN_<nombre>.md`, llenarla, pasarla
por el paso 3 (revisión adversarial, `10-auditorias/PLANTILLA-REVISION-ADVERSARIAL.md`),
corregir lo que el revisor rompa, volver a revisión si el veredicto fue NO SELLABLE, y
recién entonces commitear protocolo + informe juntos.

---

## 1. Pregunta

Qué se pregunta, en una oración, sin jerga.

## 2. Qué resultado me haría abandonar
*(pregunta 1 del paso 3)*

Explícito. Si no hay un resultado que mate la hipótesis, la pregunta está rota y no se
sella.

## 3. Entrenamiento revelado

Todo lo que se miró, sobre qué datos quemados, y con qué semillas. El rango virgen no se
solapa con esto.

## 4. Techo de confiabilidad del blanco
*(reglas 2 y 4, y pregunta 3 del paso 3)*

- ¿Cuánto se parece el blanco a sí mismo? Número medido, con su script archivado.
- **¿En qué población se midió?** Tiene que contener el dominio donde se firma el claim.
  Un techo medido en una población más ancha, donde ordenar es fácil, no vale.
- ¿La barra queda por debajo del techo, con margen? Cuánto.
- Si el techo es de n chico, decirlo: con diez unidades y sin compuerta de calidad, un
  techo no acota nada.

## 5. El instrumento contra verdad conocida
*(regla 7)*

- ¿Se le inyectó una cantidad conocida y se le exigió el número? Resultado.
- ¿Su piso bajo el nulo? ¿Su dependencia del SNR?
- Si el instrumento no está certificado, **no corre confirmatorio**. Se dice acá y se
  para.

## 6. El nulo de CADA criterio
*(regla 5, y pregunta 2 del paso 3)*

Para cada criterio, dos columnas, las dos computadas antes de sellar:

| criterio | (a) qué da bajo ruido/permutación | (b) qué da el PREDICTOR TRIVIAL |
|---|---|---|

El predictor trivial es el tonto más obvio: una constante, una sola variable leída de los
datos, la condición sin el mecanismo propuesto. **Si el predictor tonto pasa la barra, el
criterio no puede refutar y el sello es decorativo.** Se rediseña la barra o se retira el
criterio.

## 7. La explicación trivial
*(regla 8)*

Antes de interpretar cualquier diferencia entre condiciones: amplitud, cantidad de
ensayos, SNR, cobertura. ¿Cuál se mide y cómo se iguala? Si la diferencia no sobrevive
con eso igualado, es de la explicación trivial y así se reporta.

## 8. Grano y potencia
*(regla 1)*

- n por celda (mínimo 30, o justificar por qué menos).
- ¿El grano del claim es más grueso que el ruido del entrenamiento?
- Potencia contra el tamaño de efecto que se espera. Un test que no puede alcanzar alfa
  con ese n se declara descriptivo ACÁ, no después.

## 9. De dónde salen los sujetos, redes o sesiones
*(regla 3)*

- Cómo se eligen.
- Si son "los que sobraron" de otro experimento: **por qué sobraron.** Esa pregunta ha
  cambiado veredictos.

## 10. Protocolo confirmatorio: UNA corrida

Pipeline congelado, con su commit. Y **cada bifurcación declarada** *(pregunta 5 del
paso 3, la que más sellos arruina)*:

- semillas (regla exacta, no "una semilla fija")
- criterios de exclusión, y qué se hace con los faltantes
- qué pasa si algo no converge
- permutaciones: cuántas, con qué semilla
- criterio de corte
- compuertas de calidad: cuáles, con qué umbral, **congeladas acá o declaradas post-hoc**

## 11. Claims a sellar, con las barras CONGELADAS

| id | enunciado exacto que se va a imprimir en el paper | barra | valor de entrenamiento |
|---|---|---|---|

**El enunciado tiene que ser el que después se publica.** Si el juez computa "mayor o
igual" y el paper va a decir "mayor", son dos claims distintos y hay que sellar el que se
va a imprimir.

## 12. ¿Un desconocido computaría mi número igual?
*(pregunta 4 del paso 3)*

Con el protocolo solo, sin preguntarme nada. Si la métrica admite dos lecturas, no está
sellada.

## 13. Matriz de interpretación, con la zona gris
*(pregunta 6 del paso 3)*

Todas las celdas publicables, incluidas las incómodas. **Qué pasa si cae en el medio,
declarado ANTES.** Si un criterio está condicionado a otro, decirlo: un criterio
secundario cuyo primario murió no se lee como si nada.

## 14. ¿Entra en la máquina?
*(pregunta 7 del paso 3)*

Diez repeticiones de prueba, medir, multiplicar. Costo estimado. Un sello que no termina
obliga a bajar la vara después de ver el resultado.

## 15. ¿Ya se miraron los datos?
*(pregunta 8 del paso 3, con el matiz de la casa)*

Entrenar sobre semillas quemadas es legítimo y obligatorio. Lo prohibido: que el rango
virgen se solape, que las barras se elijan después de ver resultados vírgenes, o que se
mire el veredicto antes de fijar el juez. Declarar cuál es cada cosa.

## 16. Notas de honestidad

Lo que no se sabe, lo que se asume, lo que se hereda de otro protocolo.

---

## Informe del paso 3 (lo llena el revisor adversarial, no el autor)

Va en el mismo commit que este protocolo. Veredicto: **SELLABLE** o
**NO SELLABLE — falta X**. Si es NO SELLABLE, se corrige y **vuelve a revisión** con el
informe anterior a la vista; nunca se commitea con una nota que diga "lo consideré".
