# Preregistro — El techo de dimensión reproducible del cerebro humano (exp32)

**Sellado ANTES de abrir cualquier archivo de datos de COGITATE.** (La descarga del bundle
puede estar en curso; ningún archivo de señal se abre hasta que este documento esté commiteado
en el repo público.)

## La pregunta
En redes simuladas, la dimensión reproducible de la respuesta (R-dim) converge a un techo
finito al aumentar los trials (exp30). En humanos con TMS, crece hasta los 120 trials
disponibles sin techo visible (exp31, confirmada). COGITATE ofrece cientos de ensayos por
sujeto: **¿la R-dim humana satura dentro del rango medible, y a cuánto?** Nadie midió esto.

## Datos
COGITATE Data Release v1.2, bundle "iEEG Experiment 1 – BIDS, Sample" (CC BY 4.0).
Respuestas evocadas visuales, ancladas al ONSET del estímulo. Se usan TODOS los ensayos
(todas las categorías y duraciones pooled; las duraciones ≥0.5 s garantizan que la ventana
de respuesta 0–500 ms no pisa el offset). Orden cronológico; "primeros n válidos".

## Pipeline (congelado; enmiendas solo vía piloto, documentadas)
- Epochs: −600 a +600 ms del onset; baseline (−400, −50); respuesta (0, 500) ms.
- Canales: los iEEG del BIDS; se excluyen los marcados malos en la metadata si existe;
  sin re-referencia adicional si el BIDS ya trae referencia bipolar/limpia (decidir en piloto
  y documentar).
- Rechazo de trials: |z| robusto por canal > 6 en el epoch ⇒ trial fuera.
- R-dim: estimador del programa (4 splits, min_snr=1.1, max_var=99), idéntico a exp28/31.
- Grilla: n = 30, 60, 120, 240, y 480 si hay (n_max = mayor valor de la grilla ≤ n_válidos).
- Inclusión: sujetos con n_válidos ≥ 240. Mínimo 8 sujetos para correr los tests; si el
  sample trae menos, esto se degrada a piloto declarado y los tests esperan al dataset
  completo.
- **Piloto:** el primer sujeto por ID se usa para depurar el pipeline y QUEDA EXCLUIDO de
  los tests. Solo su estructura/señal puede mirarse antes de congelar detalles finos.

## Tests sellados (por sujeto: I_alto = R(n_max) − R(n_max/2); I_bajo = R(60) − R(30))
- **T1 (desaceleración):** Wilcoxon una cola I_alto < I_bajo, α=0.05.
- **T2 (crecimiento arriba):** Wilcoxon una cola I_alto > 0, α=0.05.
- Matriz de interpretación (fijada ahora):
  - T1 ✓ y T2 ✗ → **techo alcanzado** en el rango medido.
  - T1 ✓ y T2 ✓ → **acercándose al techo** (crecimiento desacelerando).
  - T1 ✗ y T2 ✓ → **sin techo detectable** hasta n_max.
  - T1 ✗ y T2 ✗ → señal insuficiente; se reporta sin interpretación direccional.
- **Descriptivo (no test):** ajuste por sujeto R(n) = D·(1 − e^(−n/n₀)); se reporta la
  mediana e IQR de D como "techo estimado con esta cobertura de electrodos". NOTA sellada:
  D depende de la cobertura (nº y ubicación de electrodos varía por paciente); es un techo
  POR REGISTRO, no "del cerebro" en abstracto — así se redactará siempre.

## Riesgos declarados
- iEEG de pacientes con epilepsia: actividad patológica puede inflar o deformar; el rechazo
  por amplitud mitiga parcialmente; se reporta sensibilidad excluyendo el 20% de trials más
  ruidosos.
- Evocados sensoriales ≠ perturbacionales (misma cautela sellada que en exp28/31).
- Categorías pooled: si la heterogeneidad de estímulos afectara R-dim, sesga contra techo
  limpio; análisis por categoría solo como secundario etiquetado.

## Sellado
Commit en https://github.com/nfgalindez-aiko/rdim (preregistrations/) antes de abrir datos.
