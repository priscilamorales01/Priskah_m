import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse
import re

# 1. Configurar la página
st.set_page_config(
    page_title="Diagnóstico | Priskah_m",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ESTÉTICA LUXURY SPA (CSS AVANZADO Y BLINDAJE CONTRA MODO OSCURO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,400&display=swap');

    :root {
        color-scheme: light !important;
    }

    [data-testid="stAppViewContainer"], .stApp {
        background: linear-gradient(180deg, #F9F7F3 0%, #F1ECE3 100%) !important;
        font-family: 'Montserrat', sans-serif;
        color: #2C362B !important;
    }

    [data-testid="stHeader"], footer, #MainMenu {
        visibility: hidden;
        height: 0px;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2.5rem;
        max-width: 720px;
    }

    .brand-title {
        font-family: 'Playfair Display', serif;
        font-size: 40px;
        font-weight: 600;
        color: #2C3A2E;
        text-align: center;
        letter-spacing: 1px;
        margin-top: 8px;
        margin-bottom: 2px;
    }
    .brand-slogan {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 15px;
        color: #555D54;
        text-align: center;
        margin-bottom: 6px;
    }
    .brand-subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 12px;
        font-weight: 600;
        color: #6B655D;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 1.8px;
        margin-bottom: 6px;
    }
    .brand-location {
        font-size: 12.5px;
        color: #8C734B;
        text-align: center;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .ethics-banner {
        background-color: #EFECE6;
        border: 1px solid #D5C9B6;
        color: #2C3A2E;
        font-size: 12px;
        font-weight: 600;
        text-align: center;
        padding: 7px 14px;
        border-radius: 20px;
        margin: 0 auto 18px auto;
        max-width: 520px;
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

    /* --- MENÚ DE NAVEGACIÓN RESPONSIVO (BOTONES) --- */
    div[data-testid="stButton"] button[kind="primary"] {
        background: linear-gradient(135deg, #2C3A2E 0%, #3B4D3E 100%) !important;
        color: #FFFFFF !important;
        border: 2px solid #C5A880 !important;
        border-radius: 14px !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600 !important;
        font-size: 13.5px !important;
        padding: 0.7rem 0.6rem !important;
        box-shadow: 0 6px 16px rgba(44, 58, 46, 0.22) !important;
        transition: all 0.25s ease !important;
    }

    div[data-testid="stButton"] button[kind="secondary"] {
        background-color: #FFFFFF !important;
        color: #2C3A2E !important;
        border: 1.5px solid #D5C9B6 !important;
        border-radius: 14px !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600 !important;
        font-size: 13.5px !important;
        padding: 0.7rem 0.6rem !important;
        box-shadow: 0 3px 10px rgba(44, 58, 46, 0.04) !important;
        transition: all 0.25s ease !important;
    }
    div[data-testid="stButton"] button[kind="secondary"]:hover {
        border-color: #C5A880 !important;
        background-color: #FAF6F0 !important;
        color: #1E2820 !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border-radius: 18px !important;
        border: 1px solid #EAE4D8 !important;
        box-shadow: 0 10px 30px rgba(44, 58, 46, 0.05) !important;
        padding: 22px 24px !important;
        margin-bottom: 18px !important;
    }

    .stTextInput label, .stMultiSelect label {
        font-size: 13px !important;
        font-weight: 600 !important;
        color: #3B4D3E !important;
    }
    .stTextInput > div > div > input {
        background-color: #FAF9F6 !important;
        border-radius: 10px !important;
        border: 1px solid #DDD6C8 !important;
        padding: 12px 14px !important;
        font-size: 14px !important;
        color: #2C362B !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #FAF9F6 !important;
        border-radius: 10px !important;
        border: 1px solid #DDD6C8 !important;
        color: #2C362B !important;
    }

    div[role="radiogroup"] > label {
        background-color: #FAF9F6 !important;
        border: 1px solid #EAE4D8 !important;
        border-radius: 12px !important;
        padding: 14px 16px !important;
        margin-bottom: 10px !important;
        transition: all 0.25s ease;
        cursor: pointer;
    }
    div[role="radiogroup"] > label:hover {
        border-color: #C5A880 !important;
        background-color: #FFFFFF !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(197, 168, 128, 0.12);
    }
    div[role="radiogroup"] p {
        font-size: 14px !important;
        color: #2C362B !important;
        line-height: 1.45;
    }

    [data-testid="stExpander"] {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
        border: 1px solid #EAE4D8 !important;
        margin-bottom: 12px !important;
    }
    [data-testid="stExpander"] summary p {
        color: #2C3A2E !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }

    .result-card {
        background: linear-gradient(145deg, #FFFFFF 0%, #FBF9F5 100%);
        border: 1px solid #DFD3C0;
        border-left: 5px solid #C5A880;
        border-radius: 16px;
        padding: 24px;
        margin-top: 18px;
        margin-bottom: 16px;
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
        font-size: 25px;
        color: #2C3A2E;
        margin-bottom: 10px;
    }
    .result-desc {
        font-size: 14.5px;
        color: #4A5249;
        line-height: 1.65;
        margin-bottom: 10px;
    }

    .turrucares-bonus {
        background: linear-gradient(135deg, #2C3A2E 0%, #3B4D3E 100%);
        color: #FFFFFF;
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 18px;
        border: 1.5px solid #C5A880;
        box-shadow: 0 8px 20px rgba(44, 58, 46, 0.15);
    }

    .loyalty-banner {
        background: linear-gradient(135deg, #FAF3E8 0%, #F2E5D0 100%);
        border: 2px dashed #C5A880;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-bottom: 18px;
    }

    .promo-card {
        background: linear-gradient(145deg, #FFFFFF 0%, #FAF7F2 100%);
        border: 1.5px solid #DFD3C0;
        border-radius: 16px;
        padding: 20px 22px;
        margin-bottom: 16px;
        box-shadow: 0 6px 18px rgba(44, 58, 46, 0.05);
    }
    .promo-tag {
        display: inline-block;
        background-color: #2C3A2E;
        color: #F2ECE1;
        font-size: 10.5px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        padding: 4px 10px;
        border-radius: 12px;
        margin-bottom: 8px;
    }
    .promo-title {
        font-family: 'Playfair Display', serif;
        font-size: 20px;
        font-weight: 600;
        color: #2C3A2E;
        margin-bottom: 6px;
    }

    .service-item {
        background-color: #FAF9F6;
        border: 1px solid #EAE4D8;
        border-left: 4px solid #3B4D3E;
        border-radius: 12px;
        padding: 16px 18px;
        margin-bottom: 14px;
    }
    .service-name {
        font-family: 'Playfair Display', serif;
        font-size: 18px;
        font-weight: 600;
        color: #2C3A2E;
        margin-bottom: 4px;
    }
    .service-meta {
        font-size: 11.5px;
        font-weight: 600;
        color: #8C734B;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 8px;
    }
    .service-text {
        font-size: 13.5px;
        color: #4A5249;
        line-height: 1.55;
        margin: 0;
    }
    .credential-pill {
        display: inline-block;
        background-color: #F2ECE1;
        color: #2C3A2E;
        border: 1px solid #DFD3C0;
        padding: 7px 14px;
        border-radius: 20px;
        font-size: 12.5px;
        font-weight: 500;
        margin: 4px 6px 6px 0;
    }
    .edu-box {
        background-color: #FAF9F6;
        border: 1px solid #EAE4D8;
        border-radius: 12px;
        padding: 14px 18px;
        margin-bottom: 12px;
    }
    .edu-title {
        font-weight: 600;
        font-size: 14px;
        color: #2C3A2E;
        margin-bottom: 2px;
    }
    .edu-sub {
        font-size: 12.5px;
        color: #6B655D;
        margin: 0;
    }

    .wa-btn {
        background: linear-gradient(135deg, #25D366 0%, #1DA851 100%);
        color: white !important;
        padding: 14px 28px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 14.5px;
        letter-spacing: 0.4px;
        display: inline-block;
        box-shadow: 0 8px 20px rgba(37, 211, 102, 0.28);
        transition: all 0.3s ease;
    }
    .wa-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 25px rgba(37, 211, 102, 0.38);
    }
    .social-btn {
        background-color: #FFFFFF;
        color: #2C3A2E !important;
        border: 1px solid #DFD3C0;
        padding: 9px 18px;
        border-radius: 30px;
        text-decoration: none !important;
        font-size: 13px;
        font-weight: 600;
        margin: 4px 6px;
        display: inline-block;
        box-shadow: 0 3px 10px rgba(44, 58, 46, 0.05);
        transition: all 0.25s ease;
    }
    .social-btn:hover {
        border-color: #C5A880;
        background-color: #FAF6F0;
        transform: translateY(-1px);
    }

    .gold-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #D8CBB8, transparent);
        margin: 16px 0 20px 0;
        border: none;
    }

    .logo-circle img {
        border-radius: 50% !important;
        box-shadow: 0 8px 24px rgba(44, 58, 46, 0.14);
        border: 3px solid #DFD3C0;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# --- CONTROL DE NAVEGACIÓN ---
if "pagina_activa" not in st.session_state:
    st.session_state.pagina_activa = "diagnostico"

def cambiar_pagina(nombre_pagina):
    st.session_state.pagina_activa = nombre_pagina

# --- ENCABEZADO Y LOGO ---
col1, col2, col3 = st.columns([1.4, 1, 1.4])
with col2:
    st.markdown("<div class='logo-circle'>", unsafe_allow_html=True)
    try:
        st.image("LOGO.jpeg", use_container_width=True)
    except:
        pass
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='brand-title'>Priskah_m</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-slogan'>Cuida tu cuerpo • Relaja tu mente y energía</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-subtitle'>Masajes Especializados y Recuperación Capilar</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-location'>📍 Sede Turrúcares, Alajuela • 🏠 Servicio a Domicilio (Turrúcares y San Ramón)</div>", unsafe_allow_html=True)
st.markdown("<div class='ethics-banner'>🛡️ Servicio Exclusivamente Profesional y Terapéutico (No Tántrico)</div>", unsafe_allow_html=True)

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
        "🎁 Promos & Taller",
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
# VISTA 1: DIAGNÓSTICO INTERACTIVO
# ==========================================
if st.session_state.pagina_activa == "diagnostico":
    with st.container(border=True):
        st.markdown("<div class='section-title'>1. Tus Datos y Modalidad Preferida</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Completa tu información. Recuerda que al asistir a nuestra sede en Turrúcares desbloqueas promociones y cortesías exclusivas.</div>", unsafe_allow_html=True)
        
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

    with st.container(border=True):
        st.markdown("<div class='section-title'>2. ¿Qué área deseas consentir hoy?</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Elige la experiencia que mejor se adapte a lo que buscas.</div>", unsafe_allow_html=True)
        
        categoria = st.radio(
            "Categoría",
            ["💆‍♀️ Masajes Especializados y Reducción de Medidas", "✨ Tratamientos y Recuperación Capilar"],
            label_visibility="collapsed"
        )

    with st.container(border=True):
        if "Masajes" in categoria:
            st.markdown("<div class='section-title'>3. ¿Cuál es tu objetivo o molestia principal?</div>", unsafe_allow_html=True)
            st.markdown("<div class='section-desc'>Selecciona la opción que mejor describa cómo se siente tu cuerpo hoy.</div>", unsafe_allow_html=True)
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
            st.markdown("<div class='section-title'>3. ¿Cómo se encuentra tu cabello actualmente?</div>", unsafe_allow_html=True)
            st.markdown("<div class='section-desc'>Selecciona tu necesidad capilar principal.</div>", unsafe_allow_html=True)
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

    if st.button("✨ Descubrir mi Tratamiento Ideal", type="primary", use_container_width=True):
        solo_digitos = re.sub(r"\D", "", telefono)
        
        if nombre.strip() == "" or len(solo_digitos) < 8:
            st.warning("⚠️ Por favor, ingresa tu nombre completo y un número de WhatsApp válido (mínimo 8 dígitos).")
        else:
            if "Masajes" in categoria:
                regalo_turrucares = "🎁 Cortesía exclusiva en Sede Turrúcares: +10 minutos de masaje craneofacial relajante + 1 sello para tu Tarjeta de Fidelidad (50% OFF en tu 6° visita)."
                if "Descontracturante" in opcion:
                    tratamiento = "Masaje Terapéutico y Descontracturante Profundo"
                    descripcion = "Enfocado en trabajar las capas profundas del músculo para liberar puntos gatillo, nudos y tensión acumulada en espalda, cuello y hombros."
                    duracion = "⏱️ Duración estimada: 60 min • Valoración previa incluida"
                    icono = "💆‍♀️"
                elif "Relajante" in opcion:
                    tratamiento = "Masaje Relajante Integral"
                    descripcion = "Diseñado para calmar el sistema nervioso, reducir el estrés y renovar tu mente y energía."
                    duracion = "⏱️ Duración estimada: 60 min • Ambiente de aromaterapia y relax"
                    icono = "🌿"
                elif "Deportivo" in opcion:
                    tratamiento = "Masaje Deportivo y Descarga Muscular"
                    descripcion = "Ideal para aliviar la sobrecarga física tras el ejercicio, oxigenar el tejido muscular y acelerar tu recuperación."
                    duracion = "⏱️ Duración estimada: 60 min • Enfoque en recuperación muscular"
                    icono = "⚡"
                elif "Retorno Venoso" in opcion:
                    tratamiento = "Drenaje Linfático y Retorno Venoso"
                    descripcion = "Técnica especializada para estimular el sistema linfático, favorecer la eliminación de líquidos retenidos y aliviar la pesadez en las piernas."
                    duracion = "⏱️ Duración estimada: 60 - 75 min • Estimulación circulatoria y linfática"
                    icono = "🌊"
                else:
                    tratamiento = "Reducción de Medidas: Marcación, Cierre de Costillas y Drenaje Brasileño"
                    descripcion = "Técnicas manuales especializadas enfocadas en estilizar el contorno corporal, desinflamar abdomen y activar la circulación local."
                    duracion = "⏱️ Duración estimada: 60 - 75 min • Valoración personalizada"
                    icono = "✨"
            else:
                regalo_turrucares = "🎁 Cortesía exclusiva en Sede Turrúcares: Diagnóstico capilar + sellado nutritivo de puntas de cortesía + 1 sello para tu Tarjeta de Fidelidad."
                if "Colesterol y Miel" in opcion:
                    tratamiento = "Recuperación Capilar Intensiva (Colesterol y Miel)"
                    descripcion = "Fórmula altamente nutritiva y restauradora que devuelve lípidos, suavidad extrema, fuerza y elasticidad al cabello maltratado o químicamente procesado."
                    duracion = "⏱️ Duración estimada: 60 - 90 min • Restauración profunda"
                    icono = "🍯"
                elif "Nanoqueratina" in opcion:
                    tratamiento = "Queratina / Nanoqueratina Capilar Pro"
                    descripcion = "Tratamiento de reconstrucción térmica que sella la cutícula, elimina el frizz y aporta un brillo espejo duradero."
                    duracion = "⏱️ Duración según largo y volumen • Diagnóstico de hebra incluido"
                    icono = "✨"
                elif "Botox" in opcion:
                    tratamiento = "Botox Capilar y Nutrición Profunda"
                    descripcion = "Devuelve la suavidad, elasticidad y vitalidad a las hebras deshidratadas, opacas o con frizz."
                    duracion = "⏱️ Duración estimada: 90 - 120 min • Hidratación intensiva"
                    icono = "💧"
                else:
                    tratamiento = "Taninoplastia / Alisado Capilar"
                    descripcion = "Alisado progresivo que disciplina la fibra capilar, controla el volumen y deja el cabello sedoso y manejable."
                    duracion = "⏱️ Duración según largo y volumen • Acabado liso y natural"
                    icono = "🍃"

            texto_condiciones = ", ".join(condiciones) if condiciones else "Ninguna reportada"
            es_turrucares = "Sede Turrúcares" in modalidad

            # Guardar en CSV
            nuevo_registro = pd.DataFrame({
                "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M")],
                "Nombre": [nombre.strip()],
                "WhatsApp": [solo_digitos],
                "Modalidad": [modalidad],
                "Área": [categoria],
                "Selección": [opcion],
                "Condiciones": [texto_condiciones],
                "Recomendación": [tratamiento]
            })
            nuevo_registro.to_csv("clientes_priskah.csv", mode='a', header=False, index=False)

            st.markdown(f"""
                <div class="result-card">
                    <div class="result-badge">✨ Tu Recomendación Personalizada</div>
                    <div class="result-title">{icono} {tratamiento}</div>
                    <p class="result-desc">{descripcion}</p>
                    <p style="font-size: 12.5px; color: #8C734B; font-weight: 600; margin-bottom: 0;">{duracion}</p>
                </div>
            """, unsafe_allow_html=True)

            if es_turrucares:
                st.markdown(f"""
                    <div class="turrucares-bonus">
                        <div style="font-size: 13.5px; font-weight: 700; color: #EAD8B8; margin-bottom: 4px;">
                            📍 BENEFICIO EXCLUSIVO DESBLOQUEADO (SEDE TURRÚCARES)
                        </div>
                        <div style="font-size: 13.5px; line-height: 1.5;">
                            {regalo_turrucares}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.info("🏠 Has seleccionado **Servicio a Domicilio** (Turrúcares / San Ramón). *Nota: Si decides asistir a nuestra cabina en Turrúcares, desbloqueas nuestras promociones y minutos extra de cortesía.*")

            mi_numero_whatsapp = "50660218458"
            mensaje = (
                f"Hola Priskah, soy {nombre.strip()}. "
                f"Realicé el diagnóstico en tu web para {categoria}. "
                f"Mi resultado fue *{tratamiento}* en modalidad *{modalidad}* "
                f"(Observaciones: {texto_condiciones}) y me gustaría agendar mi cita."
            )
            mensaje_codificado = urllib.parse.quote(mensaje)
            link_whatsapp = f"https://wa.me/{mi_numero_whatsapp}?text={mensaje_codificado}"

            st.markdown(f"""
                <div style="text-align: center; margin-top: 10px; margin-bottom: 15px;">
                    <a href="{link_whatsapp}" target="_blank" class="wa-btn">
                        💬 Agendar mi cita por WhatsApp
                    </a>
                </div>
            """, unsafe_allow_html=True)

    # --- TARJETA DE FIDELIDAD VISIBLE ---
    st.markdown("""
        <div class="loyalty-banner">
            <div style="font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 600; color: #2C3A2E; margin-bottom: 4px;">
                🖤 Premiamos tu Fidelidad en Priskah_m
            </div>
            <p style="font-size: 14px; color: #4A5249; margin: 0;">
                Por cada <strong>5 tratamientos realizados</strong>, recibe tu <strong>6° tratamiento con 50% de descuento</strong> o un <strong>Kit de Belleza</strong> especial.
            </p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# VISTA 2: PROMOCIONES Y TALLER EN VIVO
# ==========================================
elif st.session_state.pagina_activa == "promos":
    # --- TALLER VIRTUAL DE AUTOMASAJE CON VIDEO ---
    with st.container(border=True):
        link_taller = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, quiero reservar mi espacio para el Taller de Automasaje del 15 de diciembre (Inversión: ₡6,000).')}"
        st.markdown("<div class='result-badge'>💻 Evento Especial En Vivo • Vía Zoom Online</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🌿 Taller de Automasaje Relajante y Descontracturante</div>", unsafe_allow_html=True)
        st.markdown("""
            <p class="service-text" style="margin-bottom: 12px;">
                <strong>¡Libera tu tensión online en diciembre!</strong> Aprende técnicas profesionales para aliviar el estrés y la tensión muscular desde casa.
                <br>• <strong>Temas:</strong> Relajación de cuello, hombros y espalda, liberación de puntos gatillo y técnicas de bienestar personal.
                <br>• <strong>Instructora:</strong> Priscilla Morales
            </p>
            <div style="background-color: #FAF9F6; border: 1px solid #DFD3C0; border-radius: 12px; padding: 12px 16px; margin-bottom: 14px; font-size: 13.5px; color: #2C3A2E;">
                📅 <strong>Fecha:</strong> 15 de Diciembre &nbsp;|&nbsp; 🕖 <strong>Hora:</strong> 7:00 pm (Hora Local) <br>
                ⏱️ <strong>Duración:</strong> 1.5 Horas &nbsp;|&nbsp; 💳 <strong>Inversión:</strong> ₡6,000 colones
            </div>
        """, unsafe_allow_html=True)

        # Mostrar el video del taller si está subido al repositorio
        try:
            st.video("video_1.mp4")
        except:
            pass

        st.markdown(f"""
            <div style="text-align: center; margin-top: 12px;">
                <a href="{link_taller}" target="_blank" class="wa-btn">
                    🎟️ Reservar mi espacio al Taller (₡6,000)
                </a>
            </div>
        """, unsafe_allow_html=True)

    # --- PROMOCIONES EXCLUSIVAS SEDE TURRÚCARES ---
    with st.container(border=True):
        st.markdown("<div class='result-badge'>📍 Exclusivo en Cabina • Turrúcares, Alajuela</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🎁 Promociones Exclusivas en Sede Turrúcares</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Estos beneficios aplican únicamente cuando nos visitas para realizarte tu tratamiento en nuestra sede de Turrúcares.</div>", unsafe_allow_html=True)

        # Fidelidad
        link_fid = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, quiero agendar en Turrúcares y empezar mi tarjeta de fidelidad (5 tratamientos = 6° al 50% OFF).')}"
        st.markdown(f"""
            <div class="promo-card" style="border-left: 5px solid #2C3A2E;">
                <span class="promo-tag">🖤 Tarjeta de Fidelidad Priskah_m</span>
                <div class="promo-title">🎁 50% de Descuento o Kit de Belleza en tu 6° Tratamiento</div>
                <p class="service-text" style="margin-bottom: 10px;">
                    Premiamos tu constancia: acumula <strong>5 tratamientos</strong> con nosotros y en el <strong>6° tratamiento</strong> elige entre un <strong>50% de descuento</strong> o un <strong>Kit de Belleza</strong> de regalo.
                </p>
                <a href="{link_fid}" target="_blank" style="color: #2C3A2E; font-weight: 700; font-size: 13.5px; text-decoration: underline;">
                    👉 Empezar mi Tarjeta de Fidelidad por WhatsApp
                </a>
            </div>
        """, unsafe_allow_html=True)

        # Promo 1: Dúo Renovación Total
        link_p1 = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, quiero consultar por la Promo Dúo en tu sede de Turrúcares (Masaje + Recuperación Capilar Colesterol y Miel).')}"
        st.markdown(f"""
            <div class="promo-card">
                <span class="promo-tag">📍 Válido solo en sede Turrúcares</span>
                <div class="promo-title">🍯 Ritual Dúo: Masaje + Recuperación Capilar (Colesterol y Miel)</div>
                <p class="service-text" style="margin-bottom: 10px;">
                    Realízate en nuestra cabina de Turrúcares un <strong>Masaje Relajante o Descontracturante (60 min)</strong> junto con nuestra <strong>Recuperación Capilar de Colesterol y Miel o Botox Capilar</strong> con un <strong>15% de descuento especial</strong> en el paquete.
                </p>
                <a href="{link_p1}" target="_blank" style="color: #2C3A2E; font-weight: 700; font-size: 13.5px; text-decoration: underline;">
                    👉 Reservar este Ritual en Turrúcares
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
                    Al realizarte tu <strong>Nanoqueratina, Queratina o Alisado</strong> en nuestra cabina de Turrúcares, recibe de cortesía un <strong>masaje relajante de cuello y hombros</strong> durante el tiempo de pose + sellado nutritivo.
                </p>
                <a href="{link_p2}" target="_blank" style="color: #2C3A2E; font-weight: 700; font-size: 13.5px; text-decoration: underline;">
                    👉 Cotizar mi largo de cabello en Turrúcares
                </a>
            </div>
        """, unsafe_allow_html=True)

        st.caption("⚠️ Nota: Los descuentos de cabina aplican exclusivamente asistiendo a nuestra sede en Turrúcares, Alajuela.")

# ==========================================
# VISTA 3: QUÉ OFRECEMOS (PORTAFOLIO)
# ==========================================
elif st.session_state.pagina_activa == "servicios":
    with st.container(border=True):
        st.markdown("<div class='section-title'>💆‍♀️ Masajes Especializados y Reducción de Medidas</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Disponibles en nuestra sede en Turrúcares y A Domicilio (Turrúcares y San Ramón). Servicio exclusivamente profesional y terapéutico.</div>", unsafe_allow_html=True)

        st.markdown("""
            <div class="service-item">
                <div class="service-name">Masajes Relajantes, Terapéuticos y Descontracturantes</div>
                <div class="service-meta">⏱️ Sesiones de 60 min • Liberación de puntos gatillo y estrés</div>
                <p class="service-text">Terapias manuales adaptadas para liberar tensión muscular profunda, aliviar contracturas en espalda, cuello y hombros, y relajar tu mente y energía.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Masaje Deportivo y Descarga Muscular</div>
                <div class="service-meta">⏱️ Sesiones de 60 min • Pre y Post Entrenamiento</div>
                <p class="service-text">Protocolos enfocados en la preparación y recuperación de tejidos musculares sometidos a exigencia física o deporte.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Drenaje Linfático y Retorno Venoso</div>
                <div class="service-meta">⏱️ Sesiones de 60 a 75 min • Estimulación circulatoria</div>
                <p class="service-text">Técnicas especializadas para favorecer el drenaje de líquidos retenidos, desinflamar tejidos y aliviar piernas cansadas.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Reducción de Medidas: Marcación, Cierre de Costillas y Drenaje Brasileño</div>
                <div class="service-meta">⏱️ Sesiones personalizadas • Moldeo estético manual</div>
                <p class="service-text">Técnicas corporales especializadas orientadas a la reducción de medidas, marcaje abdominal y definición armónica de la silueta.</p>
            </div>
        """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("<div class='section-title'>✨ Tratamientos Capilares y Recuperación</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Fórmulas profesionales aplicadas según el diagnóstico de tu hebra capilar.</div>", unsafe_allow_html=True)

        st.markdown("""
            <div class="service-item" style="border-left-color: #C5A880;">
                <div class="service-name">Recuperación Capilar (Colesterol y Miel) y Botox Capilar</div>
                <div class="service-meta">🍯 Nutrición profunda • Restauración de hebras maltratadas</div>
                <p class="service-text">Acondicionamiento y nutrición intensiva con activos como colesterol y miel para devolver suavidad, elasticidad y vitalidad al cabello seco o procesado.</p>
            </div>
            <div class="service-item" style="border-left-color: #C5A880;">
                <div class="service-name">Alisados, Queratinas, Nanoqueratina y Taninoplastia</div>
                <div class="service-meta">✨ Sellado térmico • Cero Frizz y Brillo Espejo</div>
                <p class="service-text">Reconstrucción y sellado de la cutícula capilar para eliminar el frizz, controlar el volumen y aportar un brillo espejo duradero.</p>
            </div>
        """, unsafe_allow_html=True)

        # Mostrar afiche oficial si está en el repositorio
        with st.expander("📋 Ver Afiche Oficial de Servicios Priskah_m"):
            try:
                st.image("PRISKA BANNER 1.jpeg", use_container_width=True)
            except:
                st.info("Sube el archivo 'PRISKA BANNER 1.jpeg' a tu GitHub para visualizar el afiche aquí.")

    link_wa_general = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, estuve viendo los servicios en tu web y me gustaría agendar una cita.')}"
    st.markdown(f"""
        <div style="text-align: center; margin-top: 10px;">
            <a href="{link_wa_general}" target="_blank" class="wa-btn">
                💬 Agendar mi cita hoy por WhatsApp
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

        st.markdown("<div style='text-align: center; margin-top: 10px;'><span class='result-badge'>Perfil Profesional y Trayectoria</span></div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title' style='font-size: 28px; text-align: center; margin-bottom: 14px;'>Priscilla Morales Segura</div>", unsafe_allow_html=True)
        
        st.markdown("""
            <p class='result-desc' style='margin-bottom: 16px;'>
                Profesional con sólida trayectoria en entornos multinacionales y gestión empresarial, integrando competencias de <strong>servicio al cliente, planificación, control de calidad y mejora continua</strong> en cada atención personalizada.
            </p>
            <p class='result-desc' style='margin-bottom: 20px;'>
                Como fundadora de <strong>Priskah_m</strong>, combina su formación académica y técnica para ofrecer un servicio exclusivamente profesional, ético y personalizado en bienestar corporal y recuperación capilar, realizando siempre una valoración inicial de necesidades y aplicando estrictos protocolos de higiene y bioseguridad.
            </p>
        """, unsafe_allow_html=True)

        st.markdown("<div class='section-title' style='font-size: 19px; margin-top: 10px; margin-bottom: 12px;'>🎓 Formación Técnica Especializada</div>", unsafe_allow_html=True)
        
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

        st.markdown("<div class='section-title' style='font-size: 19px; margin-top: 22px; margin-bottom: 12px;'>🏛️ Formación Académica Universitaria</div>", unsafe_allow_html=True)

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

        st.markdown("<div class='section-title' style='font-size: 19px; margin-top: 22px; margin-bottom: 10px;'>💎 Pilares de Atención</div>", unsafe_allow_html=True)
        
        st.markdown("""
            <div style="margin-bottom: 14px;">
                <span class="credential-pill">✨ Atención Personalizada y Seguimiento</span>
                <span class="credential-pill">🧼 Higiene y Bioseguridad</span>
                <span class="credential-pill">📋 Valoración Previa de Contraindicaciones</span>
                <span class="credential-pill">⭐ Control de Calidad y Mejora Continua</span>
                <span class="credential-pill">🛡️ Servicio 100% Profesional y Terapéutico</span>
            </div>
        """, unsafe_allow_html=True)

    link_wa_fundadora = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, me encantó conocer tu formación y servicios en Priskah_m. Me gustaría agendar una cita.')}"
    st.markdown(f"""
        <div style="text-align: center; margin-top: 10px;">
            <a href="{link_wa_fundadora}" target="_blank" class="wa-btn">
                💬 Agendar valoración por WhatsApp
            </a>
        </div>
    """, unsafe_allow_html=True)

# --- PIE DE PÁGINA CON REDES SOCIALES OFICIALES ---
st.markdown("<hr class='gold-divider'>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; margin-bottom: 24px;">
        <p style="font-family: 'Playfair Display', serif; font-size: 18px; color: #2C3A2E; margin-bottom: 10px;">
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
        <p style="font-size: 11.5px; color: #8C857B; margin-top: 14px;">
            © 2026 Priskah_m • Turrúcares, Alajuela & San Ramón • Servicio Exclusivamente Profesional y Terapéutico
        </p>
    </div>
""", unsafe_allow_html=True)

# --- PANEL DE ADMINISTRACIÓN PROTEGIDO ---
with st.expander("🔒 Acceso Propietaria"):
    password_ingresada = st.text_input("Contraseña de administración:", type="password")
    
    if password_ingresada == "Priskah2026*":
        st.success("Acceso concedido.")
        try:
            df_registros = pd.read_csv(
                "clientes_priskah.csv",
                names=["Fecha", "Nombre", "WhatsApp", "Modalidad", "Área", "Selección", "Condiciones", "Recomendación"],
                on_bad_lines="skip"
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
