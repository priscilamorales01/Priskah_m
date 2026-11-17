import streamlit as st
import pandas as pd
from datetime import datetime, date
import urllib.parse
import re

# 1. Configurar la página
st.set_page_config(
    page_title="Priskah_m | Bienestar & Recuperación Capilar",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- DISEÑO UX TOTAL: LUXURY BOTANICAL SPA ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    :root {
        color-scheme: light !important;
    }

    /* Animación suave de entrada */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Fondo general multicapa y tipografía */
    [data-testid="stAppViewContainer"], .stApp {
        background: radial-gradient(circle at 50% 0%, #FFFFFF 0%, #F7F3EB 55%, #EFE9DE 100%) !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #232E24 !important;
    }

    /* Ocultar elementos nativos de Streamlit */
    [data-testid="stHeader"], footer, #MainMenu {
        visibility: hidden;
        height: 0px;
    }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 4rem;
        max-width: 740px;
        animation: fadeIn 0.45s ease-out;
    }

    /* --- HERO BANNER DE CABECERA --- */
    .hero-wrapper {
        background: linear-gradient(145deg, rgba(255,255,255,0.92) 0%, rgba(250,246,239,0.95) 100%);
        border: 1px solid #E5DEC9;
        border-radius: 24px;
        padding: 24px 20px 18px 20px;
        text-align: center;
        box-shadow: 0 14px 35px rgba(35, 46, 36, 0.06);
        margin-bottom: 18px;
    }
    .brand-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 46px;
        font-weight: 700;
        color: #1F2D21;
        letter-spacing: 0.8px;
        line-height: 1.05;
        margin-top: 6px;
        margin-bottom: 4px;
    }
    .brand-slogan {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-size: 18px;
        color: #7A633E;
        margin-bottom: 8px;
    }
    .brand-subtitle {
        font-size: 11.5px;
        font-weight: 600;
        color: #5C645B;
        text-transform: uppercase;
        letter-spacing: 2.2px;
        margin-bottom: 10px;
    }
    .location-pill {
        display: inline-block;
        background-color: #F4EFE6;
        border: 1px solid #DFD3C0;
        color: #2C3A2E;
        font-size: 12px;
        font-weight: 600;
        padding: 5px 14px;
        border-radius: 30px;
        margin: 3px;
    }
    .ethics-badge {
        background: linear-gradient(90deg, #2C3A2E 0%, #3B4D3E 100%);
        color: #F8F4EC;
        font-size: 11.5px;
        font-weight: 600;
        letter-spacing: 0.5px;
        padding: 6px 16px;
        border-radius: 20px;
        display: inline-block;
        margin-top: 8px;
        border: 1px solid #C5A880;
    }

    /* --- ENCABEZADOS DE SECCIÓN CON PASO NUMERADO --- */
    .step-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 6px;
    }
    .step-circle {
        background: linear-gradient(135deg, #C5A880 0%, #9E7F56 100%);
        color: #FFFFFF;
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 13px;
        font-weight: 700;
        flex-shrink: 0;
        box-shadow: 0 3px 8px rgba(158, 127, 86, 0.3);
    }
    .section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 25px;
        font-weight: 700;
        color: #1F2D21;
        margin: 0;
    }
    .section-desc {
        font-size: 13px;
        color: #6E6A63;
        margin-bottom: 16px;
        line-height: 1.5;
    }

    /* --- MENÚ DE NAVEGACIÓN (BOTONES MÓVIL-FIRST) --- */
    div[data-testid="stButton"] button[kind="primary"] {
        background: linear-gradient(135deg, #1F2D21 0%, #354738 100%) !important;
        color: #FFFFFF !important;
        border: 1.5px solid #C5A880 !important;
        border-radius: 14px !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 13.5px !important;
        padding: 0.72rem 0.6rem !important;
        box-shadow: 0 8px 18px rgba(31, 45, 33, 0.22) !important;
        transition: all 0.25s ease !important;
    }
    div[data-testid="stButton"] button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 22px rgba(31, 45, 33, 0.3) !important;
    }

    div[data-testid="stButton"] button[kind="secondary"] {
        background-color: #FFFFFF !important;
        color: #232E24 !important;
        border: 1.5px solid #DFD5C5 !important;
        border-radius: 14px !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 13.5px !important;
        padding: 0.72rem 0.6rem !important;
        box-shadow: 0 4px 10px rgba(35, 46, 36, 0.04) !important;
        transition: all 0.25s ease !important;
    }
    div[data-testid="stButton"] button[kind="secondary"]:hover {
        border-color: #C5A880 !important;
        background-color: #FBF8F3 !important;
        transform: translateY(-1px);
    }

    /* --- CONTENEDORES DE TARJETA (GLASSMORPHISM) --- */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(255, 255, 255, 0.94) !important;
        border-radius: 20px !important;
        border: 1px solid #E6DEC8 !important;
        box-shadow: 0 12px 32px rgba(35, 46, 36, 0.05) !important;
        padding: 22px 24px !important;
        margin-bottom: 18px !important;
        animation: fadeIn 0.35s ease-out;
    }

    /* Inputs, Calendario y Selectores */
    .stTextInput label, .stMultiSelect label, .stDateInput label, .stSelectbox label {
        font-size: 13px !important;
        font-weight: 600 !important;
        color: #2C3A2E !important;
    }
    .stTextInput > div > div > input, .stDateInput > div > div > input {
        background-color: #FAF8F5 !important;
        border-radius: 12px !important;
        border: 1px solid #DCD3C2 !important;
        padding: 11px 14px !important;
        font-size: 14px !important;
        color: #232E24 !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #FAF8F5 !important;
        border-radius: 12px !important;
        border: 1px solid #DCD3C2 !important;
        color: #232E24 !important;
    }

    /* Opciones de Radio interactivas */
    div[role="radiogroup"] > label {
        background-color: #FAF8F5 !important;
        border: 1px solid #E6DEC8 !important;
        border-radius: 14px !important;
        padding: 14px 16px !important;
        margin-bottom: 9px !important;
        transition: all 0.22s ease;
        cursor: pointer;
    }
    div[role="radiogroup"] > label:hover {
        border-color: #C5A880 !important;
        background-color: #FFFFFF !important;
        transform: translateX(3px);
        box-shadow: 0 5px 15px rgba(197, 168, 128, 0.15);
    }
    div[role="radiogroup"] p {
        font-size: 14px !important;
        color: #232E24 !important;
        font-weight: 500 !important;
        line-height: 1.45;
    }

    /* Expander elegante */
    [data-testid="stExpander"] {
        background-color: #FFFFFF !important;
        border-radius: 14px !important;
        border: 1px solid #E6DEC8 !important;
        margin-bottom: 10px !important;
    }
    [data-testid="stExpander"] summary p {
        color: #1F2D21 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }

    /* --- TARJETA DE RESULTADO CERTIFICADO --- */
    .result-card {
        background: linear-gradient(145deg, #FFFFFF 0%, #FAF6EE 100%);
        border: 1.5px solid #D8C39E;
        border-top: 6px solid #2C3A2E;
        border-radius: 20px;
        padding: 26px;
        margin-top: 18px;
        margin-bottom: 16px;
        box-shadow: 0 16px 36px rgba(35, 46, 36, 0.09);
        animation: fadeIn 0.4s ease-out;
    }
    .result-badge {
        display: inline-block;
        background-color: #EFE7D8;
        color: #7A6038;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        padding: 5px 13px;
        border-radius: 20px;
        margin-bottom: 10px;
    }
    .result-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 30px;
        font-weight: 700;
        color: #1F2D21;
        margin-bottom: 8px;
    }
    .result-desc {
        font-size: 14.5px;
        color: #454F46;
        line-height: 1.65;
        margin-bottom: 14px;
    }
    .appointment-summary {
        background-color: #F4EFE6;
        border-radius: 12px;
        padding: 12px 16px;
        font-size: 13px;
        color: #232E24;
        border-left: 4px solid #C5A880;
        margin-top: 12px;
    }

    /* Bono Turrúcares */
    .turrucares-bonus {
        background: linear-gradient(135deg, #1F2D21 0%, #344937 100%);
        color: #FFFFFF;
        border-radius: 16px;
        padding: 18px 22px;
        margin-bottom: 18px;
        border: 1.5px solid #C5A880;
        box-shadow: 0 10px 25px rgba(31, 45, 33, 0.18);
    }

    /* --- TARJETA DE FIDELIDAD VISUAL (SELLOS) --- */
    .stamp-grid {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 16px 0;
        flex-wrap: wrap;
    }
    .stamp-slot {
        width: 52px;
        height: 52px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        font-weight: 700;
        border: 2px dashed #C5A880;
        background-color: #FAF8F5;
        color: #B5AA99;
    }
    .stamp-filled {
        background: linear-gradient(135deg, #2C3A2E 0%, #3B4D3E 100%);
        color: #FFFFFF;
        border: 2px solid #C5A880;
        box-shadow: 0 4px 10px rgba(44, 58, 46, 0.2);
    }
    .stamp-reward {
        background: linear-gradient(135deg, #C5A880 0%, #9E7F56 100%);
        color: #FFFFFF;
        border: 2px solid #1F2D21;
    }

    /* Tarjetas de Servicios y Promociones */
    .promo-card {
        background: linear-gradient(145deg, #FFFFFF 0%, #FAF7F2 100%);
        border: 1.5px solid #DFD3C0;
        border-radius: 16px;
        padding: 20px 22px;
        margin-bottom: 16px;
        box-shadow: 0 6px 18px rgba(44, 58, 46, 0.05);
        transition: transform 0.25s ease;
    }
    .promo-card:hover {
        transform: translateY(-2px);
    }
    .promo-tag {
        display: inline-block;
        background-color: #1F2D21;
        color: #F2ECE1;
        font-size: 10.5px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        padding: 4px 11px;
        border-radius: 12px;
        margin-bottom: 8px;
    }
    .promo-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 22px;
        font-weight: 700;
        color: #1F2D21;
        margin-bottom: 6px;
    }

    .service-item {
        background-color: #FAF8F5;
        border: 1px solid #EAE2D3;
        border-left: 4px solid #2C3A2E;
        border-radius: 14px;
        padding: 16px 18px;
        margin-bottom: 14px;
    }
    .service-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 21px;
        font-weight: 700;
        color: #1F2D21;
        margin-bottom: 2px;
    }
    .service-meta {
        font-size: 11px;
        font-weight: 700;
        color: #8C734B;
        text-transform: uppercase;
        letter-spacing: 0.9px;
        margin-bottom: 8px;
    }
    .service-text {
        font-size: 13.5px;
        color: #4A5249;
        line-height: 1.55;
        margin: 0;
    }

    /* Testimonios */
    .review-card {
        background-color: #FAF8F5;
        border: 1px solid #EAE2D3;
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .stars {
        color: #D4AF37;
        font-size: 14px;
        margin-bottom: 6px;
    }

    .credential-pill {
        display: inline-block;
        background-color: #F2ECE1;
        color: #2C3A2E;
        border: 1px solid #DFD3C0;
        padding: 7px 14px;
        border-radius: 20px;
        font-size: 12.5px;
        font-weight: 600;
        margin: 4px 6px 6px 0;
    }
    .edu-box {
        background-color: #FAF8F5;
        border: 1px solid #EAE2D3;
        border-radius: 12px;
        padding: 14px 18px;
        margin-bottom: 12px;
    }
    .edu-title {
        font-weight: 700;
        font-size: 14px;
        color: #1F2D21;
        margin-bottom: 2px;
    }
    .edu-sub {
        font-size: 12.5px;
        color: #6B655D;
        margin: 0;
    }

    /* Botones de WhatsApp y Flotante */
    .wa-btn {
        background: linear-gradient(135deg, #25D366 0%, #1DA851 100%);
        color: white !important;
        padding: 15px 30px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 14.5px;
        letter-spacing: 0.4px;
        display: inline-block;
        box-shadow: 0 8px 22px rgba(37, 211, 102, 0.32);
        transition: all 0.3s ease;
    }
    .wa-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 26px rgba(37, 211, 102, 0.42);
    }
    .floating-wa {
        position: fixed;
        bottom: 22px;
        right: 22px;
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white !important;
        padding: 12px 18px;
        border-radius: 50px;
        font-size: 13px;
        font-weight: 700;
        text-decoration: none !important;
        box-shadow: 0 8px 24px rgba(18, 140, 126, 0.38);
        z-index: 9999;
        display: flex;
        align-items: center;
        gap: 6px;
        border: 2px solid #FFFFFF;
    }
    .social-btn {
        background-color: #FFFFFF;
        color: #1F2D21 !important;
        border: 1px solid #DFD3C0;
        padding: 9px 18px;
        border-radius: 30px;
        text-decoration: none !important;
        font-size: 13px;
        font-weight: 600;
        margin: 4px 6px;
        display: inline-block;
        box-shadow: 0 3px 10px rgba(44, 58, 46, 0.05);
    }

    .gold-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #D5C5AA, transparent);
        margin: 16px 0 20px 0;
        border: none;
    }

    .logo-circle img {
        border-radius: 50% !important;
        box-shadow: 0 10px 26px rgba(44, 58, 46, 0.16);
        border: 3px solid #C5A880;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# --- BOTÓN FLOTANTE DE WHATSAPP SIEMPRE VISIBLE ---
link_wa_rapido = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, estoy visitando tu página web y me gustaría hacerte una consulta.')}"
st.markdown(f"""
    <a href="{link_wa_rapido}" target="_blank" class="floating-wa">
        💬 WhatsApp Directo
    </a>
""", unsafe_allow_html=True)

# --- FUNCIÓN PARA CONTAR VISITAS DE FIDELIDAD ---
def obtener_visitas_cliente(telefono_limpio):
    try:
        df = pd.read_csv(
            "clientes_priskah.csv",
            names=["Fecha", "Nombre", "WhatsApp", "Modalidad", "Fecha_Cita", "Horario", "Área", "Selección", "Condiciones", "Recomendación"],
            on_bad_lines="skip"
        )
        df["WhatsApp_Str"] = df["WhatsApp"].astype(str).str.replace(r"\D", "", regex=True)
        return int((df["WhatsApp_Str"] == telefono_limpio).sum())
    except FileNotFoundError:
        return 0

# --- CONTROL DE NAVEGACIÓN ---
if "pagina_activa" not in st.session_state:
    st.session_state.pagina_activa = "diagnostico"

def cambiar_pagina(nombre_pagina):
    st.session_state.pagina_activa = nombre_pagina

# --- CABECERA HERO LUXURY ---
st.markdown("<div class='hero-wrapper'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1.4, 1, 1.4])
with col2:
    st.markdown("<div class='logo-circle'>", unsafe_allow_html=True)
    try:
        st.image("LOGO.jpeg", use_container_width=True)
    except:
        pass
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='brand-title'>Priskah_m</div>
    <div class='brand-slogan'>“Cuida tu cuerpo • Relaja tu mente y energía”</div>
    <div class='brand-subtitle'>Masajes Especializados & Recuperación Capilar</div>
    <div>
        <span class='location-pill'>📍 Cabina en Turrúcares, Alajuela</span>
        <span class='location-pill'>🏠 A Domicilio: Turrúcares y San Ramón</span>
    </div>
    <div class='ethics-badge'>🛡️ Servicio Exclusivamente Profesional y Terapéutico (No Tántrico)</div>
</div>
""", unsafe_allow_html=True)

# --- MENÚ PRINCIPAL DE NAVEGACIÓN ---
nav1, nav2, nav3, nav4 = st.columns(4)
with nav1:
    st.button(
        "✨ Diagnóstico",
        use_container_width=True,
        type="primary" if st.session_state.pagina_activa == "diagnostico" else "secondary",
        on_click=cambiar_pagina,
        args=("diagnostico",)
    )
with nav2:
    st.button(
        "🎁 Promos & Club",
        use_container_width=True,
        type="primary" if st.session_state.pagina_activa == "promos" else "secondary",
        on_click=cambiar_pagina,
        args=("promos",)
    )
with nav3:
    st.button(
        "🌿 Servicios",
        use_container_width=True,
        type="primary" if st.session_state.pagina_activa == "servicios" else "secondary",
        on_click=cambiar_pagina,
        args=("servicios",)
    )
with nav4:
    st.button(
        "👩‍⚕️ Fundadora",
        use_container_width=True,
        type="primary" if st.session_state.pagina_activa == "fundadora" else "secondary",
        on_click=cambiar_pagina,
        args=("fundadora",)
    )

st.markdown("<hr class='gold-divider'>", unsafe_allow_html=True)

# ==========================================
# VISTA 1: DIAGNÓSTICO + AGENDAMIENTO GUIADO
# ==========================================
if st.session_state.pagina_activa == "diagnostico":
    
    # PASO 1: DATOS Y MODALIDAD
    with st.container(border=True):
        st.markdown("""
            <div class='step-header'>
                <span class='step-circle'>1</span>
                <h3 class='section-title'>Tus Datos y Modalidad</h3>
            </div>
            <div class='section-desc'>Ingresa tus datos para personalizar tu expediente y acumular sellos en tu Tarjeta de Fidelidad.</div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            nombre = st.text_input("Nombre completo", placeholder="Ej: María José Pérez")
        with c2:
            telefono = st.text_input("Número de WhatsApp (8 dígitos)", placeholder="Ej: 60218458")

        st.write("")
        modalidad = st.radio(
            "📍 ¿Cómo prefieres recibir tu atención?",
            [
                "✨ En Sede Turrúcares, Alajuela (Desbloquea Promoción Exclusiva + Regalía)",
                "🏠 Servicio A Domicilio (Disponible en Turrúcares y San Ramón)"
            ]
        )

    # PASO 2: ÁREA A CONSENTIR
    with st.container(border=True):
        st.markdown("""
            <div class='step-header'>
                <span class='step-circle'>2</span>
                <h3 class='section-title'>¿Qué área deseas consentir hoy?</h3>
            </div>
            <div class='section-desc'>Selecciona el enfoque de tu sesión.</div>
        """, unsafe_allow_html=True)
        
        categoria = st.radio(
            "Categoría",
            ["💆‍♀️ Masajes Especializados y Reducción de Medidas", "✨ Tratamientos y Recuperación Capilar"],
            label_visibility="collapsed"
        )

    # PASO 3: NECESIDAD Y VALORACIÓN DE SEGURIDAD
    with st.container(border=True):
        if "Masajes" in categoria:
            st.markdown("""
                <div class='step-header'>
                    <span class='step-circle'>3</span>
                    <h3 class='section-title'>Evaluación Corporal y Seguridad</h3>
                </div>
                <div class='section-desc'>Selecciona la opción que mejor describa lo que tu cuerpo necesita hoy.</div>
            """, unsafe_allow_html=True)
            opcion = st.radio(
                "Enfoque corporal",
                [
                    "Dolor intenso de espalda, cuello, hombros o nudos profundos (Terapéutico / Descontracturante)",
                    "Nivel alto de estrés, ansiedad, insomnio y fatiga mental (Masaje Relajante)",
                    "Sobrecarga muscular por entrenamiento o deporte (Deportivo / Descarga Muscular)",
                    "Piernas cansadas, retención de líquidos o mala circulación (Drenaje Linfático / Retorno Venoso)",
                    "Reducción de medidas, marcación abdominal o cierre de costillas (Moldeo y Drenaje Brasileño)"
                ],
                label_visibility="collapsed"
            )
            
            st.write("")
            condiciones = st.multiselect(
                "🩺 Valoración de Seguridad (Selecciona si presentas alguna condición actual):",
                [
                    "Ninguna condición especial",
                    "Embarazo o lactancia",
                    "Cirugía reciente (menos de 6 meses)",
                    "Lesión muscular o articular aguda",
                    "Problemas circulatorios severos / trombosis",
                    "Piel sensible o alergias a aceites"
                ],
                default=["Ninguna condición especial"]
            )
        else:
            st.markdown("""
                <div class='step-header'>
                    <span class='step-circle'>3</span>
                    <h3 class='section-title'>Evaluación de tu Hebra Capilar</h3>
                </div>
                <div class='section-desc'>Selecciona el estado actual de tu cabello y lo que deseas lograr.</div>
            """, unsafe_allow_html=True)
            opcion = st.radio(
                "Necesidad capilar",
                [
                    "Cabello muy seco, poroso o dañado por químicos (Recuperación Capilar con Colesterol y Miel)",
                    "Cabello opaco, sensibilizado o con frizz (Botox Capilar / Nutrición Profunda)",
                    "Busco brillo espejo, reconstrucción profunda y efecto liso (Queratina / Nanoqueratina)",
                    "Alisado progresivo natural y reducción de volumen (Taninoplastia / Alisado Capilar)"
                ],
                label_visibility="collapsed"
            )

            st.write("")
            condiciones = st.multiselect(
                "🩺 Valoración Capilar Previa (Selecciona si aplica algún caso):",
                [
                    "Ninguna condición especial",
                    "Decoloración reciente o mechas muy claras",
                    "Cuero cabelludo sensible, irritado o con alergias",
                    "Uso previo de henna o tintes metálicos",
                    "Embarazo o lactancia",
                    "Caída capilar severa"
                ],
                default=["Ninguna condición especial"]
            )

    # PASO 4: FECHA Y HORARIO PREFERIDO
    with st.container(border=True):
        st.markdown("""
            <div class='step-header'>
                <span class='step-circle'>4</span>
                <h3 class='section-title'>Preferencia de Cita</h3>
            </div>
            <div class='section-desc'>Elige tu fecha tentativa y horario ideal para agilizar tu reserva por WhatsApp.</div>
        """, unsafe_allow_html=True)

        f_col1, f_col2 = st.columns(2)
        with f_col1:
            fecha_cita = st.date_input("📅 Fecha tentativa", min_value=date.today(), value=date.today())
        with f_col2:
            horario_cita = st.selectbox(
                "🕒 Franja horaria preferida",
                [
                    "Mañana (8:00 AM - 12:00 MD)",
                    "Tarde (1:00 PM - 5:00 PM)",
                    "Noche / After Office (5:30 PM - 8:00 PM)",
                    "Sábado / Fin de Semana"
                ]
            )

    if st.button("✨ Obtener mi Diagnóstico Certificado y Beneficio", type="primary", use_container_width=True):
        solo_digitos = re.sub(r"\D", "", telefono)
        
        if nombre.strip() == "" or len(solo_digitos) < 8:
            st.warning("⚠️ Por favor, ingresa tu nombre completo y un número de WhatsApp válido (mínimo 8 dígitos).")
        else:
            if "Masajes" in categoria:
                regalo_turrucares = "🎁 Cortesía exclusiva en Sede Turrúcares: +10 minutos de masaje craneofacial relajante + 1 sello en tu Tarjeta de Fidelidad (50% OFF en tu 6° visita)."
                if "Descontracturante" in opcion:
                    tratamiento = "Masaje Terapéutico y Descontracturante Profundo"
                    descripcion = "Protocolo manual enfocado en liberar fascias, puntos gatillo y contracturas profundas en espalda, cuello y hombros, devolviendo ligereza inmediata."
                    duracion = "⏱️ Sesión de 60 min • Incluye valoración muscular inicial"
                    icono = "💆‍♀️"
                elif "Relajante" in opcion:
                    tratamiento = "Masaje Relajante Integral"
                    descripcion = "Maniobras envolventes y rítmicas diseñadas para calmar el sistema nervioso, disminuir niveles de estrés y renovar tu energía."
                    duracion = "⏱️ Sesión de 60 min • Ambiente de aromaterapia y descanso"
                    icono = "🌿"
                elif "Deportivo" in opcion:
                    tratamiento = "Masaje Deportivo y Descarga Muscular"
                    descripcion = "Ideal para aliviar la sobrecarga física tras el entrenamiento, oxigenar las fibras musculares y prevenir lesiones."
                    duracion = "⏱️ Sesión de 60 min • Enfoque en recuperación muscular"
                    icono = "⚡"
                elif "Retorno Venoso" in opcion:
                    tratamiento = "Drenaje Linfático y Retorno Venoso"
                    descripcion = "Técnica especializada para estimular el sistema linfático, eliminar retención de líquidos y aliviar la pesadez e inflamación en las piernas."
                    duracion = "⏱️ Sesión de 60 - 75 min • Estimulación circulatoria"
                    icono = "🌊"
                else:
                    tratamiento = "Reducción de Medidas: Marcación, Cierre de Costillas y Drenaje Brasileño"
                    descripcion = "Técnicas manuales especializadas enfocadas en estilizar el contorno corporal, desinflamar el abdomen y definir la silueta."
                    duracion = "⏱️ Sesión de 60 - 75 min • Valoración anatómica personalizada"
                    icono = "✨"
            else:
                regalo_turrucares = "🎁 Cortesía exclusiva en Sede Turrúcares: Diagnóstico capilar profundo + sellado nutritivo de puntas gratis + 1 sello en tu Tarjeta de Fidelidad."
                if "Colesterol y Miel" in opcion:
                    tratamiento = "Recuperación Capilar Intensiva (Colesterol y Miel)"
                    descripcion = "Fórmula altamente nutritiva y restauradora que repone lípidos, suavidad extrema, fuerza y elasticidad al cabello seco o procesado."
                    duracion = "⏱️ Sesión de 60 - 90 min • Restauración profunda"
                    icono = "🍯"
                elif "Nanoqueratina" in opcion:
                    tratamiento = "Queratina / Nanoqueratina Capilar Pro"
                    descripcion = "Reconstrucción térmica profesional que sella la cutícula al 100%, elimina el frizz y aporta un brillo espejo de larga duración."
                    duracion = "⏱️ Duración según largo y volumen • Diagnóstico de hebra incluido"
                    icono = "✨"
                elif "Botox" in opcion:
                    tratamiento = "Botox Capilar y Nutrición Profunda"
                    descripcion = "Rejuvenecimiento capilar intensivo que devuelve cuerpo, sedosidad y brillo a las hebras sensibilizadas."
                    duracion = "⏱️ Sesión de 90 - 120 min • Hidratación intensiva"
                    icono = "💧"
                else:
                    tratamiento = "Taninoplastia / Alisado Capilar"
                    descripcion = "Alisado orgánico progresivo que disciplina la fibra capilar, controla el volumen y deja el cabello liso, sedoso y manejable."
                    duracion = "⏱️ Duración según largo y volumen • Acabado liso y natural"
                    icono = "🍃"

            texto_condiciones = ", ".join(condiciones) if condiciones else "Ninguna reportada"
            fecha_str = fecha_cita.strftime("%d/%m/%Y")
            es_turrucares = "Sede Turrúcares" in modalidad

            # Guardar en CSV
            nuevo_registro = pd.DataFrame({
                "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M")],
                "Nombre": [nombre.strip()],
                "WhatsApp": [solo_digitos],
                "Modalidad": [modalidad],
                "Fecha_Cita": [fecha_str],
                "Horario": [horario_cita],
                "Área": [categoria],
                "Selección": [opcion],
                "Condiciones": [texto_condiciones],
                "Recomendación": [tratamiento]
            })
            nuevo_registro.to_csv("clientes_priskah.csv", mode='a', header=False, index=False)

            st.markdown(f"""
                <div class="result-card">
                    <div class="result-badge">✨ Certificado de Diagnóstico Personalizado</div>
                    <div class="result-title">{icono} {tratamiento}</div>
                    <p class="result-desc">{descripcion}</p>
                    <p style="font-size: 12.5px; color: #7A6038; font-weight: 700; margin-bottom: 8px;">{duracion}</p>
                    <div class="appointment-summary">
                        👤 <strong>Cliente:</strong> {nombre.strip()} &nbsp;|&nbsp; 📅 <strong>Fecha deseada:</strong> {fecha_str}<br>
                        🕒 <strong>Horario:</strong> {horario_cita} &nbsp;|&nbsp; 📍 <strong>Modalidad:</strong> {modalidad.split('(')[0].strip()}
                    </div>
                </div>
            """, unsafe_allow_html=True)

            if es_turrucares:
                st.markdown(f"""
                    <div class="turrucares-bonus">
                        <div style="font-size: 13.5px; font-weight: 700; color: #EAD8B8; margin-bottom: 4px;">
                            📍 BENEFICIO EXCLUSIVO DESBLOQUEADO (VÁLIDO EN SEDE TURRÚCARES)
                        </div>
                        <div style="font-size: 13.5px; line-height: 1.5;">
                            {regalo_turrucares}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.info("🏠 Has elegido **Servicio a Domicilio** (Turrúcares / San Ramón). *Recuerda que si decides visitarnos en nuestra cabina en Turrúcares, desbloqueas nuestras promociones y cortesías exclusivas.*")

            mi_numero_whatsapp = "50660218458"
            mensaje = (
                f"Hola Priskah, soy {nombre.strip()}. "
                f"Realicé mi diagnóstico en la web y mi recomendación fue *{tratamiento}*. "
                f"Me gustaría agendar para el *{fecha_str}* en horario *{horario_cita}*, "
                f"modalidad *{modalidad.split('(')[0].strip()}* (Salud/Notas: {texto_condiciones})."
            )
            mensaje_codificado = urllib.parse.quote(mensaje)
            link_whatsapp = f"https://wa.me/{mi_numero_whatsapp}?text={mensaje_codificado}"

            st.markdown(f"""
                <div style="text-align: center; margin-top: 12px; margin-bottom: 18px;">
                    <a href="{link_whatsapp}" target="_blank" class="wa-btn">
                        💬 Confirmar mi Cita por WhatsApp
                    </a>
                </div>
            """, unsafe_allow_html=True)

    # --- TESTIMONIOS Y POLÍTICAS EN LA PÁGINA PRINCIPAL ---
    with st.container(border=True):
        st.markdown("<div class='section-title' style='margin-bottom: 12px;'>💬 Lo que dicen nuestras clientas</div>", unsafe_allow_html=True)
        t1, t2 = st.columns(2)
        with t1:
            st.markdown("""
                <div class="review-card">
                    <div class="stars">★★★★★</div>
                    <p style="font-size: 13px; color: #454F46; font-style: italic; margin-bottom: 6px;">
                        "El masaje descontracturante me quitó un dolor de cuello y espalda que tenía hace semanas. El espacio en Turrúcares transmite demasiada paz."
                    </p>
                    <div style="font-size: 12px; font-weight: 700; color: #1F2D21;">— Cliente verificada, Turrúcares</div>
                </div>
            """, unsafe_allow_html=True)
        with t2:
            st.markdown("""
                <div class="review-card">
                    <div class="stars">★★★★★</div>
                    <p style="font-size: 13px; color: #454F46; font-style: italic; margin-bottom: 6px;">
                        "Me hice la recuperación capilar con colesterol y miel y luego la nanoqueratina; el brillo espejo y la suavidad que me dejó en el cabello son increíbles."
                    </p>
                    <div style="font-size: 12px; font-weight: 700; color: #1F2D21;">— Cliente verificada, Alajuela</div>
                </div>
            """, unsafe_allow_html=True)

    with st.expander("📋 Políticas de Reserva, Puntualidad y Métodos de Pago"):
        st.markdown("""
        * **Atención 100% personalizada:** Trabajamos únicamente con cita previa para dedicarte el tiempo y la calidad que mereces.
        * **Puntualidad y Reprogramaciones:** Agradecemos avisar con al menos **24 horas de anticipación** en caso de requerir reprogramar tu espacio.
        * **Métodos de Pago:** Aceptamos **SINPE Móvil**, transferencia bancaria y efectivo.
        * **Ética Profesional:** Todos nuestros servicios de masaje son estrictamente terapéuticos, deportivos, estéticos y de relajación (No tántricos).
        """)

# ==========================================
# VISTA 2: PROMOS SEDE TURRÚCARES, CLUB DE FIDELIDAD Y TALLER
# ==========================================
elif st.session_state.pagina_activa == "promos":
    
    # --- CONSULTOR INTERACTIVO DE TARJETA DE FIDELIDAD ---
    with st.container(border=True):
        st.markdown("<div class='result-badge'>🖤 Programa de Lealtad Oficial</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>Club de Fidelidad Priskah_m</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='section-desc'>
                <strong>¡Premiamos tu constancia!</strong> Cada <strong>5 tratamientos realizados</strong>, tu <strong>6° tratamiento tiene 50% de descuento</strong> o recibes un <strong>Kit de Belleza</strong> especial.
            </div>
        """, unsafe_allow_html=True)

        tel_consulta = st.text_input("🔍 Ingresa tu número de WhatsApp para consultar tus sellos acumulados:", placeholder="Ej: 60218458")
        
        sellos_actuales = 0
        if tel_consulta.strip() != "":
            digitos_consulta = re.sub(r"\D", "", tel_consulta)
            total_visitas = obtener_visitas_cliente(digitos_consulta)
            sellos_actuales = total_visitas % 6
            if total_visitas > 0 and sellos_actuales == 0:
                sellos_actuales = 5
            st.caption(f"Registros encontrados con el número {digitos_consulta}: **{total_visitas} visita(s)**.")

        # Renderizar los 5 sellos + 1 premio
        stamps_html = "<div class='stamp-grid'>"
        for i in range(1, 6):
            if i <= sellos_actuales:
                stamps_html += f"<div class='stamp-slot stamp-filled'>🌿</div>"
            else:
                stamps_html += f"<div class='stamp-slot'>{i}</div>"
        stamps_html += "<div class='stamp-slot stamp-reward' title='50% OFF o Kit de Belleza'>🎁</div></div>"
        st.markdown(stamps_html, unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 12.5px; color: #7A6038; font-weight: 600; margin-bottom: 0;'>Completa tus 5 sellos 🌿 y desbloquea tu regalo 🎁 en la 6° cita</p>", unsafe_allow_html=True)

    # --- TALLER VIRTUAL DE AUTOMASAJE (15 DE DICIEMBRE) ---
    with st.container(border=True):
        link_taller = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, quiero reservar mi espacio para el Taller de Automasaje del 15 de diciembre (Inversión: ₡6,000).')}"
        st.markdown("<div class='result-badge'>💻 Evento Especial En Vivo • Zoom Online</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🌿 Taller de Automasaje Relajante y Descontracturante</div>", unsafe_allow_html=True)
        st.markdown("""
            <p class="service-text" style="margin-bottom: 12px;">
                <strong>¡Libera tu tensión online en diciembre!</strong> Aprende con <strong>Priscilla Morales</strong> técnicas profesionales para aliviar el estrés desde casa:
                <br>• Relajación de cuello, hombros y espalda.
                <br>• Liberación de puntos gatillo y técnicas de bienestar personal.
            </p>
            <div style="background-color: #F4EFE6; border: 1px solid #DFD3C0; border-radius: 12px; padding: 12px 16px; margin-bottom: 14px; font-size: 13.5px; color: #1F2D21;">
                📅 <strong>Fecha:</strong> 15 de Diciembre &nbsp;|&nbsp; 🕖 <strong>Hora:</strong> 7:00 pm (Hora Local) <br>
                ⏱️ <strong>Duración:</strong> 1.5 Horas &nbsp;|&nbsp; 💳 <strong>Inversión:</strong> ₡6,000 colones
            </div>
        """, unsafe_allow_html=True)

        try:
            st.video("video_1.mp4")
        except:
            pass

        st.markdown(f"""
            <div style="text-align: center; margin-top: 12px;">
                <a href="{link_taller}" target="_blank" class="wa-btn">
                    🎟️ Reservar mi cupo al Taller (₡6,000)
                </a>
            </div>
        """, unsafe_allow_html=True)

    # --- PROMOCIONES EXCLUSIVAS SEDE TURRÚCARES ---
    with st.container(border=True):
        st.markdown("<div class='result-badge'>📍 Exclusivo en Cabina • Turrúcares, Alajuela</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🎁 Promociones Exclusivas en Sede Turrúcares</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Beneficios diseñados especialmente para quienes nos visitan en nuestra cabina en Turrúcares.</div>", unsafe_allow_html=True)

        # Promo 1: Dúo Renovación Total
        link_p1 = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, quiero reservar la Promo Ritual Dúo (Masaje + Recuperación Capilar Colesterol y Miel) en tu sede de Turrúcares.')}"
        st.markdown(f"""
            <div class="promo-card">
                <span class="promo-tag">📍 Válido solo en sede Turrúcares</span>
                <div class="promo-title">🍯 Ritual Dúo: Masaje + Recuperación Capilar (Colesterol y Miel)</div>
                <p class="service-text" style="margin-bottom: 10px;">
                    Combina en una misma visita un <strong>Masaje Relajante o Descontracturante (60 min)</strong> + nuestra <strong>Recuperación Capilar con Colesterol y Miel o Botox Capilar</strong> y recibe un <strong>15% de descuento especial</strong> en el paquete completo.
                </p>
                <a href="{link_p1}" target="_blank" style="color: #1F2D21; font-weight: 700; font-size: 13.5px; text-decoration: underline;">
                    👉 Reservar este Ritual en Turrúcares por WhatsApp
                </a>
            </div>
        """, unsafe_allow_html=True)

        # Promo 2: Especial Alisados & Nanoqueratina
        link_p2 = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, me interesa la promoción de Nanoqueratina / Alisado en tu sede de Turrúcares.')}"
        st.markdown(f"""
            <div class="promo-card">
                <span class="promo-tag">📍 Válido solo en sede Turrúcares</span>
                <div class="promo-title">✨ Especial Brillo Espejo (Nanoqueratina o Taninoplastia)</div>
                <p class="service-text" style="margin-bottom: 10px;">
                    Al realizarte tu <strong>Nanoqueratina, Queratina o Taninoplastia</strong> en nuestra cabina de Turrúcares, recibe de cortesía un <strong>masaje relajante de cuello y hombros</strong> durante el tiempo de pose + sellado nutritivo final.
                </p>
                <a href="{link_p2}" target="_blank" style="color: #1F2D21; font-weight: 700; font-size: 13.5px; text-decoration: underline;">
                    👉 Cotizar según mi largo de cabello en Turrúcares
                </a>
            </div>
        """, unsafe_allow_html=True)

        # Promo 3: Amigas en Turrúcares
        link_p3 = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, quiero consultar por la Promo Dúo Amigas en tu sede de Turrúcares.')}"
        st.markdown(f"""
            <div class="promo-card">
                <span class="promo-tag">📍 Válido solo en sede Turrúcares</span>
                <div class="promo-title">👯‍♀️ Plan Amigas en Cabina Turrúcares</div>
                <p class="service-text" style="margin-bottom: 10px;">
                    Agenda en nuestra sede de Turrúcares junto con una amiga o familiar el mismo día y <strong>ambas reciben 15 minutos adicionales de relajación o hidratación capilar de cortesía</strong>.
                </p>
                <a href="{link_p3}" target="_blank" style="color: #1F2D21; font-weight: 700; font-size: 13.5px; text-decoration: underline;">
                    👉 Agendar cita doble en Turrúcares
                </a>
            </div>
        """, unsafe_allow_html=True)

        st.caption("⚠️ Nota: Todas las promociones especiales aplican únicamente realizando el tratamiento en nuestra cabina ubicada en Turrúcares, Alajuela.")

# ==========================================
# VISTA 3: QUÉ OFRECEMOS (CATÁLOGO PROFESIONAL)
# ==========================================
elif st.session_state.pagina_activa == "servicios":
    with st.container(border=True):
        st.markdown("<div class='section-title'>💆‍♀️ Masajes Especializados y Reducción de Medidas</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Disponibles en nuestra cabina en Turrúcares y en modalidad A Domicilio (Turrúcares y San Ramón). Valoración previa e higiene clínica garantizada.</div>", unsafe_allow_html=True)

        st.markdown("""
            <div class="service-item">
                <div class="service-name">Masajes Relajantes, Terapéuticos y Descontracturantes</div>
                <div class="service-meta">⏱️ Sesiones de 60 min • Alivio de puntos gatillo y tensión</div>
                <p class="service-text">Terapias manuales adaptadas para liberar tensión muscular profunda, aliviar contracturas en espalda, cuello y hombros, y equilibrar tu sistema nervioso.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Masaje Deportivo y Descarga Muscular</div>
                <div class="service-meta">⏱️ Sesiones de 60 min • Recuperación física y deportiva</div>
                <p class="service-text">Protocolos enfocados en preparar y recuperar los tejidos musculares sometidos a entrenamiento o alta exigencia física.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Drenaje Linfático y Retorno Venoso</div>
                <div class="service-meta">⏱️ Sesiones de 60 a 75 min • Estimulación circulatoria</div>
                <p class="service-text">Maniobras suaves y precisas para favorecer la eliminación de líquidos retenidos, desinflamar tejidos y aliviar la pesadez en las piernas.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Reducción de Medidas: Marcación, Cierre de Costillas y Drenaje Brasileño</div>
                <div class="service-meta">⏱️ Sesiones personalizadas • Moldeo estético manual</div>
                <p class="service-text">Técnicas corporales especializadas orientadas a estilizar la figura, marcaje abdominal y definición armónica de la silueta.</p>
            </div>
        """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("<div class='section-title'>✨ Tratamientos Capilares con Recuperación</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Fórmulas especializadas aplicadas según las necesidades de tu hebra capilar.</div>", unsafe_allow_html=True)

        st.markdown("""
            <div class="service-item" style="border-left-color: #C5A880;">
                <div class="service-name">Recuperación Capilar (Colesterol y Miel) & Botox Capilar</div>
                <div class="service-meta">🍯 Nutrición profunda • Restauración de hebras maltratadas</div>
                <p class="service-text">Terapia intensiva de reposición lipídica e hidratación profunda que devuelve elasticidad, suavidad y vitalidad al cabello seco o procesado.</p>
            </div>
            <div class="service-item" style="border-left-color: #C5A880;">
                <div class="service-name">Alisados, Queratinas, Nanoqueratina y Taninoplastia</div>
                <div class="service-meta">✨ Sellado térmico • Cero Frizz y Brillo Espejo</div>
                <p class="service-text">Reconstrucción y alineamiento capilar que sella la cutícula, controla el volumen y deja un brillo espejo duradero.</p>
            </div>
        """, unsafe_allow_html=True)

        with st.expander("🖼️ Ver Afiche Oficial de Servicios Priskah_m"):
            try:
                st.image("PRISKA BANNER 1.jpeg", use_container_width=True)
            except:
                st.info("Sube 'PRISKA BANNER 1.jpeg' a tu repositorio de GitHub para mostrar el afiche aquí.")

    link_wa_general = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, estuve viendo tu catálogo de servicios en la web y me gustaría cotizar o agendar una cita.')}"
    st.markdown(f"""
        <div style="text-align: center; margin-top: 10px;">
            <a href="{link_wa_general}" target="_blank" class="wa-btn">
                💬 Consultar Precios y Disponibilidad por WhatsApp
            </a>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# VISTA 4: CONOCE A LA FUNDADORA
# ==========================================
elif st.session_state.pagina_activa == "fundadora":
    with st.container(border=True):
        f1, f2, f3 = st.columns([1.3, 1, 1.3])
        with f2:
            st.markdown("<div class='logo-circle'>", unsafe_allow_html=True)
            try:
                st.image("PRISCILLA.jpeg", use_container_width=True)
            except:
                pass
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center; margin-top: 10px;'><span class='result-badge'>Perfil Profesional y Respaldo Técnico</span></div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title' style='font-size: 30px; text-align: center; margin-bottom: 14px;'>Priscilla Morales Segura</div>", unsafe_allow_html=True)
        
        st.markdown("""
            <p class='result-desc' style='margin-bottom: 16px;'>
                Profesional con sólida trayectoria en entornos multinacionales y gestión empresarial, integrando competencias de <strong>servicio al cliente, planificación, control de calidad y mejora continua</strong> en cada atención personalizada.
            </p>
            <p class='result-desc' style='margin-bottom: 20px;'>
                Como fundadora de <strong>Priskah_m</strong>, combina su formación académica y técnica para ofrecer un servicio exclusivamente profesional, ético y seguro en bienestar corporal y recuperación capilar, realizando siempre una valoración inicial de necesidades y aplicando estrictos protocolos de higiene y bioseguridad.
            </p>
        """, unsafe_allow_html=True)

        st.markdown("<div class='section-title' style='font-size: 21px; margin-top: 10px; margin-bottom: 12px;'>🎓 Formación Técnica y Capacitación Profesional</div>", unsafe_allow_html=True)
        
        st.markdown("""
            <div class="edu-box">
                <div class="edu-title">🌿 Formación en Técnicas de Masaje — Instituto Jasper CR</div>
                <p class="edu-sub">Masaje relajante, descontracturante, deportivo, descarga muscular y retorno venoso.</p>
            </div>
            <div class="edu-box">
                <div class="edu-title">🌊 Talleres Especializados en Masaje — Instituto Multieducativo Costarricense</div>
                <p class="edu-sub">Drenaje linfático brasileño, técnicas de cierre de costillas y marcaje abdominal.</p>
            </div>
            <div class="edu-box">
                <div class="edu-title">✨ Capacitación Profesional en Nanoqueratina — Instituto Yess</div>
                <p class="edu-sub">Formación teórico-práctica en protocolos de nanoqueratina y recuperación capilar.</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='section-title' style='font-size: 21px; margin-top: 22px; margin-bottom: 12px;'>🏛️ Formación Académica Universitaria</div>", unsafe_allow_html=True)

        st.markdown("""
            <div class="edu-box">
                <div class="edu-title">Licenciatura en Administración de Recursos Humanos</div>
                <p class="edu-sub">Universidad Estatal a Distancia (UNED)</p>
            </div>
            <div class="edu-box">
                <div class="edu-title">Especialización en Ingeniería en Telecomunicaciones</div>
                <p class="edu-sub">Universidad Politécnica Internacional</p>
            </div>
            <div class="edu-box">
                <div class="edu-title">Bachillerato en Enseñanza del Inglés</div>
                <p class="edu-sub">Universidad Hispanoamericana</p>
            </div>
            <div class="edu-box">
                <div class="edu-title">Especialización en Comercio Electrónico (E-commerce)</div>
                <p class="edu-sub">Escuela de Organización Industrial, España</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='section-title' style='font-size: 21px; margin-top: 22px; margin-bottom: 10px;'>💎 Pilares de Atención</div>", unsafe_allow_html=True)
        
        st.markdown("""
            <div style="margin-bottom: 14px;">
                <span class="credential-pill">✨ Atención Personalizada y Seguimiento</span>
                <span class="credential-pill">🧼 Higiene y Bioseguridad</span>
                <span class="credential-pill">📋 Valoración Previa de Contraindicaciones</span>
                <span class="credential-pill">⭐ Control de Calidad y Mejora Continua</span>
                <span class="credential-pill">🛡️ Servicio 100% Profesional y Terapéutico</span>
            </div>
        """, unsafe_allow_html=True)

    link_wa_fundadora = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, me encantó conocer tu trayectoria profesional en la web y me gustaría agendar una cita.')}"
    st.markdown(f"""
        <div style="text-align: center; margin-top: 10px;">
            <a href="{link_wa_fundadora}" target="_blank" class="wa-btn">
                💬 Hablar con Priskah por WhatsApp
            </a>
        </div>
    """, unsafe_allow_html=True)

# --- PIE DE PÁGINA CON REDES SOCIALES OFICIALES ---
st.markdown("<hr class='gold-divider'>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; margin-bottom: 24px;">
        <p style="font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 700; color: #1F2D21; margin-bottom: 10px;">
            Síguenos y agenda tu cita hoy
        </p>
        <a href="https://www.instagram.com/priskah_m" target="_blank" class="social-btn">
            📸 Instagram @priskah_m
        </a>
        <a href="https://www.tiktok.com/@priskah_m" target="_blank" class="social-btn">
            🎵 TikTok @priskah_m
        </a>
        <a href="https://wa.me/50660218458" target="_blank" class="social-btn">
            📲 WhatsApp 6021-8458
        </a>
        <p style="font-size: 11.5px; color: #7A746B; margin-top: 14px;">
            © 2026 Priskah_m • Turrúcares, Alajuela & San Ramón • Servicio Exclusivamente Profesional y Terapéutico
        </p>
    </div>
""", unsafe_allow_html=True)

# --- PANEL DE ADMINISTRACIÓN Y CRM DE FIDELIDAD (SOLO PROPIETARIA) ---
with st.expander("🔒 Acceso Propietaria (CRM & Fidelidad)"):
    password_ingresada = st.text_input("Contraseña de administración:", type="password")
    
    if password_ingresada == "Priskah2026*":
        st.success("Acceso concedido al sistema de gestión de Priskah_m.")
        try:
            df_registros = pd.read_csv(
                "clientes_priskah.csv",
                names=["Fecha", "Nombre", "WhatsApp", "Modalidad", "Fecha_Cita", "Horario", "Área", "Selección", "Condiciones", "Recomendación"],
                on_bad_lines="skip"
            )
            
            st.markdown("#### 🏆 Control de Fidelidad por Cliente (Cada 5 citas = 6° al 50% OFF)")
            resumen_fidelidad = (
                df_registros.groupby(["WhatsApp", "Nombre"])
                .size()
                .reset_index(name="Total_Diagnosticos_Citas")
                .sort_values(by="Total_Diagnosticos_Citas", ascending=False)
            )
            resumen_fidelidad["Estado_Premio"] = resumen_fidelidad["Total_Diagnosticos_Citas"].apply(
                lambda x: "🎁 ¡PREMIO DISPONIBLE (6° Cita)!" if x >= 5 and x % 5 == 0 else f"Lleva {x % 5}/5 sellos"
            )
            st.dataframe(resumen_fidelidad, use_container_width=True)

            st.markdown("#### 📋 Historial Completo de Diagnósticos y Citas")
            st.dataframe(df_registros, use_container_width=True)
            
            csv_data = df_registros.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Descargar base de datos en CSV / Excel",
                data=csv_data,
                file_name="clientes_priskah.csv",
                mime="text/csv"
            )
        except FileNotFoundError:
            st.info("Aún no hay registros guardados en el sistema.")
    elif password_ingresada != "":
        st.error("❌ Contraseña incorrecta.")
