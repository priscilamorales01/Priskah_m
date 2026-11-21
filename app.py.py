import streamlit as st

# 1. Configuración inicial de la página
st.set_page_config(
    page_title="Priskah_m | Bienestar y Cuidado Capilar",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed" # Mantiene limpia la vista en móvil al usar menú superior
)

# 2. Estilos personalizados (Paleta minimalista: blanco, beige, verde salvia y rosa suave)
st.markdown("""
<style>
    /* Fondo general y tipografía limpia */
    .stApp {
        background-color: #FAF8F5;
        color: #3D3D3D;
    }

    /* Caja destacada para el menú de navegación */
    .menu-header {
        background-color: #FFFFFF;
        padding: 14px 18px;
        border-radius: 14px;
        border: 1px solid #EAE4DC;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        margin-bottom: 12px;
        text-align: center;
    }

    /* Estilizado de las píldoras (st.pills) para que parezcan botones de menú claros */
    div[data-testid="stPills"] {
        display: flex;
        justify-content: center;
        gap: 8px;
    }
    
    div[data-testid="stPills"] button {
        border-radius: 20px !important;
        border: 1px solid #D5CEC4 !important;
        background-color: #FFFFFF !important;
        color: #4A4A4A !important;
        font-weight: 600 !important;
        padding: 6px 14px !important;
        transition: all 0.2s ease-in-out;
    }

    div[data-testid="stPills"] button:hover {
        border-color: #8FA998 !important;
        background-color: #F2F6F4 !important;
    }

    /* Botón de la sección activa */
    div[data-testid="stPills"] button[aria-checked="true"] {
        background-color: #8FA998 !important; /* Verde salvia */
        color: #FFFFFF !important;
        border-color: #7A9684 !important;
        box-shadow: 0 2px 6px rgba(143, 169, 152, 0.4);
    }

    /* Tarjetas de contenido */
    .card-priska {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #EAE4DC;
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Control de estado para permitir navegar desde botones internos
opciones_menu = [
    "✨ Inicio",
    "💆‍♀️ Masajes",
    "💇‍♀️ Cabello",
    "📋 Diagnóstico",
    "⭐ Reseñas",
    "🎁 Ruleta"
]

if "menu_activo" not in st.session_state:
    st.session_state.menu_activo = "✨ Inicio"

def cambiar_seccion(nueva_seccion):
    st.session_state.menu_activo = nueva_seccion

# 4. Encabezado de marca
st.markdown("""
<div style="text-align: center; padding-bottom: 5px;">
    <h1 style="margin-bottom: 0; color: #2E3A34; font-size: 2.1rem;">Priskah_m</h1>
    <p style="color: #7A746E; font-size: 0.95rem; margin-top: 4px;">
        Terapia Corporal Profesional & Recuperación Capilar
    </p>
</div>
""", unsafe_allow_html=True)

# 5. Menú visual e intuitivo (se adapta en varias filas en celular sin ocultar opciones)
st.markdown("""
<div class="menu-header">
    <span style="font-size: 0.9rem; font-weight: 600; color: #5C6B62;">
        👇 Toca una sección para explorar nuestros servicios y beneficios:
    </span>
</div>
""", unsafe_allow_html=True)

seleccion = st.pills(
    label="Menú de navegación",
    options=opciones_menu,
    default=st.session_state.menu_activo,
    selection_mode="single",
    label_visibility="collapsed",
    key="pills_navegacion"
)

# Sincronizar selección manual del usuario con el estado de sesión
if seleccion and seleccion != st.session_state.menu_activo:
    st.session_state.menu_activo = seleccion

st.divider()

# ==============================================================================
# 6. CONTENIDO DINÁMICO SEGÚN LA PESTAÑA SELECCIONADA
# ==============================================================================

if st.session_state.menu_activo == "✨ Inicio":
    st.markdown("""
    <div class="card-priska">
        <h3 style="margin-top:0; color:#2E3A34;">Bienvenida a tu espacio de bienestar 🌿</h3>
        <p>En <b>Priskah_m</b> combinamos técnicas profesionales de masaje terapéutico y deportivo con tratamientos avanzados de recuperación capilar.</p>
        <p style="font-size: 0.85rem; color: #6E6A66; background-color: #F7F4F0; padding: 8px 12px; border-radius: 8px;">
            ℹ️ <i>Nota: Todos nuestros servicios de masaje son estrictamente profesionales, terapéuticos y estéticos (no tántricos).</i>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🧭 ¿Qué te gustaría hacer hoy? (Accesos directos)")
    col1, col2 = st.columns(2)
    with col1:
        st.button("💆‍♀️ Ver Masajes", use_container_width=True, on_click=cambiar_seccion, args=("💆‍♀️ Masajes",))
        st.button("📋 Hacer Diagnóstico", use_container_width=True, on_click=cambiar_seccion, args=("📋 Diagnóstico",))
    with col2:
        st.button("💇‍♀️ Ver Tratamientos Capilares", use_container_width=True, on_click=cambiar_seccion, args=("💇‍♀️ Cabello",))
        st.button("🎁 Girar Ruleta de Premios", use_container_width=True, on_click=cambiar_seccion, args=("🎁 Ruleta",))

elif st.session_state.menu_activo == "💆‍♀️ Masajes":
    st.subheader("💆‍♀️ Masajes Terapéuticos, Deportivos y Estéticos")
    st.write("Aquí va tu catálogo de masajes (descontracturante, deportivo, drenaje linfático, moldeo brasileño, etc.).")
    # Pega aquí tu código actual de la pestaña de Masajes

elif st.session_state.menu_activo == "💇‍♀️ Cabello":
    st.subheader("💇‍♀️ Tratamientos y Recuperación Capilar")
    st.write("Aquí va tu catálogo capilar (alisados, nano-keratina, botox capilar, células madre, miel y colesterol).")
    # Pega aquí tu código actual de la pestaña de Cabello

elif st.session_state.menu_activo == "📋 Diagnóstico":
    st.subheader("📋 Test de Diagnóstico Personalizado")
    st.write("Aquí va tu cuestionario interactivo para recomendar el masaje o tratamiento ideal.")
    # Pega aquí tu código actual del Diagnóstico

elif st.session_state.menu_activo == "⭐ Reseñas":
    st.subheader("⭐ Experiencias de Nuestros Clientes")
    st.write("Aquí van tus capturas o testimonios de Instagram y sellos de lealtad.")
    # Pega aquí tu código actual de Reseñas / Lealtad

elif st.session_state.menu_activo == "🎁 Ruleta":
    st.subheader("🎁 Ruleta Promocional Priskah_m")
    st.write("Aquí va tu ruleta de premios y promociones.")
    # Pega aquí tu código actual de la Ruleta
