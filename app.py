import streamlit as st

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="WordCloud Studio",
    layout="wide"
)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("☁️ **WORDCLOUD STUDIO**")

    st.divider()

    st.subheader("FUENTE DE TEXTO")

    opcion = st.radio(
        "",
        ["✍️ Escribir / Pegar", "📁 Subir archivo"]
    )

    texto = st.text_area(
        "Texto:",
        placeholder="Pega aquí un artículo,\nreseña, discurso,\nencuesta..."
    )

    st.button("›  Cargar texto de ejemplo")

    st.divider()

    st.subheader("PROCESAMIENTO")

    idioma = st.selectbox(
        "Stopwords:",
        ["Español", "Inglés"]
    )

    st.slider(
        "Longitud mínima de palabra",
        1,
        10,
        3
    )

    st.text_input(
        "Excluir palabras adicionales:",
        placeholder="ej: también, así, aquí"
    )

    st.divider()

    st.subheader("APARIENCIA")

    paleta = st.selectbox(
        "Paleta:",
        [
            "Escala de grises",
            "Azul corporativo",
            "Verde institucional",
            "Gris azulado",
            "Terracota",
            "Índigo profundo",
            "Monocromático negro"
        ]
    )

    fondo = st.radio(
        "Fondo:",
        ["Blanco", "Negro"],
        horizontal=True
    )

    forma = st.selectbox(
        "Forma:",
        ["Rectángulo", "Círculo"]
    )

    st.slider(
        "Máximo de palabras:",
        10,
        200,
        80
    )

    st.divider()

    st.button("GENERAR NUBE ↗", use_container_width=True)

# ---------------- CONTENIDO PRINCIPAL ----------------

st.markdown("""
<div style="
padding:30px;
border-radius:12px;
border-left:6px solid #1f2937;
background-color:white;
margin-bottom:20px;
">
<h1 style="margin:0;">☁️ WordCloud Studio</h1>
<p style="font-size:22px;">
Análisis de frecuencia léxica y visualización de nubes de palabras
</p>
</div>
""", unsafe_allow_html=True)

# CAJAS VACÍAS SUPERIORES

col1, col2 = st.columns(2)

with col1:
    st.container(height=60, border=True)

with col2:
    st.container(height=60, border=True)

st.write("")

# COLUMNAS PRINCIPALES

izq, der = st.columns([2,1])

# ---------------- IZQUIERDA ----------------

with izq:

    st.header("Acerca de esta herramienta")

    st.write("""
Una nube de palabras representa visualmente la frecuencia de términos en un texto:
las palabras más frecuentes aparecen con mayor tamaño, permitiendo identificar
los temas centrales de un corpus de manera intuitiva.
""")

    with st.container(border=True):
        st.markdown("""
### 📊 Análisis de frecuencia
Identifica los términos dominantes de cualquier corpus textual.
""")

    with st.container(border=True):
        st.markdown("""
### 🔎 Filtrado inteligente
Elimina palabras vacías (*stopwords*) en español e inglés.
""")

    with st.container(border=True):
        st.markdown("""
### 🎨 Personalización visual
Selecciona paleta, forma y densidad de la nube.
""")

    with st.container(border=True):
        st.markdown("""
### ⬇️ Exportación
Descarga la imagen en alta resolución y la tabla de frecuencias en CSV.
""")

    st.header("Instrucciones")

    st.markdown("""
1. Ingresa o sube un texto en el panel lateral.

2. Configura el idioma de *stopwords*, paleta y número de palabras.

3. Haz clic en **GENERAR NUBE ↗**.

4. Descarga la imagen PNG o la tabla CSV.
""")

# ---------------- DERECHA ----------------

with der:

    st.header("Aplicaciones frecuentes")

    st.button("📰 Análisis de prensa y noticias")
    st.button("📋 Resultados de encuestas abiertas")
    st.button("💬 Reseñas y comentarios de clientes")
    st.button("🎓 Análisis de textos académicos")
    st.button("📁 Discursos y documentos políticos")
    st.button("📊 Estudios literarios y de corpus")
    st.button("📈 Informes de inteligencia de negocio")

    st.write("")

    st.container(height=60, border=True)

    st.write("")

    st.header("Paletas disponibles")

    st.write("Escala de grises")
    st.write("Azul corporativo")
    st.write("Verde institucional")
    st.write("Gris azulado")
    st.write("Terracota")
    st.write("Índigo profundo")
    st.write("Monocromático negro")
