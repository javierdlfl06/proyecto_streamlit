import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la app
st.title("📊 Análisis de datos con Streamlit")

# Cargar datos
st.subheader("1️⃣ Cargar archivo CSV")
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Archivo cargado correctamente")

    # Mostrar primeras filas
    st.subheader("2️⃣ Vista previa del dataset")
    st.dataframe(df.head())

    # Seleccionar columna numérica
    st.subheader("3️⃣ Selecciona una columna numérica para graficar")
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if len(numeric_cols) > 0:
        selected_col = st.selectbox("Elige una columna", numeric_cols)

        # Graficar
        st.subheader(f"4️⃣ Histograma de {selected_col}")
        fig, ax = plt.subplots()
        ax.hist(df[selected_col].dropna(), bins=20, color="skyblue", edgecolor="black")
        st.pyplot(fig)
    else:
        st.warning("No hay columnas numéricas para graficar.")
else:
    st.info("👆 Sube un archivo CSV para empezar el análisis.")
