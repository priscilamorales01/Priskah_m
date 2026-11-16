import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configurar la página
st.set_page_config(page_title="Diagnóstico Priskah_m", page_icon="🌿", layout="centered")

# --- CARGAR TU LOGO ---
try:
    st.image("LOGO.jpeg", width=150)
except:
    pass

st.title("🌿 Bienvenida a Priskah_m")
st.subheader("Descubre tu tratamiento ideal")

# 2. Recolectar datos del cliente
st.write("Por favor, déjanos tus datos para enviarte tu diagnóstico:")
nombre = st.text_input("Nombre completo")
telefono = st.text_input("Número de WhatsApp")

# 3. El Test de Bienestar
st.write("---")
st.write("### ¿Qué es lo que más necesita tu cuerpo o cabello hoy?")
opcion = st.radio(
    "Selecciona una opción:",
    [
        "Tensión, dolor muscular o nudos", 
        "Mucho estrés, necesito relajarme", 
        "Pesadez en las piernas o retención de líquidos",
        "Cabello seco, con frizz, maltratado o necesito nanoqueratina"
    ]
)

# 4. Botón para generar resultado y guardar datos
if st.button("Ver mi diagnóstico y enviar"):
    if nombre == "" or telefono == "":
        st.warning("⚠️ Por favor, llena tu nombre y teléfono para continuar.")
    else:
        st.success("¡Gracias! Aquí tienes tu recomendación:")
        
        # Mostrar resultado y definir recomendación
        if opcion == "Tensión, dolor muscular o nudos":
            st.info("💆‍♀️ **Tu tratamiento ideal: Masaje Descontracturante / Terapéutico.**\n\nAyuda a liberar fascias, deshacer nudos y aliviar dolor muscular profundo.")
            tratamiento_recomendado = "Masaje Descontracturante"
        elif opcion == "Mucho estrés, necesito relajarme":
            st.info("💆‍♀️ **Tu tratamiento ideal: Masaje Relajante.**\n\nPerfecto para calmar el sistema nervioso, bajar el estrés y descansar profundamente.")
            tratamiento_recomendado = "Masaje Relajante"
        elif opcion == "Pesadez en las piernas o retención de líquidos":
            st.info("💆‍♀️ **Tu tratamiento ideal: Drenaje Linfático / Retorno Venoso.**\n\nEstimula la circulación, desinflama y quita la sensación de pesadez.")
            tratamiento_recomendado = "Drenaje Linfático"
        elif opcion == "Cabello seco, con frizz, maltratado o necesito nanoqueratina":
            st.info("✨ **Tu tratamiento ideal: Nanoqueratina o Hidratación Profunda.**\n\nDevuelve la suavidad, controla el frizz y le da un brillo espejo a tu hebra.")
            tratamiento_recomendado = "Cuidado Capilar (Nanoqueratina)"

        # 5. Lógica para guardar los datos en tu archivo CSV (Excel)
        nuevo_registro = pd.DataFrame({
            "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M")],
            "Nombre": [nombre],
            "WhatsApp": [telefono],
            "Síntoma": [opcion],
            "Recomendación": [tratamiento_recomendado]
        })
        
        nuevo_registro.to_csv("clientes_priskah.csv", mode='a', header=False, index=False)
        
        st.write("---")
        st.write("✨ **Tus datos han sido guardados.** En breve te contactaremos por WhatsApp para agendar tu cita.")
