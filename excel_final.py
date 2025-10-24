import pandas as pd
import re

# --- Archivos ---
archivo_base = "base_datos_energia_hdd.xlsx"
archivo_consumo = "innovation moderate/consumo-biomasa.xlsx"

# --- Leer archivos ---
base = pd.read_excel(archivo_base, engine="openpyxl")
consumo = pd.read_excel(archivo_consumo, engine="openpyxl")

# --- Normalizar columnas ---
consumo.columns = consumo.columns.str.strip()
consumo.rename(columns={
    "Código Instalación": "Instalacion",
    "Fecha de Descarga": "Fecha",
    "Cantidad Descargada [Tn]": "Cantidad_Tn"
}, inplace=True)

# --- Homogeneizar nombres de instalación ---
base["Instalacion"] = base["Instalacion"].astype(str).str.strip().str.upper()
consumo["Instalacion"] = consumo["Instalacion"].astype(str).str.strip().str.upper()

# --- Limpiar la columna de cantidad descargada ---
def limpiar_toneladas(x):
    if pd.isna(x):
        return None
    x = str(x).lower().replace(",", ".")
    x = re.sub(r"[^0-9.\-]", "", x)
    try:
        return float(x)
    except:
        return None

consumo["Cantidad_Tn"] = consumo["Cantidad_Tn"].apply(limpiar_toneladas)

# --- Procesar fechas ---
consumo["Fecha"] = pd.to_datetime(consumo["Fecha"], errors="coerce", dayfirst=True)
consumo["Date"] = consumo["Fecha"].dt.strftime("%d-%m")

# --- Promediar por instalación y día (multianual) ---
consumo_media = (
    consumo.groupby(["Instalacion", "Date"], as_index=False)["Cantidad_Tn"].mean()
)

# --- Fusionar ---
merged = pd.merge(base, consumo_media, on=["Instalacion", "Date"], how="left")

# --- Renombrar y ordenar columnas ---
merged.rename(columns={
    "EnergiaCaldera(MW-hr)": "Demanda",
    "Cantidad_Tn": "Consumo"
}, inplace=True)
merged = merged[["Date", "Instalacion", "HDD", "Demanda", "Consumo"]]

# --- Guardar ---
merged.to_excel("base_datos_energia_hdd_consumo.xlsx", index=False)

# --- Comprobación ---
print("✅ Archivo final generado: base_datos_energia_hdd_consumo.xlsx")
print("Filas con consumo disponible:", merged["Consumo"].notna().sum(), "de", len(merged))
print(merged.head(10))
