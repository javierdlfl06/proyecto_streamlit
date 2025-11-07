import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(
    page_title="Análisis de Datos",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
        font-family: 'Segoe UI';
    }
    .stMetric {
        background-color: #262730;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- TÍTULO PRINCIPAL ---
st.title("📊 Dashboard de Análisis de Datos")

# --- CARGA DE ARCHIVO ---
st.sidebar.header("📁 Cargar archivo CSV")
archivo = st.sidebar.file_uploader("Sube un archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)
    st.sidebar.success("✅ Archivo cargado correctamente")

    # --- VISTA PREVIA ---
    st.subheader("👀 Vista previa del dataset")
    st.dataframe(df.head())

    # --- SELECCIÓN DE COLUMNA ---
    columnas_numericas = df.select_dtypes(include=np.number).columns.tolist()
    if columnas_numericas:
        columna = st.selectbox("Selecciona una columna numérica para analizar", columnas_numericas)

        # --- SLIDER DE RANGO ---
        min_val, max_val = float(df[columna].min()), float(df[columna].max())
        rango = st.slider(
            f"Filtra los valores de {columna}",
            min_val,
            max_val,
            (min_val, max_val)
        )

        df_filtrado = df[(df[columna] >= rango[0]) & (df[columna] <= rango[1])]

        # --- KPIs / MÉTRICAS ---
        st.markdown("### 📈 Indicadores Clave (KPI)")
        col1, col2, col3 = st.columns(3)
        col1.metric("Valor mínimo", f"{df_filtrado[columna].min():.2f}")
        col2.metric("Promedio", f"{df_filtrado[columna].mean():.2f}")
        col3.metric("Valor máximo", f"{df_filtrado[columna].max():.2f}")

        # --- GRÁFICO ---
        st.markdown("### 📊 Distribución de valores")
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.hist(df_filtrado[columna], bins=12, color="#29B5E8", edgecolor="white")
        ax.set_xlabel(columna)
        ax.set_ylabel("Frecuencia")
        ax.set_facecolor("#0E1117")
        st.pyplot(fig)

    else:
        st.warning("⚠️ No hay columnas numéricas para graficar.")
else:
    st.info("⬆️ Sube un archivo CSV desde la barra lateral para comenzar.")
