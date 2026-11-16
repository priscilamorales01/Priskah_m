import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

# 1. Configurar la página
st.set_page_config(page_title="Diagnóstico | Priskah_m", page_icon="🌿", layout="centered")

# --- DISEÑO UX AVANZADO Y ESTÉTICA SPA ---
st.markdown("""
    <style>
    .main {
        background-color: #fcfbf9;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #dcd6cd;
        padding: 10px;
    }
    .stButton>button {
        background-color: #3b4d3e;
        color: white;
        border-radius: 10px;
        font-weight: 600;
        width: 100%;
        padding: 0.75rem;
        font-size: 16px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #2c3a2e;
        color: white;
        box-shadow: 0 6px 8px rgba(0,0,0,0.1);
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #efece6;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGO CENTRADO PERFECTAMENTE ---
col1, col2, col3 = st.columns([1, 1.2, 1])
with col2:
    try:
        st.image("LOGO.jpeg", width=180)
    except:
        pass

st.markdown("<h1 style='text-align: center; color: #2c3a2e; font-family: sans-serif; margin-bottom: 0px;'>Priskah_m</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7a756d; font-size: 15px; margin-top: 5px;'>Bienestar Integral, Cuidado Capilar y Masajes Profesionales</p>", unsafe_allow_html=True)
st.write("---")

# 2. Recolectar datos con mejor UX
st.markdown("### 📝 Tus Datos")
st.markdown("<p style='color: #666; font-size: 13px; margin-top: -10px;'>Completa tus datos para enviarte tu diagnóstico personalizado.</p>", unsafe_allow_html=True)

nombre = st.text_input("Nombre completo", placeholder="Ej: María José Pérez")
telefono = st.text_input("Número de WhatsApp", placeholder="Ej: 60218458")

st.write("---")

# 3. Selección de Categoría Principal
st.markdown("### 🌿 ¿Qué área deseas consentir hoy?")
categoria = st.radio(
    "Selecciona una opción:",
    ["💆‍♀️ Masajes y Bienestar Corporal", "✨ Cuidado Capilar Avanzado"],
    label_visibility="collapsed"
)

st.write("")

# 4. Preguntas detalladas y enriquecidas según la categoría
opcion = ""
if "Masajes" in categoria:
    st.markdown("### 🔍 ¿Cuál es tu objetivo o molestia principal hoy?")
    opcion = st.radio(
        "Selecciona el enfoque que necesitas:",
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
    st.markdown("### 🔍 ¿Cómo se encuentra tu cabello actualmente?")
    opcion = st.radio(
        "Selecciona tu necesidad capilar:",
        [
            "Cabello muy seco, maltratado por tintes/decoloraciones y frizz extremo (Hidratación Profunda)",
            "Busco brillo espejo, nutrición profunda y efecto liso perfecto (Nanoqueratina)",
            "Cuero cabelludo graso, pesado o con acumulación de residuos (Detox Purificante)",
            "Caída frecuente o necesidad de estimular crecimiento nuevo (Anticaída / Raíz)"
        ],
        label_visibility="collapsed"
    )

st.write("---")

# 5. Botón de acción con estilo superior
if st.button("✨ Ver mi Diagnóstico y Recomendación"):
    if nombre.strip() == "" or telefono.strip() == "":
        st.warning("⚠️ Por favor, ingresa tu nombre y número de WhatsApp para continuar.")
    else:
        st.success("¡Excelente! Hemos analizado tu caso. Aquí tienes tu recomendación ideal:")
        
        # Lógica de recomendaciones detalladas
        if "Masajes" in categoria:
            if "Descontracturante" in opcion:
                tratamiento_recomendado = "Masaje Descontracturante Profundo"
                st.info("💆‍♀️ **Tratamiento Sugerido: Masaje Descontracturante.**\n\nTrabaja directamente sobre las capas profundas del músculo para liberar fascias, deshacer nudos rebeldes y devolver la movilidad y el alivio a tu cuerpo.")
            elif "Relajante" in opcion:
                tratamiento_recomendado = "Masaje Relajante Aromaterapia"
                st.info("🌿 **Tratamiento Sugerido: Masaje Relajante.**\n\nCreado para calmar por completo el sistema nervioso, reducir los niveles de estrés y regalarte un espacio de paz y descanso profundo.")
            elif "Drenaje" in opcion:
                tratamiento_recomendado = "Drenaje Linfático / Retorno Venoso"
                st.info("🌊 **Tratamiento Sugerido: Drenaje Linfático.**\n\nTécnica suave y precisa para estimular la circulación, eliminar líquidos retenidos y calmar la pesadez en las piernas.")
            elif "Deportivo" in opcion:
                tratamiento_recomendado = "Masaje Deportivo Especializado"
                st.info("⚡ **Tratamiento Sugerido: Masaje Deportivo.**\n\nIdeal para preparar el tejido muscular ante el esfuerzo o acelerar su recuperación óptima post-entrenamiento.")
            else:
                tratamiento_recomendado = "Masaje Reductivo y Modelador"
                st.info("✨ **Tratamiento Sugerido: Modelado Corporal.**\n\nAyuda a activar la circulación local, movilizar grasa superficial y perfilar la silueta.")
        else:
            if "Nanoqueratina" in opcion:
                tratamiento_recomendado = "Nanoqueratina Capilar Pro"
                st.info("✨ **Tratamiento Sugerido: Nanoqueratina.**\n\nSella la cutícula, elimina el frizz al 100% y aporta un brillo espejo espectacular de larga duración.")
            elif "Hidratación" in opcion:
                tratamiento_recomendado = "Hidratación Capilar Profunda"
                st.info("💧 **Tratamiento Sugerido: Hidratación Intensiva.**\n\nDevuelve la suavidad, elasticidad y nutrición extrema a las hebras maltratadas.")
            elif "Detox" in opcion:
                tratamiento_recomendado = "Detox Purificante Capilar"
                st.info("🍃 **Tratamiento Sugerido: Detox de Cuero Cabelludo.**\n\nLimpia a profundidad, equilibra la grasa natural y revitaliza la salud de tu raíz.")
            else:
                tratamiento_recomendado = "Tratamiento Anticaída y Estimulante"
                st.info("🌱 **Tratamiento Sugerido: Estimulación Capilar.**\n\nActiva el riego sanguíneo en el folículo para fortalecer el cabello y fomentar un crecimiento sano.")

        # 6. Guardar automáticamente en CSV
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
        
        # 7. Botón de WhatsApp rediseñado y elegante
        mi_numero_whatsapp = "50660218458"
        
        mensaje = f"Hola Priskah, soy {nombre}. Realicé el diagnóstico en tu web para {categoria}, mi resultado fue *{tratamiento_recomendado}* y me gustaría agendar una cita."
        mensaje_codificado = urllib.parse.quote(mensaje)
        link_whatsapp = f"https://wa.me/{mi_numero_whatsapp}?text={mensaje_codificado}"
        
        st.markdown(f"""
            <div style="text-align: center; margin-top: 25px; margin-bottom: 15px;">
                <a href="{link_whatsapp}" target="_blank" style="background-color: #25D366; color: white; padding: 14px 28px; border-radius: 10px; text-decoration: none; font-weight: bold; font-size: 16px; display: inline-block; box-shadow: 0 4px 10px rgba(37, 211, 102, 0.3);">
                    💬 Agendar mi cita por WhatsApp
                </a>
            </div>
        """, unsafe_allow_html=True)
        
        st.caption("✨ Tus datos han sido guardados correctamente en sistema.")

st.write("")
st.write("")

# --- PANEL DE CONTROL / VER CLIENTES REGISTRADOS (PROTEGIDO CON CONTRASEÑA) ---
with st.expander("🔒 Panel de Administración (Solo Propietaria)"):
    # Cambia "Priskah2026*" por la contraseña secreta que tú desees
    password_ingresada = st.text_input("Ingresa tu contraseña de administración:", type="password")
    
    if password_ingresada == "Priskah2026*":
        st.success("Contraseña correcta. Aquí tienes los registros:")
        try:
            df_registros = pd.read_csv("clientes_priskah.csv", names=["Fecha", "Nombre", "WhatsApp", "Área", "Selección", "Recomendación"])
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
