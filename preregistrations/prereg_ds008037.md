# Preregistro — ds008037 (Biabani & Rogasch 2026, OpenNeuro, CC0)
## Congelado 2026-08-25 ANTES de analizar (solo sub-001 se usará para depurar el pipeline,
## y queda EXCLUIDO del test confirmatorio)

## Por qué este dataset
EEG de reposo real + TMS-EEG crudo trial-level (4 sitios, hombro control) por sujeto.
Resuelve las 3 limitaciones del hallazgo exploratorio (exp18/19, dataset Monash procesado):
baseline promediado como proxy de reposo, sin trials (XV inaplicable), n_trials desconocido.

## Hipótesis confirmatoria H1 (dirección comprometida por exp18/19)
Entre sujetos: **pendiente espectral 1/f del EEG de reposo** (más plana) → **mayor PCIst-XV**
de la respuesta evocada por TMS prefrontal. Spearman una cola (positiva), α=0.05.

## Variables y pipeline (congelados)
- Muestra: primeros 30 sujetos por orden de ID (excluyendo sub-001, piloto). Si un sujeto
  falla el pipeline (archivos corruptos, <60 trials válidos, >12 canales malos) se reemplaza
  por el siguiente ID y se registra.
- X (pendiente): rest EEG → 2-90 Hz bandpass, notch 50 Hz, canales malos por z-score robusto
  de varianza >4 (interpolados), re-ref promedio, Welch 4 s, ajuste log-log 3–40 Hz
  excluyendo 8–13 Hz, promedio de canales.
- Y (complejidad): TMS-EEG prefrontal → epochs −1000..+999 ms alrededor de cada pulso
  (events.tsv), ventana −5..+15 ms interpolada linealmente (artefacto TMS), 1–90 Hz, notch,
  downsample a 725 Hz, rechazo de trials con amplitud absoluta >150 µV post-interpolación,
  **ecualización: exactamente 60 trials por sujeto (los primeros 60 válidos)**, re-ref promedio,
  PCIst-XV (parámetros de los papers; 4 splits; baseline −400/−50, respuesta 0/300 ms).
- Confundidores controlados por diseño: n_trials idéntico entre sujetos; y se reporta
  Spearman(X, nº de trials rechazados) como chequeo.
- Secundarias (exploratorias): duración de respuesta → XV; pendiente → XV en los otros sitios;
  XV hombro vs prefrontal pareado; PCIst estándar vs XV en trial-level real (para paper 1).

## Criterio
H1 confirmada si ρ>0 con p(una cola)<0.05 en los 30 sujetos. Se publica el resultado sea cual sea.

## ENMIENDA (2026-08-25, tras piloto sub-001, ANTES de todo computo confirmatorio)
El piloto mostro que el umbral de rechazo congelado (150 uV) es irreal para trials crudos sin ICA (mediana de max-amp 190 uV, sin outliers: 119/120 trials < 300 uV). Se enmienda: rechazo >300 uV; ventana de interpolacion TMS -5..+20 ms. sub-001 queda excluido del test confirmatorio como estaba previsto.
