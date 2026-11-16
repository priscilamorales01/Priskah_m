import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

# 1. Configurar la página
st.set_page_config(
    page_title="Diagnóstico | Priskah_m",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ESTÉTICA LUXURY SPA (CSS AVANZADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;1,400&display=swap');

    /* Fondo general y tipografía */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #F9F7F3 0%, #F1ECE3 100%);
        font-family: 'Montserrat', sans-serif;
        color: #2C362B;
    }

    /* Ocultar barra superior y pie de página de Streamlit */
    [data-testid="stHeader"], footer, #MainMenu {
        visibility: hidden;
        height: 0px;
    }

    /* Contenedor principal */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 680px;
    }

    /* Títulos editoriales */
    .brand-title {
        font-family: 'Playfair Display', serif;
        font-size: 42px;
        font-weight: 600;
        color: #2C3A2E;
        text-align: center;
        letter-spacing: 1px;
        margin-top: 10px;
        margin-bottom: 4px;
    }
    .brand-subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 13px;
        font-weight: 400;
        color: #7A746B;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2.5px;
        margin-bottom: 25px;
    }
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        color: #2C3A2E;
        margin-bottom: 4px;
    }
    .section-desc {
        font-size: 13px;
        color: #7A746B;
        margin-bottom: 16px;
    }

    /* Estilo de tarjetas (contenedores con borde) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF;
        border-radius: 18px !important;
        border: 1px solid #EAE4D8 !important;
        box-shadow: 0 10px 30px rgba(44, 58, 46, 0.05) !important;
        padding: 24px 26px !important;
        margin-bottom: 20px !important;
    }

    /* Inputs de texto */
    .stTextInput label {
        font-size: 13px !important;
        font-weight: 500 !important;
        color: #4A554B !important;
    }
    .stTextInput > div > div > input {
        background-color: #FAF9F6 !important;
        border-radius: 10px !important;
        border: 1px solid #DDD6C8 !important;
        padding: 12px 14px !important;
        font-size: 14px !important;
        color: #2C362B !important;
        transition: all 0.25s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #C5A880 !important;
        box-shadow: 0 0 0 2px rgba(197, 168, 128, 0.2) !important;
        background-color: #FFFFFF !important;
    }

    /* Opciones de Radio estilo tarjetas interactivas */
    div[role="radiogroup"] > label {
        background-color: #FAF9F6;
        border: 1px solid #EAE4D8;
        border-radius: 12px;
        padding: 14px 16px !important;
        margin-bottom: 10px !important;
        transition: all 0.25s ease;
        cursor: pointer;
    }
    div[role="radiogroup"] > label:hover {
        border-color: #C5A880;
        background-color: #FFFFFF;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(197, 168, 128, 0.12);
    }
    div[role="radiogroup"] p {
        font-size: 14px !important;
        color: #2C362B !important;
        line-height: 1.4;
    }

    /* Botón principal */
    .stButton > button {
        background: linear-gradient(135deg, #3B4D3E 0%, #2C3A2E 100%) !important;
        color: #FAF8F5 !important;
        border-radius: 12px !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 500 !important;
        letter-spacing: 0.8px !important;
        width: 100%;
        padding: 0.9rem 1.5rem !important;
        font-size: 15px !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(44, 58, 46, 0.18) !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 24px rgba(44, 58, 46, 0.25) !important;
        background: linear-gradient(135deg, #2C3A2E 0%, #1E2820 100%) !important;
    }

    /* Tarjeta de Resultado de Diagnóstico */
    .result-card {
        background: linear-gradient(145deg, #FFFFFF 0%, #FBF9F5 100%);
        border: 1px solid #DFD3C0;
        border-left: 5px solid #C5A880;
        border-radius: 16px;
        padding: 26px;
        margin-top: 18px;
        margin-bottom: 22px;
        box-shadow: 0 12px 30px rgba(44, 58, 46, 0.07);
    }
    .result-badge {
        display: inline-block;
        background-color: #F2ECE1;
        color: #8C734B;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        padding: 5px 12px;
        border-radius: 20px;
        margin-bottom: 12px;
    }
    .result-title {
        font-family: 'Playfair Display', serif;
        font-size: 26px;
        color: #2C3A2E;
        margin-bottom: 10px;
    }
    .result-desc {
        font-size: 14.5px;
        color: #555D54;
        line-height: 1.65;
        margin-bottom: 0;
    }

    /* Botón de WhatsApp */
    .wa-btn {
        background: linear-gradient(135deg, #25D366 0%, #1DA851 100%);
        color: white !important;
        padding: 15px 32px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 15px;
        letter-spacing: 0.4px;
        display: inline-block;
        box-shadow: 0 8px 20px rgba(37, 211, 102, 0.28);
        transition: all 0.3s ease;
    }
    .wa-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 25px rgba(37, 211, 102, 0.38);
    }

    /* Línea divisora elegante */
    .gold-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #D8CBB8, transparent);
        margin: 18px 0 28px 0;
        border: none;
    }

    /* Imagen del logo redondeada */
    [data-testid="stImage"] img {
        border-radius: 50%;
        box-shadow: 0 8px 24px rgba(44, 58, 46, 0.12);
        border: 3px solid #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO Y LOGO ---
col1, col2, col3 = st.columns([1.3, 1, 1.3])
with col2:
    try:
        st.image("LOGO.jpeg", use_container_width=True)
    except:
        pass

st.markdown("<div class='brand-title'>Priskah_m</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-subtitle'>Bienestar Integral • Cuidado Capilar • Masajes</div>", unsafe_allow_html=True)
st.markdown("<hr class='gold-divider'>", unsafe_allow_html=True)

# --- SECCIÓN 1: DATOS PERSONALES ---
with st.container(border=True):
    st.markdown("<div class='section-title'>Tus Datos</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-desc'>Completa tu información para generar tu diagnóstico personalizado.</div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        nombre = st.text_input("Nombre completo", placeholder="Ej: María José Pérez")
    with c2:
        telefono = st.text_input("Número de WhatsApp", placeholder="Ej: 60218458")

# --- SECCIÓN 2: CATEGORÍA ---
with st.container(border=True):
    st.markdown("<div class='section-title'>¿Qué área deseas consentir hoy?</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-desc'>Elige la experiencia que mejor se adapte a lo que buscas.</div>", unsafe_allow_html=True)
    
    categoria = st.radio(
        "Categoría",
        ["💆‍♀️ Masajes y Bienestar Corporal", "✨ Cuidado Capilar Avanzado"],
        label_visibility="collapsed"
    )

# --- SECCIÓN 3: DIAGNÓSTICO ESPECÍFICO ---
with st.container(border=True):
    if "Masajes" in categoria:
        st.markdown("<div class='section-title'>¿Cuál es tu objetivo o molestia principal?</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Selecciona la opción que mejor describa cómo se siente tu cuerpo hoy.</div>", unsafe_allow_html=True)
        opcion = st.radio(
            "Enfoque corporal",
            [
                "Dolor intenso de espalda, cuello, hombros o nudos profundos (Descontracturante)",
                "Nivel alto de estrés, ansiedad, insomnio y fatiga mental (Relajante)",
                "Piernas cansadas, hinchadas, mala circulación o retención de líquidos (Drenaje / Retorno Venoso)",
                "Sobrecarga muscular por entrenamiento o deporte (Deportivo)",
                "Reafirmar, moldear figura o activar metabolismo local (Reductivo / Modelado)"
            ],
            label_visibility="collapsed"
        )
    else:
        st.markdown("<div class='section-title'>¿Cómo se encuentra tu cabello actualmente?</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Selecciona tu necesidad capilar principal.</div>", unsafe_allow_html=True)
        opcion = st.radio(
            "Necesidad capilar",
            [
                "Cabello muy seco, maltratado por tintes/decoloraciones y frizz extremo (Hidratación Profunda)",
                "Busco brillo espejo, nutrición profunda y efecto liso perfecto (Nanoqueratina)",
                "Cuero cabelludo graso, pesado o con acumulación de residuos (Detox Purificante)",
                "Caída frecuente o necesidad de estimular crecimiento nuevo (Anticaída / Raíz)"
            ],
            label_visibility="collapsed"
        )

# --- BOTÓN DE ACCIÓN ---
if st.button("✨ Descubrir mi Tratamiento Ideal"):
    if nombre.strip() == "" or telefono.strip() == "":
        st.warning("⚠️ Por favor, ingresa tu nombre y número de WhatsApp para ver tu diagnóstico.")
    else:
        # Lógica de recomendaciones
        if "Masajes" in categoria:
            if "Descontracturante" in opcion:
                tratamiento = "Masaje Descontracturante Profundo"
                descripcion = "Trabaja directamente sobre las capas profundas del músculo para liberar fascias, deshacer nudos rebeldes y devolver la movilidad y el alivio a tu cuerpo."
                icono = "💆‍♀️"
            elif "Relajante" in opcion:
                tratamiento = "Masaje Relajante con Aromaterapia"
                descripcion = "Creado para calmar por completo el sistema nervioso, reducir los niveles de estrés y regalarte un espacio de paz y descanso profundo."
                icono = "🌿"
            elif "Drenaje" in opcion:
                tratamiento = "Drenaje Linfático / Retorno Venoso"
                descripcion = "Técnica suave y precisa para estimular la circulación, eliminar líquidos retenidos y aliviar la sensación de pesadez en las piernas."
                icono = "🌊"
            elif "Deportivo" in opcion:
                tratamiento = "Masaje Deportivo Especializado"
                descripcion = "Ideal para preparar el tejido muscular ante el esfuerzo físico o acelerar su recuperación óptima post-entrenamiento."
                icono = "⚡"
            else:
                tratamiento = "Masaje Reductivo y Modelador"
                descripcion = "Ayuda a activar la circulación local, movilizar grasa superficial y perfilar la silueta de forma natural."
                icono = "✨"
        else:
            if "Nanoqueratina" in opcion:
                tratamiento = "Nanoqueratina Capilar Pro"
                descripcion = "Sella la cutícula, elimina el frizz al 100% y aporta un brillo espejo espectacular de larga duración."
                icono = "✨"
            elif "Hidratación" in opcion:
                tratamiento = "Hidratación Capilar Profunda"
                descripcion = "Devuelve la suavidad, elasticidad y nutrición extrema a las hebras maltratadas por procesos químicos o calor."
                icono = "💧"
            elif "Detox" in opcion:
                tratamiento = "Detox Purificante Capilar"
                descripcion = "Limpia a profundidad, equilibra la grasa natural y revitaliza la salud de tu raíz desde la primera sesión."
                icono = "🍃"
            else:
                tratamiento = "Tratamiento Anticaída y Estimulante"
                descripcion = "Activa el riego sanguíneo en el folículo para fortalecer la hebra capilar y fomentar un crecimiento sano."
                icono = "🌱"

        # Guardar en CSV
        nuevo_registro = pd.DataFrame({
            "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M")],
            "Nombre": [nombre],
            "WhatsApp": [telefono],
            "Área": [categoria],
            "Selección": [opcion],
            "Recomendación": [tratamiento]
        })
        nuevo_registro.to_csv("clientes_priskah.csv", mode='a', header=False, index=False)

        # Mostrar tarjeta de resultado de lujo
        st.markdown(f"""
            <div class="result-card">
                <div class="result-badge">✨ Tu Recomendación Personalizada</div>
                <div class="result-title">{icono} {tratamiento}</div>
                <p class="result-desc">{descripcion}</p>
            </div>
        """, unsafe_allow_html=True)

        # Botón de WhatsApp
        mi_numero_whatsapp = "50660218458"
        mensaje = f"Hola Priskah, soy {nombre}. Realicé el diagnóstico en tu web para {categoria}, mi resultado fue *{tratamiento}* y me gustaría agendar una cita."
        mensaje_codificado = urllib.parse.quote(mensaje)
        link_whatsapp = f"https://wa.me/{mi_numero_whatsapp}?text={mensaje_codificado}"

        st.markdown(f"""
            <div style="text-align: center; margin-top: 10px; margin-bottom: 15px;">
                <a href="{link_whatsapp}" target="_blank" class="wa-btn">
                    💬 Agendar mi cita por WhatsApp
                </a>
                <p style="font-size: 12px; color: #8C857B; margin-top: 12px;">
                    Tus datos han sido registrados de forma segura.
                </p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='gold-divider'>", unsafe_allow_html=True)

# --- PANEL DE ADMINISTRACIÓN PROTEGIDO ---
with st.expander("🔒 Acceso Propietaria"):
    password_ingresada = st.text_input("Contraseña de administración:", type="password")
    
    if password_ingresada == "Priskah2026*":
        st.success("Acceso concedido.")
        try:
            df_registros = pd.read_csv(
                "clientes_priskah.csv",
                names=["Fecha", "Nombre", "WhatsApp", "Área", "Selección", "Recomendación"]
            )
            st.dataframe(df_registros, use_container_width=True)
            
            csv_data = df_registros.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Descargar lista en CSV",
                data=csv_data,
                file_name="clientes_priskah.csv",
                mime="text/csv"
            )
        except FileNotFoundError:
            st.info("Aún no hay registros guardados en el sistema.")
    elif password_ingresada != "":
        st.error("❌ Contraseña incorrecta.")
