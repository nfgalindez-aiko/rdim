> *Adversarial review report (in Spanish, the program's working language). Part of the program's five-step sealing procedure: before or upon deposit, each protocol is attacked by an independent reviewer whose default verdict is BROKEN. Published so the audit itself can be audited.*

# Revisión paranoica del proyecto — 31/08/2026

Pedido: revisar el proyecto entero, cosa por cosa, con más escepticismo sobre lo que
podría ser **letal** (no lo que se arregla con una nota). Se buscó activamente
evidencia de que el programa fuera inválido. **No se encontró.** Lo que sigue son los
cuatro chequeos de nivel letal, ninguno de los cuales se había hecho nunca, más el
cierre de un agujero estructural.

---

## LETAL 1 — ¿Los sellos son reales, o decoración?

**La pregunta:** si un archivo de resultados confirmatorios existiera ANTES del commit
que lo selló, el programa no tendría preregistro: tendría un relato.

**El chequeo** (`verificar_integridad_sellos.py`): para los 27 protocolos sellados, se
comparó la fecha del commit del preregistro en el repo público contra la fecha de
creación del archivo de resultados confirmatorios.

**Resultado: 27 de 27 posteriores al sello. CERO violaciones.** Las demoras van de 6
minutos a 1.7 horas — consistentes con "sellé y corrí".

*Honestidad sobre el método:* los mtime del filesystem son la única evidencia temporal
para `03-experimentos` (su repo git nació el 30/08). Un mtime **anterior** al sello
habría sido prueba de contaminación; uno posterior es consistente con el sello, no una
prueba criptográfica. La evidencia fuerte es el commit público, que sí tiene timestamp
de GitHub.

## LETAL 2 — ¿La máquina de simulación mide lo que dice?

**La pregunta:** todo el brazo simulado (papers 2, 4, 8, 9, 10) descansa en tres
funciones que nunca fueron validadas contra una verdad conocida. Si λ está mal medido,
todo lo simulado es ruido.

**El chequeo** (`verificar_motor_simulacion.py`), contra verdad analítica: para una
dinámica lineal, el exponente de Lyapunov es exactamente log(radio espectral).

- `make_W` clava el radio espectral pedido con error **3×10⁻¹⁴**.
- El método de trayectorias recupera log(ρ) con error **1.5×10⁻⁵** en todo el rango.
- `lyapunov_esn` coincide con la verdad donde tanh es lineal (error ≤ 0.012).
- Donde tanh no es lineal, la brecha respecto de log(ρ) **crece monótonamente con el
  drive**: −0.03 a ρ=1.0 → −1.16 a ρ=4.0. Esa brecha ES la saturación. **La ley de
  saturación del programa aparece sola en la medición de λ**, por un camino
  independiente de todos los protocolos.

*Dos intentos previos fallaron por errores míos* (salir del régimen lineal; cancelación
de punto flotante) y quedan documentados en el script: el motor no falló, mi test sí.

## LETAL 3 — ¿Contaminación de semillas?

**La pregunta:** si dos confirmatorios comparten redes, sus veredictos no son
independientes y las "confirmaciones cruzadas" del programa son ecos del mismo dato.

**El chequeo** (`verificar_semillas.py`): se extrajeron todas las semillas de todos los
jsonl de resultados del proyecto (39 archivos).

- Hay 1386 semillas compartidas entre familias — **todas** son entrenamiento sobre
  datos quemados, que es la disciplina declarada (exp54 entrena sobre exp51/exp53 ya
  corridos; exp64 sobre exp61b; exp46 sobre exp45; etc.).
- **Entre los 18 confirmatorios sellados: NINGÚN par comparte una sola semilla.**
  Independencia total.

## LETAL 4 — ¿El corpus se contradice a sí mismo?

**El chequeo** (`verificar_coherencia_papers.py`): un mismo hecho citado en varios
papers debe llevar el mismo número, las correcciones deben estar propagadas, y cada DOI
citado debe existir.

Encontró **una** inconsistencia (el paper 8 citaba la disociación gateada como 0.91 en
vez de 0.912), corregida. **Veredicto: corpus coherente.**

---

## El agujero estructural que se cerró

Los papers **1, 2 y 3 no tenían verificador mecánico** — los tres más viejos del
programa, y nunca nadie recomputó sus números. Ahora lo tienen, y al escribirlos
salieron a la luz mecánicamente los errores que la revisión adversarial había
encontrado a mano:

| paper | lo que decía | lo que dicen los datos |
|---|---|---|
| 1 | "XV remains ≤ 12 everywhere" | máximo real **23.1**; 13 de 240 superan 12 |
| 1 | "identical to one decimal" | es idéntico a **precisión de máquina** (1.1×10⁻¹³): se subestimaba |
| 1 | "statistically indistinguishable" | no existe test; n=3 redes por celda |
| 1 | "decae en 4–16 pasos" | 4–**34** por mediana de ρ |
| 2 | "máximo en \|λ\|<0.01 (mediana 94) ... p=1.8×10⁻³" | el p sellado es de la banda [−0.05,0), cuya mediana es **47.5**; la de 94.4 es post-hoc |
| 2 | "n = 92 networks" | el test usa **n = 57** (el propio cuerpo ya lo decía) |
| 2 | "mediana R-dim 1.4" | esa banda tiene **una sola red** |
| 3 | "la asociación sobrevivió al control (+0.33, p=0.0012)" | solo en la réplica; en descubrimiento **+0.21, p=0.27** |
| 3 | "estadísticamente indistinguible" (sham) | p=0.095 sin test de equivalencia; 48 pares son 12 sujetos |

Los tres papers fueron corregidos y ahora **pasan sus propios verificadores**.

---

## Estado final

`AUDITAR_TODO.py` pasó de 6 verificadores a **18**, y ahora incluye los cuatro de
integridad estructural, que son los que ningún verificador de números puede reemplazar.

**AUDITORÍA TOTAL: TODO EL PROYECTO VERIFICADO** (18/18).

### La lectura honesta
Se buscó activamente el modo de falla que mataría el programa —sellos falsos, motor
roto, semillas contaminadas, corpus contradictorio— y no está. Lo que apareció en la
auditoría del día son **claims sobrevendidos y un confundidor no reportado**: cosas que
se corrigen con una versión nueva, no cosas que invalidan un programa.

El instrumento mide lo que dice medir, los sellos son anteriores a sus datos, los
confirmatorios son independientes, y el motor reproduce la verdad analítica. Eso es el
esqueleto, y está sano.
