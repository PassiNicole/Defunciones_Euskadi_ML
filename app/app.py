import streamlit as st
import pandas as pd
import streamlit.components.v1 as c
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Defunciones en Euskadi",
                   page_icon=":skull:")

# Sidebar para la navegación
seleccion = st.sidebar.selectbox("Selecciona menú", ["Inicio", "EDA", "Filtros"])

# Menú "Home"
if seleccion == "Inicio":
    st.title("Defunciones en Euskadi")
    
    with st.expander("¿Qué es esta aplicación?"):
        st.write("""
            Esta aplicación permite explorar los datos de defunciones en Euskadi, 
            analizando las principales causas de muerte, territorios históricos 
            y otros factores relevantes para facilitar la comprensión de los datos.
        """)

# Menú "EDA" (Análisis exploratorio de datos)
elif seleccion == "EDA":
    st.title("Análisis Exploratorio de Datos (EDA)")
    
    df = pd.read_csv("../data/data_defunciones_procesado.csv", encoding='ISO-8859-1', skiprows=1)

    # Mostrar las primeras filas del DataFrame
    st.write("Visualización de los datos:")
    st.dataframe(df.head())

    # Gráfico exploratorio (por ejemplo, defunciones por año)
    st.write("Gráfico de defunciones por año")
    defunciones_por_año = df.groupby("rango1", 'rango2', 'rango3')["Defunciones"].sum()
    st.bar_chart(defunciones_por_año)

    # Incluir más gráficos exploratorios si es necesario
    st.write("Distribución de defunciones por grandes grupos CIE-10")
    defunciones_por_territorio = df.groupby("grandes grupos CIE-10")["Defunciones"].sum()
    st.bar_chart(defunciones_por_territorio)
