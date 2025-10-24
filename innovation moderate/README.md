# Innovathon MODERATE 2025

Este repositorio contiene datos relacionados con el consumo energético, la producción de energía y los grados día de calefacción (HDD - Heating Degree Days) para el análisis de eficiencia energética.

## Contenido del Repositorio

### 📊 Archivos de Datos Principales

#### `consumo-biomasa.xlsx`
Archivo con datos de consumo de biomasa.

### 📁 Directorio: `hdd-anual/`
Contiene archivos con valores diarios de grados día (Degree Days) para los años 2019-2025, calculados para las coordenadas 40.9701039, -5.6635397.

**Archivos incluidos:**
- `2019-degree-days-40.9701039-5.6635397-20190101-20191231-daily-values.xlsx`
- `2020-degree-days-40.9701039-5.6635397-20200101-20201231-daily-values.xlsx`
- `2021-degree-days-40.9701039-5.6635397-20210101-20211231-daily-values.xlsx`
- `2022-degree-days-40.9701039-5.6635397-20220101-20221231-daily-values.xlsx`
- `2023-degree-days-40.9701039-5.6635397-20230101-20231231-daily-values.xlsx`
- `2024-degree-days-40.9701039-5.6635397-20240101-20241231-daily-values.xlsx`
- `2025-degree-days-40.9701039-5.6635397-20250101-20251013-daily-values.xlsx` (parcial)

### 📁 Directorio: `produccion-energetica/`
Contiene archivos Excel con datos de producción energética de diferentes medidores identificados con códigos M.

**Archivos incluidos:**
- `m218807.xlsx`
- `m218820-1.xlsx`, `m218820-2.xlsx`
- `m220825-1.xlsx`, `m220825-2.xlsx`
- `m220850.xlsx`
- `m220853.xlsx`
- `m220854.xlsx`
- `m220860.xlsx`
- `m222805.xlsx`
- `m222813.xlsx`
- `m222819.xlsx`
- `m222820.xlsx`
- `m222821.xlsx`
- `m222824.xlsx`
- `m223296.xlsx`

## 📄 Documentación Técnica

### API AEMET
**Archivo:** `api-aemet.pdf`

**Contenido:**
El documento contiene la referencia al endpoint de la API de AEMET (Agencia Estatal de Meteorología) para obtener datos meteorológicos del municipio con código 37274:

```
https://www.aemet.es/xml/municipios/localidad_37274.xml
```

Esta API proporciona datos meteorológicos oficiales que pueden utilizarse para el cálculo de grados día y análisis energético.

### Fórmula HDD (Heating Degree Days)
**Archivo:** `hdd-formula.pdf`

**Contenido:**
El documento describe la metodología para calcular los grados día de calefacación (HDD), que es una medida utilizada para estimar la demanda de energía para calefacción.

#### Fórmula Base
```
Tavg = (Tmax + Tmin) / 2
Tbase = 18°C
```

#### Casos de Cálculo

| Caso | Condición | Fórmula HDD |
|------|-----------|-------------|
| 1 | Tmax < Tbase (día uniformemente frío) | HDD = Tbase - Tavg |
| 2 | Tavg < Tbase < Tmax (día mayormente frío) | HDD = [(Tbase - Tmin)/2] - [(Tmax - Tbase)/4] |
| 3 | Tmin < Tbase < Tavg (día mayormente cálido) | HDD = (Tbase - Tmin)/4 |
| 4 | Tmin ≥ Tbase (día uniformemente cálido) | No se requiere calefacción, HDD = 0 |

**Donde:**
- `Tmax`: Temperatura máxima del día
- `Tmin`: Temperatura mínima del día
- `Tavg`: Temperatura media del día
- `Tbase`: Temperatura base de referencia (18°C)

Los grados día de calefacción son un indicador clave para:
- Estimar el consumo energético de calefacción
- Comparar diferentes períodos o ubicaciones
- Planificar la demanda energética
- Evaluar la eficiencia de sistemas de calefacción
