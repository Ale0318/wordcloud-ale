import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="LexiCloud AI",
    page_icon="☁️",
    layout="wide"
)

# TÍTULO
st.title("☁️ LexiCloud AI")
st.subheader("Análisis de frecuencia léxica y visualización de nubes de palabras")

# SIDEBAR
st.sidebar.header("FUENTE DE TEXTO")

opcion = st.sidebar.radio(
    "Selecciona una opción:",
    ["✍️ Escribir texto", "📄 Texto de ejemplo"]
)

# TEXTO DE EJEMPLO
texto_ejemplo = """
La inteligencia artificial está transformando el mundo moderno.
Las interfaces multimodales permiten una interacción más natural
entre humanos y computadoras. El análisis de texto ayuda a identificar
palabras importantes y comprender grandes volúmenes de información.
"""

# INPUT DE TEXTO
if opcion == "✍️ Escribir texto":
    texto = st.sidebar.text_area(
        "Escribe o pega tu texto:",
        height=200
    )
else:
    texto = texto_ejemplo
    st.sidebar.success("Texto de ejemplo cargado")

# CONFIGURACIONES
st.sidebar.header("PROCESAMIENTO")

max_palabras = st.sidebar.slider(
    "Máximo de palabras",
    20,
    200,
    80
)

color_nube = st.sidebar.selectbox(
    "Paleta de colores",
    ["viridis", "plasma", "inferno", "magma", "cividis"]
)

fondo = st.sidebar.radio(
    "Color de fondo",
    ["white", "black"]
)

# CONTENIDO PRINCIPAL
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Acerca de esta herramienta")

    st.info("""
    Una nube de palabras representa visualmente la frecuencia de términos
    en un texto. Las palabras más frecuentes aparecen con mayor tamaño,
    permitiendo identificar temas importantes rápidamente.
    """)

    st.markdown("""
    ### Funciones principales

    ✅ Identificación de palabras frecuentes  
    ✅ Visualización interactiva  
    ✅ Personalización de colores  
    ✅ Procesamiento rápido de texto  
    ✅ Herramienta útil para análisis de contenido  
    """)

    st.header("Instrucciones")

    st.markdown("""
    1. Escribe o pega un texto en el panel lateral.  
    2. Configura el número máximo de palabras.  
    3. Selecciona colores y fondo.  
    4. Haz clic en el botón para generar la nube.  
    """)

with col2:
    st.header("Aplicaciones")

    st.success("📚 Análisis académico")
    st.success("📰 Noticias y artículos")
    st.success("💬 Comentarios y reseñas")
    st.success("📈 Marketing digital")
    st.success("🧠 Investigación de texto")

    st.header("Paletas disponibles")

    st.write("🎨 viridis")
    st.write("🎨 plasma")
    st.write("🎨 inferno")
    st.write("🎨 magma")
    st.write("🎨 cividis")

# BOTÓN
if st.button("☁️ GENERAR NUBE"):

    if texto.strip() == "":
        st.warning("Por favor ingresa un texto.")
    else:

        stopwords = set(STOPWORDS)

        nube = WordCloud(
            width=1000,
            height=500,
            background_color=fondo,
            colormap=color_nube,
            stopwords=stopwords,
            max_words=max_palabras
        ).generate(texto)

        st.header("Resultado")

        fig, ax = plt.subplots(figsize=(15, 7))

        ax.imshow(nube, interpolation="bilinear")
        ax.axis("off")

        st.pyplot(fig)

        st.success("Nube generada correctamente")
