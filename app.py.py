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
        max-width: 720px;
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
        margin-bottom: 20px;
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

    /* Estilo de las Pestañas (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        justify-content: center;
        background-color: transparent;
        border-bottom: 1px solid #E2D9C8;
        padding-bottom: 8px;
        margin-bottom: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #FAF9F6;
        border-radius: 25px;
        padding: 10px 20px;
        font-family: 'Montserrat', sans-serif;
        font-size: 13.5px;
        font-weight: 500;
        color: #555D54;
        border: 1px solid #EAE4D8;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        border-color: #C5A880;
        color: #2C3A2E;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3B4D3E 0%, #2C3A2E 100%) !important;
        color: #FFFFFF !important;
        border-color: #2C3A2E !important;
        box-shadow: 0 4px 12px rgba(44, 58, 46, 0.15);
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

    /* Tarjetas de Servicios y Fundadora */
    .service-item {
        background-color: #FAF9F6;
        border: 1px solid #EAE4D8;
        border-left: 4px solid #3B4D3E;
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 14px;
    }
    .service-name {
        font-family: 'Playfair Display', serif;
        font-size: 18px;
        font-weight: 600;
        color: #2C3A2E;
        margin-bottom: 6px;
    }
    .service-text {
        font-size: 13.5px;
        color: #555D54;
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
        color: #7A746B;
        margin: 0;
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
        margin: 18px 0 24px 0;
        border: none;
    }

    /* Imágenes redondeadas con marco elegante */
    [data-testid="stImage"] img {
        border-radius: 50%;
        box-shadow: 0 8px 24px rgba(44, 58, 46, 0.14);
        border: 3px solid #DFD3C0;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO Y LOGO ---
col1, col2, col3 = st.columns([1.4, 1, 1.4])
with col2:
    try:
        st.image("LOGO.jpeg", use_container_width=True)
    except:
        pass

st.markdown("<div class='brand-title'>Priskah_m</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-subtitle'>Masajes y Cabellos con Recuperación Capilar</div>", unsafe_allow_html=True)

# --- PESTAÑAS DE NAVEGACIÓN (TABS) ---
tab_diagnostico, tab_servicios, tab_fundadora = st.tabs([
    "✨ Diagnóstico Personalizado",
    "🌿 Qué Ofrecemos",
    "👩‍⚕️ Conoce a la Fundadora"
])

# ==========================================
# PESTAÑA 1: DIAGNÓSTICO INTERACTIVO
# ==========================================
with tab_diagnostico:
    with st.container(border=True):
        st.markdown("<div class='section-title'>Tus Datos</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Completa tu información para identificar tus necesidades y recomendar el protocolo ideal.</div>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            nombre = st.text_input("Nombre completo", placeholder="Ej: María José Pérez")
        with c2:
            telefono = st.text_input("Número de WhatsApp", placeholder="Ej: 60218458")

    with st.container(border=True):
        st.markdown("<div class='section-title'>¿Qué área deseas consentir hoy?</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Elige la experiencia que mejor se adapte a lo que buscas.</div>", unsafe_allow_html=True)
        
        categoria = st.radio(
            "Categoría",
            ["💆‍♀️ Bienestar Corporal y Masajes", "✨ Cuidado y Recuperación Capilar"],
            label_visibility="collapsed"
        )

    with st.container(border=True):
        if "Corporal" in categoria:
            st.markdown("<div class='section-title'>¿Cuál es tu objetivo o molestia principal?</div>", unsafe_allow_html=True)
            st.markdown("<div class='section-desc'>Selecciona la opción que mejor describa cómo se siente tu cuerpo hoy.</div>", unsafe_allow_html=True)
            opcion = st.radio(
                "Enfoque corporal",
                [
                    "Dolor intenso de espalda, cuello, hombros o nudos profundos (Descontracturante)",
                    "Nivel alto de estrés, ansiedad, insomnio y fatiga mental (Relajante)",
                    "Sobrecarga muscular por entrenamiento o deporte (Deportivo / Descarga Muscular)",
                    "Piernas cansadas, retención de líquidos o mala circulación (Drenaje Linfático / Retorno Venoso)",
                    "Moldeo corporal, cierre de costillas o marcaje abdominal (Técnicas Estéticas)"
                ],
                label_visibility="collapsed"
            )
        else:
            st.markdown("<div class='section-title'>¿Cómo se encuentra tu cabello actualmente?</div>", unsafe_allow_html=True)
            st.markdown("<div class='section-desc'>Selecciona tu necesidad capilar principal.</div>", unsafe_allow_html=True)
            opcion = st.radio(
                "Necesidad capilar",
                [
                    "Cabello seco, opaco, sensibilizado o con frizz (Botox Capilar / Nutrición)",
                    "Busco brillo espejo, reconstrucción profunda y efecto liso (Nanoqueratina)",
                    "Alisado progresivo natural y manejo del volumen (Taninoplastia / Alisado Capilar)",
                    "Cabello maltratado que requiere reparación y acondicionamiento profundo (Recuperación Capilar)"
                ],
                label_visibility="collapsed"
            )

    if st.button("✨ Descubrir mi Tratamiento Ideal"):
        if nombre.strip() == "" or telefono.strip() == "":
            st.warning("⚠️ Por favor, ingresa tu nombre y número de WhatsApp para ver tu diagnóstico.")
        else:
            if "Corporal" in categoria:
                if "Descontracturante" in opcion:
                    tratamiento = "Masaje Descontracturante Profundo"
                    descripcion = "Enfocado en trabajar las capas profundas del músculo para liberar nudos y tensión acumulada en espalda, cuello y hombros."
                    icono = "💆‍♀️"
                elif "Relajante" in opcion:
                    tratamiento = "Masaje Relajante Integral"
                    descripcion = "Diseñado para calmar el sistema nervioso, reducir el estrés y brindarte un descanso físico y mental profundo."
                    icono = "🌿"
                elif "Deportivo" in opcion:
                    tratamiento = "Masaje Deportivo y Descarga Muscular"
                    descripcion = "Ideal para aliviar la sobrecarga física tras el ejercicio, oxigenar el tejido muscular y acelerar tu recuperación."
                    icono = "⚡"
                elif "Drenaje" in opcion:
                    tratamiento = "Drenaje Linfático Brasileño y Retorno Venoso"
                    descripcion = "Técnica especializada para estimular el sistema linfático, favorecer la eliminación de líquidos retenidos y aliviar la pesadez en las piernas."
                    icono = "🌊"
                else:
                    tratamiento = "Protocolo de Moldeo: Cierre de Costillas y Marcaje Abdominal"
                    descripcion = "Técnicas manuales especializadas enfocadas en estilizar el contorno corporal y activar la circulación local."
                    icono = "✨"
            else:
                if "Nanoqueratina" in opcion:
                    tratamiento = "Nanoqueratina Capilar"
                    descripcion = "Tratamiento de reconstrucción que sella la cutícula, elimina el frizz y aporta un brillo espejo duradero."
                    icono = "✨"
                elif "Botox" in opcion:
                    tratamiento = "Botox Capilar y Nutrición Profunda"
                    descripcion = "Devuelve la suavidad, elasticidad y vitalidad a las hebras deshidratadas o sensibilizadas."
                    icono = "💧"
                elif "Taninoplastia" in opcion:
                    tratamiento = "Taninoplastia / Alisado Capilar"
                    descripcion = "Alisado de origen vegetal que disciplina la fibra capilar, reduce el volumen y deja el cabello sedoso y manejable."
                    icono = "🍃"
                else:
                    tratamiento = "Tratamiento de Recuperación y Acondicionamiento Capilar"
                    descripcion = "Protocolo restaurador diseñado para devolver fuerza, hidratación y salud integral a tu cabello."
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

            st.markdown(f"""
                <div class="result-card">
                    <div class="result-badge">✨ Tu Recomendación Personalizada</div>
                    <div class="result-title">{icono} {tratamiento}</div>
                    <p class="result-desc">{descripcion}</p>
                </div>
            """, unsafe_allow_html=True)

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

# ==========================================
# PESTAÑA 2: QUÉ OFRECEMOS (PORTAFOLIO)
# ==========================================
with tab_servicios:
    with st.container(border=True):
        st.markdown("<div class='section-title'>💆‍♀️ Bienestar Corporal y Masajes</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Servicios personalizados con valoración previa de necesidades y contraindicaciones bajo estrictos estándares de higiene y bioseguridad.</div>", unsafe_allow_html=True)

        st.markdown("""
            <div class="service-item">
                <div class="service-name">Masaje Relajante y Descontracturante</div>
                <p class="service-text">Terapias manuales adaptadas para liberar tensión muscular profunda, aliviar contracturas y calmar el estrés físico y mental.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Masaje Deportivo y Descarga Muscular</div>
                <p class="service-text">Protocolos enfocados en la preparación y recuperación de tejidos musculares sometidos a exigencia física o entrenamiento.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Drenaje Linfático Brasileño y Retorno Venoso</div>
                <p class="service-text">Técnicas especializadas para favorecer el drenaje de líquidos, mejorar la circulación y aliviar la pesadez corporal.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Cierre de Costillas y Marcaje Abdominal</div>
                <p class="service-text">Técnicas corporales especializadas orientadas al moldeo estético y el cuidado integral de la silueta.</p>
            </div>
        """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("<div class='section-title'>✨ Cuidado y Recuperación Capilar</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Tratamientos profesionales aplicados según el diagnóstico de cada hebra y las especificaciones técnicas de cada producto.</div>", unsafe_allow_html=True)

        st.markdown("""
            <div class="service-item" style="border-left-color: #C5A880;">
                <div class="service-name">Queratinas y Nanoqueratinas</div>
                <p class="service-text">Reconstrucción y sellado de la cutícula capilar para eliminar el frizz, aportar brillo intenso y suavidad duradera.</p>
            </div>
            <div class="service-item" style="border-left-color: #C5A880;">
                <div class="service-name">Taninoplastia y Alisados Capilares</div>
                <p class="service-text">Tratamientos de alisado y disciplina capilar que respetan la estructura del cabello dejando un acabado natural y sedoso.</p>
            </div>
            <div class="service-item" style="border-left-color: #C5A880;">
                <div class="service-name">Botox Capilar y Nutrición Profunda</div>
                <p class="service-text">Acondicionamiento intensivo para recuperar la hidratación, elasticidad y vitalidad del cabello maltratado.</p>
            </div>
        """, unsafe_allow_html=True)

    link_wa_general = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola Priskah, estuve viendo los servicios en tu web y me gustaría consultar disponibilidad.')}"
    st.markdown(f"""
        <div style="text-align: center; margin-top: 10px;">
            <a href="{link_wa_general}" target="_blank" class="wa-btn">
                💬 Consultar disponibilidad por WhatsApp
            </a>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# PESTAÑA 3: CONOCE A LA FUNDADORA
# ==========================================
with tab_fundadora:
    with st.container(border=True):
        # --- FOTO DE LA FUNDADORA ---
        f1, f2, f3 = st.columns([1.3, 1, 1.3])
        with f2:
            try:
                # Asegúrate de subir tu foto con el nombre PRISCILLA.jpeg a tu repositorio
                st.image("PRISCILLA.jpeg", use_container_width=True)
            except:
                pass

        st.markdown("<div style='text-align: center; margin-top: 10px;'><span class='result-badge'>Perfil Profesional y Trayectoria</span></div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title' style='font-size: 28px; text-align: center; margin-bottom: 14px;'>Priscilla Morales Segura</div>", unsafe_allow_html=True)
        
        st.markdown("""
            <p class='result-desc' style='margin-bottom: 16px;'>
                Profesional con sólida trayectoria en entornos multinacionales y gestión empresarial, integrando competencias de <strong>servicio al cliente, planificación, control de calidad y mejora continua</strong> en cada atención personalizada.
            </p>
            <p class='result-desc' style='margin-bottom: 20px;'>
                Como fundadora de <strong>Priskah_m</strong>, combina su formación académica y técnica para ofrecer un servicio ético, seguro y altamente personalizado en bienestar corporal y recuperación capilar, realizando siempre una valoración inicial de necesidades y aplicando estrictos protocolos de higiene y bioseguridad.
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
                <span class="credential-pill">📅 Organización y Gestión Profesional</span>
            </div>
        """, unsafe_allow_html=True)

    link_wa_fundadora = f"https://wa.me/50660218458?text={urllib.parse.quote('Hola, me encantó conocer tu formación y servicios en Priskah_m. Me gustaría agendar una cita.')}"
    st.markdown(f"""
        <div style="text-align: center; margin-top: 10px;">
            <a href="{link_wa_fundadora}" target="_blank" class="wa-btn">
                💬 Agendar valoración por WhatsApp
            </a>
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
