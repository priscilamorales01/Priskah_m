import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

# 1. Configurar la página
st.set_page_config(page_title="Diagnóstico Priskah_m", page_icon="🌿", layout="centered")

# --- ESTILOS VISUALES ELEGANTES ---
st.markdown("""
    <style>
    .main {
        background-color: #faf9f6;
    }
    .stButton>button {
        background-color: #4A5D4E;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        padding: 0.6rem;
    }
    .stButton>button:hover {
        background-color: #3B4B3E;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- CARGAR TU LOGO ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("LOGO.jpeg", width=160)
    except:
        pass

st.markdown("<h1 style='text-align: center; color: #2C3E2D;'>Priskah_m</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Bienestar, Cuidado Capilar y Masajes Profesionales</p>", unsafe_allow_html=True)
st.write("---")

# 2. Recolectar datos del cliente
st.subheader("📝 Tus Datos")
nombre = st.text_input("Nombre completo")
telefono = st.text_input("Número de WhatsApp (ej: 88888888)")

st.write("---")

# 3. Selección de Categoría Principal
st.subheader("🌿 ¿Qué área te gustaría consentir hoy?")
categoria = st.radio(
    "Selecciona una categoría:",
    ["Masajes y Bienestar Corporal", "Cuidado Capilar"]
)

# 4. Preguntas dinámicas según la categoría elegida
opcion = ""
if categoria == "Masajes y Bienestar Corporal":
    st.write("### 💆‍♀️ Selecciona tu necesidad corporal:")
    opcion = st.radio(
        "¿Qué molestia o objetivo tienes?",
        [
            "Tensión severa, nudos o dolor muscular profundo", 
            "Mucho estrés, ansiedad y fatiga mental", 
            "Pesadez en las piernas, mala circulación o retención de líquidos",
            "Recuperación post-ejercicio / Masaje deportivo",
            "Modelado corporal o reducción de medidas"
        ]
    )
else:
    st.write("### ✨ Selecciona tu necesidad capilar:")
    opcion = st.radio(
        "¿Cómo se encuentra tu cabello?",
        [
            "Muy seco, maltratado por químicos y con frizz extremo", 
            "Busco brillo espejo, nutrición y efecto liso (Nanoqueratina)", 
            "Cuero cabelludo graso o con caspa",
            "Caída de cabello o necesidad de estimular crecimiento"
        ]
    )

st.write("---")

# 5. Botón para generar resultado y guardar datos
if st.button("Ver mi diagnóstico y recomendación"):
    if nombre.strip() == "" or telefono.strip() == "":
        st.warning("⚠️ Por favor, llena tu nombre y número de WhatsApp para continuar.")
    else:
        st.success("¡Gracias! Aquí tienes tu recomendación personalizada:")
        
        # Lógica de recomendaciones según la respuesta exacta
        if categoria == "Masajes y Bienestar Corporal":
            if "Tensión severa" in opcion:
                tratamiento_recomendado = "Masaje Descontracturante"
                st.info("💆‍♀️ **Tu tratamiento ideal: Masaje Descontracturante.**\n\nIdeal para liberar fascias, deshacer nudos rebeldes y aliviar la tensión muscular profunda.")
            elif "estrés" in opcion:
                tratamiento_recomendado = "Masaje Relajante"
                st.info("🌿 **Tu tratamiento ideal: Masaje Relajante.**\n\nDiseñado para calmar por completo tu sistema nervioso, reducir el estrés y brindarte un descanso profundo.")
            elif "Pesadez" in opcion:
                tratamiento_recomendado = "Drenaje Linfático / Retorno Venoso"
                st.info("🌊 **Tu tratamiento ideal: Drenaje Linfático / Retorno Venoso.**\n\nEstimula la circulación sanguínea, desinflama y elimina la sensación de pesadez en las piernas.")
            elif "deportivo" in opcion:
                tratamiento_recomendado = "Masaje Deportivo"
                st.info("⚡ **Tu tratamiento ideal: Masaje Deportivo.**\n\nEnfocado en preparar el músculo o acelerar su recuperación tras el esfuerzo físico.")
            else:
                tratamiento_recomendado = "Masaje Reductivo / Modelado"
                st.info("✨ **Tu tratamiento ideal: Masaje Reductivo / Body Contouring.**\n\nAyuda a moldear la silueta y activar la eliminación de toxinas localizadas.")
        else:
            if "Nanoqueratina" in opcion:
                tratamiento_recomendado = "Nanoqueratina Capilar"
                st.info("✨ **Tu tratamiento ideal: Nanoqueratina.**\n\nControla el frizz al 100%, repara la hebra y aporta un brillo espejo espectacular.")
            elif "seco" in opcion:
                tratamiento_recomendado = "Hidratación Capilar Profunda"
                st.info("💧 **Tu tratamiento ideal: Hidratación Profunda con Mascarilla Natural.**\n\nDevuelve la suavidad, la hidratación y la vida a los cabellos maltratados.")
            elif "graso" in opcion:
                tratamiento_recomendado = "Tratamiento Purificante de Cuero Cabelludo"
                st.info("🍃 **Tu tratamiento ideal: Detox Capilar Purificante.**\n\nEquilibra la grasa y limpia a profundidad el cuero cabelludo.")
            else:
                tratamiento_recomendado = "Tratamiento Anticaída y Crecimiento"
                st.info("🌱 **Tu tratamiento ideal: Mascarilla Estimulante (Café y Romero).**\n\nActiva la circulación capilar en la raíz para fortalecer el folículo y estimular el crecimiento.")

        # 6. Guardar los datos automáticamente en tu CSV
        nuevo_registro = pd.DataFrame({
            "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M")],
            "Nombre": [nombre],
            "WhatsApp": [telefono],
            "Área": [categoria],
            "Selección": [opcion],
            "Recomendación": [tratamiento_recomendado]
        })
        
        nuevo_registro.to_csv("clientes_priskah.csv", mode='a', header=False, index=False)
        
        st.write("---")
        
        # 7. Botón directo de WhatsApp para agendar
        # Recuerda cambiar los ceros por tu número real con el código 506 de Costa Rica
        mi_numero_whatsapp = "50600000000" 
        
        mensaje = f"Hola Priskah, soy {nombre}. Hice el diagnóstico en tu web para {categoria}, mi resultado fue *{tratamiento_recomendado}* y quisiera agendar una cita."
        mensaje_codificado = urllib.parse.quote(mensaje)
        link_whatsapp = f"https://wa.me/{mi_numero_whatsapp}?text={mensaje_codificado}"
        
        st.markdown(f"""
            <div style="text-align: center; margin-top: 20px;">
                <a href="{link_whatsapp}" target="_blank" style="background-color: #25D366; color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 16px; display: inline-block;">
                    💬 Agendar mi cita por WhatsApp
                </a>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.caption("✨ Tus datos han sido guardados con éxito.")
