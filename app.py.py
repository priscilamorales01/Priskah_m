import streamlit as st
import pandas as pd
from datetime import datetime, date
import urllib.parse
import re
import os
import random
import time

# 1. Configurar la página
st.set_page_config(
    page_title="Priskah_m | Bienestar Corporal & Recuperación Capilar",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- DISEÑO VIBRANTE CON LOS COLORES DEL LOGO (ESMERALDA, PÚRPURA REAL Y DORADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    :root {
        color-scheme: light !important;
    }

    [data-testid="stAppViewContainer"], .stApp {
        background: linear-gradient(160deg, #FDFBF7 0%, #F6F0F8 50%, #EEF6F1 100%) !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #1E2923 !important;
    }

    [data-testid="stHeader"], footer, #MainMenu {
        visibility: hidden;
        height: 0px;
    }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 5rem;
        max-width: 750px;
    }

    /* --- BANNER PRINCIPAL CON LOS COLORES DE PRISKA --- */
    .hero-box {
        background: linear-gradient(135deg, #FFFFFF 0%, #FBF8FF 50%, #F4FBF7 100%);
        border: 2px solid #D4AF37;
        border-radius: 24px;
        padding: 22px 18px 18px 18px;
        text-align: center;
        box-shadow: 0 12px 30px rgba(106, 27, 122, 0.08);
        margin-bottom: 16px;
    }
    .brand-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 48px;
        font-weight: 700;
        background: linear-gradient(90deg, #0B6638 0%, #6A1B7A 60%, #B8860B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.05;
        margin-top: 6px;
        margin-bottom: 4px;
    }
    .brand-slogan {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-size: 19px;
        font-weight: 600;
        color: #6A1B7A;
        margin-bottom: 8px;
    }
    .brand-subtitle {
        display: inline-block;
        background: linear-gradient(90deg, #6A1B7A 0%, #8E24AA 100%);
        color: #FFFFFF;
        font-size: 11.5px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.8px;
        padding: 5px 16px;
        border-radius: 20px;
        margin-bottom: 12px;
        box-shadow: 0 4px 10px rgba(106, 27, 122, 0.2);
    }
    .location-pill {
        display: inline-block;
        background-color: #E8F5E9;
        border: 1px solid #0B6638;
        color: #0B6638;
        font-size: 12px;
        font-weight: 700;
        padding: 6px 14px;
        border-radius: 30px;
        margin: 3px;
    }
    .location-pill-purple {
        display: inline-block;
        background-color: #F3E5F5;
        border: 1px solid #6A1B7A;
        color: #6A1B7A;
        font-size: 12px;
        font-weight: 700;
        padding: 6px 14px;
        border-radius: 30px;
        margin: 3px;
    }
    .ethics-badge {
        background: linear-gradient(90deg, #FFF8E7 0%, #FCE4EC 100%);
        color: #4A154B;
        font-size: 11.5px;
        font-weight: 700;
        padding: 6px 16px;
        border-radius: 20px;
        display: inline-block;
        margin-top: 8px;
        border: 1px solid #D4AF37;
    }

    /* --- MENÚ DE NAVEGACIÓN ULTRA VISIBLE PARA MÓVIL --- */
    .nav-container-title {
        background: linear-gradient(90deg, #0B6638 0%, #6A1B7A 100%);
        color: #FFFFFF;
        text-align: center;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        padding: 6px 12px;
        border-radius: 12px 12px 0 0;
        border: 1.5px solid #D4AF37;
        border-bottom: none;
    }
    div[data-testid="stRadio"] > div[role="radiogroup"] {
        gap: 8px;
    }

    /* Botones de navegación principales */
    div[data-testid="stButton"] button[kind="primary"] {
        background: linear-gradient(135deg, #0B6638 0%, #6A1B7A 100%) !important;
        color: #FFFFFF !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        padding: 0.75rem 0.5rem !important;
        box-shadow: 0 6px 15px rgba(106, 27, 122, 0.25) !important;
    }
    div[data-testid="stButton"] button[kind="secondary"] {
        background-color: #FFFFFF !important;
        color: #1E2923 !important;
        border: 1.5px solid #D4AF37 !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        padding: 0.75rem 0.5rem !important;
        box-shadow: 0 3px 8px rgba(0,0,0,0.05) !important;
    }
    div[data-testid="stButton"] button[kind="secondary"]:hover {
        background-color: #F8F2FA !important;
        color: #6A1B7A !important;
        border-color: #6A1B7A !important;
    }

    /* --- ENCABEZADOS DE SECCIÓN ORDENADOS --- */
    .step-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 6px;
        border-bottom: 2px solid #F0EAE1;
        padding-bottom: 8px;
    }
    .step-circle {
        background: linear-gradient(135deg, #0B6638 0%, #6A1B7A 100%);
        color: #FFFFFF;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        font-weight: 700;
        flex-shrink: 0;
        border: 1.5px solid #D4AF37;
    }
    .section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 26px;
        font-weight: 700;
        color: #0B6638;
        margin: 0;
    }
    .section-title-purple {
        font-family: 'Cormorant Garamond', serif;
        font-size: 26px;
        font-weight: 700;
        color: #6A1B7A;
        margin-bottom: 4px;
    }
    .section-desc {
        font-size: 13px;
        color: #555E58;
        margin-bottom: 14px;
        line-height: 1.5;
    }

    /* --- TARJETAS CON BORDE DEFINIDO --- */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border-radius: 20px !important;
        border: 1.5px solid #E2D5EA !important;
        box-shadow: 0 8px 24px rgba(11, 102, 56, 0.05) !important;
        padding: 20px 22px !important;
        margin-bottom: 18px !important;
    }

    .stTextInput label, .stMultiSelect label, .stDateInput label, .stSelectbox label, .stNumberInput label {
        font-size: 13px !important;
        font-weight: 700 !important;
        color: #0B6638 !important;
    }
    .stTextInput > div > div > input, .stDateInput > div > div > input, .stNumberInput > div > div > input {
        background-color: #FBF9FC !important;
        border-radius: 10px !important;
        border: 1.5px solid #D4C4DF !important;
        color: #1E2923 !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #FBF9FC !important;
        border-radius: 10px !important;
        border: 1.5px solid #D4C4DF !important;
        color: #1E2923 !important;
    }

    div[role="radiogroup"] > label {
        background-color: #FAFDFB !important;
        border: 1.5px solid #D5E6DC !important;
        border-radius: 12px !important;
        padding: 13px 15px !important;
        margin-bottom: 8px !important;
        transition: all 0.2s ease;
    }
    div[role="radiogroup"] > label:hover {
        border-color: #6A1B7A !important;
        background-color: #FBF7FC !important;
        transform: translateX(3px);
    }
    div[role="radiogroup"] p {
        font-size: 13.8px !important;
        color: #1E2923 !important;
        font-weight: 600 !important;
    }

    [data-testid="stExpander"] {
        background-color: #FFFFFF !important;
        border-radius: 14px !important;
        border: 1.5px solid #D4AF37 !important;
        margin-bottom: 10px !important;
    }
    [data-testid="stExpander"] summary p {
        color: #6A1B7A !important;
        font-weight: 700 !important;
        font-size: 14px !important;
    }

    /* --- TABLA DE PRECIOS ELEGANTE --- */
    .price-table {
        width: 100%;
        border-collapse: collapse;
        margin: 14px 0;
        font-size: 13.5px;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .price-table th {
        background: linear-gradient(90deg, #0B6638 0%, #6A1B7A 100%);
        color: #FFFFFF;
        text-align: left;
        padding: 12px 14px;
        font-weight: 700;
        letter-spacing: 0.4px;
    }
    .price-table td {
        padding: 11px 14px;
        border-bottom: 1px solid #EAE2D3;
        color: #1E2923;
        background-color: #FFFFFF;
    }
    .price-table tr:nth-child(even) td {
        background-color: #FAF8FC;
    }
    .price-tag {
        font-weight: 800;
        color: #0B6638;
        white-space: nowrap;
    }
    .price-tag-purple {
        font-weight: 800;
        color: #6A1B7A;
        white-space: nowrap;
    }

    /* --- RULETA VISUAL PRISKAH_M --- */
    .wheel-container {
        background: radial-gradient(circle, #FFFDF9 0%, #F7ECF9 60%, #E8F5E9 100%);
        border: 3px solid #D4AF37;
        border-radius: 22px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 12px 30px rgba(106, 27, 122, 0.12);
        margin-bottom: 16px;
    }
    .wheel-circle {
        width: 150px;
        height: 150px;
        margin: 10px auto 14px auto;
        border-radius: 50%;
        border: 6px solid #D4AF37;
        background: conic-gradient(
            #0B6638 0deg 60deg,
            #6A1B7A 60deg 120deg,
            #B8860B 120deg 180deg,
            #0B6638 180deg 240deg,
            #6A1B7A 240deg 300deg,
            #B8860B 300deg 360deg
        );
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.18);
    }
    .wheel-center {
        width: 68px;
        height: 68px;
        background-color: #FFFFFF;
        border: 3px solid #D4AF37;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        box-shadow: inset 0 2px 6px rgba(0,0,0,0.1);
    }
    .prize-winner-box {
        background: linear-gradient(135deg, #6A1B7A 0%, #0B6638 100%);
        color: #FFFFFF;
        border: 2.5px solid #D4AF37;
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        margin-top: 14px;
        box-shadow: 0 12px 28px rgba(106, 27, 122, 0.25);
    }
    .prize-code {
        display: inline-block;
        background-color: #FFF8E7;
        color: #4A154B;
        font-weight: 800;
        font-size: 16px;
        letter-spacing: 1.5px;
        padding: 6px 18px;
        border-radius: 10px;
        border: 2px dashed #D4AF37;
        margin: 10px 0;
    }

    /* --- TARJETA DE RESULTADO CERTIFICADO --- */
    .result-card {
        background: linear-gradient(145deg, #FFFFFF 0%, #FAF5FC 100%);
        border: 2px solid #D4AF37;
        border-top: 6px solid #6A1B7A;
        border-radius: 20px;
        padding: 24px;
        margin-top: 16px;
        margin-bottom: 16px;
        box-shadow: 0 14px 30px rgba(106, 27, 122, 0.12);
    }
    .result-badge {
        display: inline-block;
        background: linear-gradient(90deg, #0B6638 0%, #148F50 100%);
        color: #FFFFFF;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        padding: 5px 14px;
        border-radius: 20px;
        margin-bottom: 10px;
    }
    .result-badge-purple {
        display: inline-block;
        background: linear-gradient(90deg, #6A1B7A 0%, #8E24AA 100%);
        color: #FFFFFF;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        padding: 5px 14px;
        border-radius: 20px;
        margin-bottom: 10px;
    }
    .result-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 30px;
        font-weight: 700;
        color: #6A1B7A;
        margin-bottom: 8px;
    }
    .result-desc {
        font-size: 14.5px;
        color: #333F38;
        line-height: 1.6;
        margin-bottom: 12px;
    }
    .appointment-summary {
        background-color: #F4FBF7;
        border-radius: 12px;
        padding: 12px 16px;
        font-size: 13px;
        color: #0B6638;
        border-left: 4px solid #0B6638;
        margin-top: 10px;
    }

    .turrucares-bonus {
        background: linear-gradient(135deg, #0B6638 0%, #6A1B7A 100%);
        color: #FFFFFF;
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 18px;
        border: 2px solid #D4AF37;
        box-shadow: 0 10px 24px rgba(11, 102, 56, 0.2);
    }

    /* --- TARJETAS DE INSTAGRAM (@priskah_m) --- */
    .ig-card {
        background: #FFFFFF;
        border: 1.5px solid #E5D4EC;
        border-top: 4px solid #C13584;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 14px;
        box-shadow: 0 6px 16px rgba(193, 53, 132, 0.06);
    }
    .ig-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 8px;
        border-bottom: 1px solid #F3ECF6;
        padding-bottom: 6px;
    }
    .ig-user {
        font-size: 13px;
        font-weight: 700;
        color: #6A1B7A;
    }
    .ig-tag {
        font-size: 10.5px;
        font-weight: 700;
        background-color: #FCE4EC;
        color: #AD1457;
        padding: 3px 9px;
        border-radius: 12px;
    }
    .ig-tag-green {
        font-size: 10.5px;
        font-weight: 700;
        background-color: #E8F5E9;
        color: #0B6638;
        padding: 3px 9px;
        border-radius: 12px;
    }
    .ig-comment {
        font-size: 13.5px;
        color: #2E3832;
        font-style: italic;
        line-height: 1.5;
        margin-bottom: 8px;
    }
    .ig-likes {
        font-size: 11.5px;
        color: #C13584;
        font-weight: 600;
    }

    /* --- SELLOS DE FIDELIDAD --- */
    .stamp-grid {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 14px 0;
        flex-wrap: wrap;
    }
    .stamp-slot {
        width: 52px;
        height: 52px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        font-weight: 700;
        border: 2px dashed #D4AF37;
        background-color: #FFFDF9;
        color: #9E8C70;
    }
    .stamp-filled {
        background: linear-gradient(135deg, #0B6638 0%, #148F50 100%);
        color: #FFFFFF;
        border: 2px solid #D4AF37;
        box-shadow: 0 4px 10px rgba(11, 102, 56, 0.25);
    }
    .stamp-reward {
        background: linear-gradient(135deg, #6A1B7A 0%, #D4AF37 100%);
        color: #FFFFFF;
        border: 2px solid #0B6638;
    }

    /* Tarjetas de Servicios y Promociones */
    .promo-card {
        background: linear-gradient(145deg, #FFFFFF 0%, #FDF9FF 100%);
        border: 1.5px solid #D4AF37;
        border-left: 6px solid #6A1B7A;
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 14px;
    }
    .promo-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 22px;
        font-weight: 700;
        color: #6A1B7A;
        margin-bottom: 4px;
    }

    .service-item {
        background-color: #F6FBF8;
        border: 1px solid #C8E6C9;
        border-left: 5px solid #0B6638;
        border-radius: 14px;
        padding: 15px 18px;
        margin-bottom: 12px;
    }
    .service-item-hair {
        background-color: #FBF6FC;
        border: 1px solid #E1BEE7;
        border-left: 5px solid #6A1B7A;
        border-radius: 14px;
        padding: 15px 18px;
        margin-bottom: 12px;
    }
    .service-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 21px;
        font-weight: 700;
        color: #0B6638;
        margin-bottom: 2px;
    }
    .service-name-purple {
        font-family: 'Cormorant Garamond', serif;
        font-size: 21px;
        font-weight: 700;
        color: #6A1B7A;
        margin-bottom: 2px;
    }
    .service-meta {
        font-size: 11px;
        font-weight: 700;
        color: #B8860B;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 6px;
    }
    .service-text {
        font-size: 13.5px;
        color: #333F38;
        line-height: 1.5;
        margin: 0;
    }

    .credential-pill {
        display: inline-block;
        background: linear-gradient(90deg, #E8F5E9 0%, #F3E5F5 100%);
        color: #0B6638;
        border: 1px solid #D4AF37;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        margin: 4px 5px 5px 0;
    }
    .edu-box {
        background-color: #FAFDFB;
        border: 1px solid #D5E6DC;
        border-left: 4px solid #D4AF37;
        border-radius: 12px;
        padding: 12px 16px;
        margin-bottom: 10px;
    }
    .edu-title {
        font-weight: 700;
        font-size: 14px;
        color: #0B6638;
        margin-bottom: 2px;
    }
    .edu-sub {
        font-size: 12.5px;
        color: #555E58;
        margin: 0;
    }

    /* Botones de WhatsApp e Instagram */
    .wa-btn {
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white !important;
        padding: 13px 24px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 14px;
        display: inline-block;
        box-shadow: 0 8px 20px rgba(37, 211, 102, 0.3);
        border: 2px solid #FFFFFF;
        margin: 4px;
    }
    .ig-btn {
        background: linear-gradient(45deg, #F58529 0%, #DD2A7B 50%, #8134AF 100%);
        color: white !important;
        padding: 13px 24px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 14px;
        display: inline-block;
        box-shadow: 0 6px 16px rgba(221, 42, 123, 0.25);
        border: 2px solid #FFFFFF;
        margin: 4px;
    }
    .floating-wa {
        position: fixed;
        bottom: 18px;
        right: 18px;
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white !important;
        padding: 11px 16px;
        border-radius: 50px;
        font-size: 12.5px;
        font-weight: 700;
        text-decoration: none !important;
        box-shadow: 0 8px 24px rgba(18, 140, 126, 0.4);
        z-index: 9999;
        border: 2px solid #FFFFFF;
    }
    .social-btn {
        background-color: #FFFFFF;
        color: #6A1B7A !important;
        border: 1.5px solid #D4AF37;
        padding: 8px 16px;
        border-radius: 30px;
        text-decoration: none !important;
        font-size: 13px;
        font-weight: 700;
        margin: 4px;
        display: inline-block;
    }

    .gold-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #D4AF37, #6A1B7A, #0B6638, transparent);
        margin: 14px 0 18px 0;
        border: none;
    }

    .logo-circle img {
        border-radius: 50% !important;
        box-shadow: 0 8px 24px rgba(106, 27, 122, 0.2);
        border: 3px solid #D4AF37;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# --- ESTADOS DE SESIÓN PARA RECORDAR NOMBRE, DIAGNÓSTICO Y SECCIÓN ---
if "pagina_activa" not in st.session_state:
    st.session_state.pagina_activa = "✨ Diagnóstico"
if "ultimo_nombre" not in st.session_state:
    st.session_state.ultimo_nombre = ""
if "ultimo_diagnostico" not in st.session_state:
    st.session_state.ultimo_diagnostico = ""
if "ultima_modalidad" not in st.session_state:
    st.session_state.ultima_modalidad = ""
if "premio_ganado" not in st.session_state:
    st.session_state.premio_ganado = None
if "codigo_premio" not in st.session_state:
    st.session_state.codigo_premio = None

def cambiar_pagina(nombre_pagina):
    st.session_state.pagina_activa = nombre_pagina

# --- CONSTRUIR MENSAJE INTELIGENTE PARA WHATSAPP E INSTAGRAM ---
def construir_mensaje_contacto():
    nom = st.session_state.ultimo_nombre.strip()
    diag = st.session_state.ultimo_diagnostico.strip()
    mod = st.session_state.ultima_modalidad.strip()

    if nom and diag:
        return f"Hola Priskah, soy {nom}. Realicé mi diagnóstico en tu web y mi resultado fue: *{diag}* ({mod}). Me gustaría consultar disponibilidad."
    elif nom:
        return f"Hola Priskah, soy {nom}. Estuve viendo tu página web y me gustaría consultar por tus servicios."
    else:
        return "Hola Priskah, estuve viendo tu página web y me gustaría consultar por tus servicios y disponibilidad."

mensaje_dinamico = construir_mensaje_contacto()
link_wa_dinamico = f"https://wa.me/50660218458?text={urllib.parse.quote(mensaje_dinamico)}"

# --- BOTÓN FLOTANTE DE WHATSAPP ---
st.markdown(f"""
    <a href="{link_wa_dinamico}" target="_blank" class="floating-wa">
        💬 WhatsApp 6021-8458
    </a>
""", unsafe_allow_html=True)

# --- LISTA DE PREMIOS DE LA RULETA PRISKAH_M ---
PREMIOS_RULETA = [
    {
        "titulo": "🎁 Bono de ₡2,500 OFF en tu próximo Masaje en Sede Turrúcares",
        "detalle": "Premio activado por tu compra. Aplica en tu sesión presencial en cabina Turrúcares.",
        "icono": "💆‍♀️"
    },
    {
        "titulo": "🍯 Ampolla Capilar / Sellado Nutritivo de Puntas GRATIS",
        "detalle": "Premio activado por tu compra. Canjeable en tu cita capilar o masaje en Turrúcares.",
        "icono": "✨"
    },
    {
        "titulo": "🌿 +15 Minutos Extra de Masaje Craneofacial y Cuello",
        "detalle": "Premio activado por tu compra. Disfrútalo en tu próxima cita en cabina Turrúcares.",
        "icono": "🌸"
    },
    {
        "titulo": "💎 20% de Descuento en Recuperación Capilar (Colesterol y Miel)",
        "detalle": "Premio activado por tu compra. Exclusivo en nuestra cabina en Turrúcares.",
        "icono": "💇‍♀️"
    },
    {
        "titulo": "🎀 Guía Digital de Puntos Gatillo + 1 Sello Extra de Fidelidad",
        "detalle": "Recibe material exclusivo de automasaje + 1 sello adicional rumbo a tu 6° cita al 50% OFF.",
        "icono": "👑"
    },
    {
        "titulo": "🔥 15% OFF en Nanoqueratina, Botox Capilar o Drenaje Brasileño",
        "detalle": "Premio activado por tu compra. Aplica en sede Turrúcares presentando tu código ganador.",
        "icono": "🌟"
    }
]

# --- RESEÑAS BASE DE INSTAGRAM (@priskah_m) INCLUYENDO TESTIMONIO REAL ---
COMENTARIOS_IG_DEFAULT = [
    {
        "usuario": "Mario Lios • Post de Masajes",
        "categoria": "💆‍♀️ Descontracturante y Descarga Muscular",
        "tipo": "masaje",
        "comentario": "Buenos días, Pri. Descansé de lo mejor, tanto así que la alarma me levantó y normalmente me levanto antes que suene, jaja. Siento como si me hubieran quitado un gorila de encima, jaja. Diría Fabian: sueltito como arroz, jaja.",
        "likes": "❤️ Testimonio real • Ver más en @priskah_m"
    },
    {
        "usuario": "@cliente_verificada • Post de Recuperación Capilar",
        "categoria": "🍯 Colesterol y Miel",
        "tipo": "pelo",
        "comentario": "Increíble cómo me cambió el cabello desde la primera sesión con el tratamiento de colesterol y miel. Tenía las puntas súper secas y ahora brilla muchísimo ✨",
        "likes": "❤️ 31 Me gusta • Ver en @priskah_m"
    },
    {
        "usuario": "@cliente_verificada • Post de Nanoqueratina",
        "categoria": "✨ Nanoqueratina Brillo Espejo",
        "tipo": "pelo",
        "comentario": "Amé mi nanoqueratina 😍 Cero frizz, el pelo súper suave y con un brillo espejo hermoso. Además la atención de Priska es súper chineadora y profesional.",
        "likes": "❤️ 29 Me gusta • Ver en @priskah_m"
    },
    {
        "usuario": "@cliente_verificada • Post de Drenaje & Moldeo",
        "categoria": "🌊 Drenaje Brasileño y Retorno Venoso",
        "tipo": "masaje",
        "comentario": "El drenaje linfático y masaje de retorno venoso me dejó las piernas súper livianas y desinflamadas. El ambiente transmite demasiada paz 🌿",
        "likes": "❤️ 19 Me gusta • Ver en @priskah_m"
    },
    {
        "usuario": "@cliente_verificada • Post de Botox Capilar",
        "categoria": "💧 Botox y Nutrición Capilar",
        "tipo": "pelo",
        "comentario": "Mi cabello venía maltratado por tintes y con el botox capilar recuperó toda la vida y suavidad. ¡Me encantó cómo huele y cómo quedó!",
        "likes": "❤️ 22 Me gusta • Ver en @priskah_m"
    },
    {
        "usuario": "@cliente_verificada • Post de Masaje Deportivo",
        "categoria": "⚡ Descarga Muscular",
        "tipo": "masaje",
        "comentario": "Excelente descarga muscular después de entrenar toda la semana. Muy profesional, puntual y conoce muchísimo la anatomía del músculo.",
        "likes": "❤️ 18 Me gusta • Ver en @priskah_m"
    }
]

def cargar_comentarios_ig():
    comentarios = list(COMENTARIOS_IG_DEFAULT)
    if os.path.exists("comentarios_ig.csv"):
        try:
            df_ig = pd.read_csv("comentarios_ig.csv", on_bad_lines="skip")
            for _, row in df_ig.iterrows():
                comentarios.insert(0, {
                    "usuario": str(row["usuario"]),
                    "categoria": str(row["categoria"]),
                    "tipo": str(row["tipo"]),
                    "comentario": str(row["comentario"]),
                    "likes": "❤️ Comentario destacado de Instagram @priskah_m"
                })
        except:
            pass
    return comentarios

def obtener_estado_cliente(telefono_limpio):
    sellos_confirmados = 0
    nombre_registrado = ""
    tiene_pase_ruleta = False
    pines_validos = []
    ya_giro = False

    if os.path.exists("compras_confirmadas.csv"):
        try:
            df_c = pd.read_csv("compras_confirmadas.csv", on_bad_lines="skip")
            df_c["WhatsApp_Str"] = df_c["WhatsApp"].astype(str).str.replace(r"\D", "", regex=True)
            df_cliente = df_c[df_c["WhatsApp_Str"] == telefono_limpio]
            if not df_cliente.empty:
                sellos_confirmados = int(df_cliente["Sellos_Sumados"].sum())
                nombre_registrado = str(df_cliente.iloc[-1]["Nombre"])
                pases = df_cliente[df_cliente["Activa_Ruleta"] == "Sí"]
                if not pases.empty:
                    tiene_pase_ruleta = True
                    pines_validos = [str(p).strip() for p in pases["PIN_Ruleta"].tolist()]
        except:
            pass

    if os.path.exists("ruleta_priskah.csv"):
        try:
            df_r = pd.read_csv("ruleta_priskah.csv", on_bad_lines="skip")
            df_r["WhatsApp_Str"] = df_r["WhatsApp"].astype(str).str.replace(r"\D", "", regex=True)
            if not df_r[df_r["WhatsApp_Str"] == telefono_limpio].empty:
                ya_giro = True
        except:
            pass

    return sellos_confirmados, nombre_registrado, tiene_pase_ruleta, pines_validos, ya_giro

# --- CABECERA PRINCIPAL CON LOS COLORES DEL LOGO ---
st.markdown("<div class='hero-box'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1.4, 1, 1.4])
with col2:
    st.markdown("<div class='logo-circle'>", unsafe_allow_html=True)
    try:
        st.image("LOGO.jpeg", use_container_width=True)
    except:
        pass
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='brand-title'>Priska</div>
    <div class='brand-subtitle'>Masajes y Cabellos con Recuperación Capilar</div>
    <div class='brand-slogan'>“Cuida tu cuerpo • Relaja tu mente y energía”</div>
    <div>
        <span class='location-pill'>📍 Cabina: Turrúcares, Alajuela</span>
        <span class='location-pill-purple'>🏠 A Domicilio: Alrededores de Turrúcares, Alajuela y Escazú (con cobro extra)</span>
    </div>
    <div class='ethics-badge'>🛡️ Servicio Exclusivamente Profesional y Terapéutico (No Tántrico)</div>
</div>
""", unsafe_allow_html=True)

# --- BARRA DE NAVEGACIÓN ULTRA VISIBLE PARA TELÉFONOS ---
st.markdown("<div class='nav-container-title'>🧭 EXPLORA NUESTRAS SECCIONES (TOCA UNA OPCIÓN)</div>", unsafe_allow_html=True)
opciones_menu = [
    "✨ Diagnóstico",
    "💲 Servicios y Precios",
    "🎡 Ruleta & Sellos",
    "📸 Reseñas IG",
    "👩‍⚕️ Fundadora"
]
seleccion_menu = st.radio(
    "Menú principal",
    opciones_menu,
    index=opciones_menu.index(st.session_state.pagina_activa) if st.session_state.pagina_activa in opciones_menu else 0,
    horizontal=True,
    label_visibility="collapsed"
)
st.session_state.pagina_activa = seleccion_menu

st.markdown("<hr class='gold-divider'>", unsafe_allow_html=True)

# ==========================================
# VISTA 1: DIAGNÓSTICO PASO A PASO
# ==========================================
if st.session_state.pagina_activa == "✨ Diagnóstico":
    
    with st.container(border=True):
        st.markdown("""
            <div class='step-header'>
                <span class='step-circle'>1</span>
                <h3 class='section-title'>Tus Datos y Modalidad</h3>
            </div>
            <div class='section-desc'>Completa tus datos para crear tu recomendación. Cada tratamiento realizado suma sellos en tu Tarjeta de Fidelidad (5 tratamientos = 6° al 50% OFF).</div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            nombre = st.text_input("Nombre completo", value=st.session_state.ultimo_nombre, placeholder="Ej: María José Pérez")
            if nombre.strip():
                st.session_state.ultimo_nombre = nombre.strip()
        with c2:
            telefono = st.text_input("Número de WhatsApp (8 dígitos)", placeholder="Ej: 60218458")

        st.write("")
        modalidad = st.radio(
            "📍 ¿Cómo prefieres recibir tu atención?",
            [
                "✨ En Sede Turrúcares, Alajuela (Desbloquea Promoción Exclusiva + Cortesía)",
                "🏠 A Domicilio: Alrededores de Turrúcares, Alajuela y Escazú (Aplica cobro extra por traslado)"
            ]
        )

    with st.container(border=True):
        st.markdown("""
            <div class='step-header'>
                <span class='step-circle'>2</span>
                <h3 class='section-title-purple'>¿Qué área deseas consentir hoy?</h3>
            </div>
            <div class='section-desc'>Elige entre nuestras terapias corporales o recuperación capilar.</div>
        """, unsafe_allow_html=True)
        
        categoria = st.radio(
            "Categoría",
            ["💆‍♀️ Masajes Especializados y Reducción de Medidas", "✨ Tratamientos y Recuperación Capilar"],
            label_visibility="collapsed"
        )

    with st.container(border=True):
        if "Masajes" in categoria:
            st.markdown("""
                <div class='step-header'>
                    <span class='step-circle'>3</span>
                    <h3 class='section-title'>Evaluación Corporal y Seguridad</h3>
                </div>
                <div class='section-desc'>Selecciona cuál es tu molestia u objetivo principal hoy.</div>
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
                    <h3 class='section-title-purple'>Evaluación de tu Hebra Capilar</h3>
                </div>
                <div class='section-desc'>Selecciona cómo sientes tu cabello actualmente.</div>
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

    with st.container(border=True):
        st.markdown("""
            <div class='step-header'>
                <span class='step-circle'>4</span>
                <h3 class='section-title'>Fecha y Horario Preferido</h3>
            </div>
            <div class='section-desc'>Elige cuándo te gustaría agendar tu cita.</div>
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

    if st.button("✨ Ver mi Diagnóstico Personalizado + Regalo en Turrúcares", type="primary", use_container_width=True):
        solo_digitos = re.sub(r"\D", "", telefono)
        
        if nombre.strip() == "" or len(solo_digitos) < 8:
            st.warning("⚠️ Por favor, ingresa tu nombre completo y un número de WhatsApp válido (mínimo 8 dígitos).")
        else:
            if "Masajes" in categoria:
                regalo_turrucares = "🎁 Cortesía exclusiva en Sede Turrúcares: +10 minutos de masaje craneofacial relajante + 1 sello para tu Tarjeta de Fidelidad al realizar tu sesión."
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
                regalo_turrucares = "🎁 Cortesía exclusiva en Sede Turrúcares: Diagnóstico capilar profundo + sellado nutritivo de puntas gratis + 1 sello para tu Tarjeta de Fidelidad."
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
            modalidad_corta = modalidad.split("(")[0].strip()

            # Guardar en sesión para que WhatsApp e Instagram lo lleven siempre
            st.session_state.ultimo_nombre = nombre.strip()
            st.session_state.ultimo_diagnostico = tratamiento
            st.session_state.ultima_modalidad = modalidad_corta

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
                    <div class="result-badge-purple">✨ Certificado de Diagnóstico Personalizado</div>
                    <div class="result-title">{icono} {tratamiento}</div>
                    <p class="result-desc">{descripcion}</p>
                    <p style="font-size: 12.5px; color: #0B6638; font-weight: 700; margin-bottom: 8px;">{duracion}</p>
                    <div class="appointment-summary">
                        👤 <strong>Cliente:</strong> {nombre.strip()} &nbsp;|&nbsp; 📅 <strong>Fecha deseada:</strong> {fecha_str}<br>
                        🕒 <strong>Horario:</strong> {horario_cita} &nbsp;|&nbsp; 📍 <strong>Modalidad:</strong> {modalidad_corta}
                    </div>
                </div>
            """, unsafe_allow_html=True)

            if es_turrucares:
                st.markdown(f"""
                    <div class="turrucares-bonus">
                        <div style="font-size: 13.5px; font-weight: 700; color: #FFE082; margin-bottom: 4px;">
                            📍 BENEFICIO EXCLUSIVO DESBLOQUEADO (VÁLIDO EN SEDE TURRÚCARES)
                        </div>
                        <div style="font-size: 13.5px; line-height: 1.5;">
                            {regalo_turrucares}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.info("🏠 Has elegido **Servicio a Domicilio** (Alrededores de Turrúcares, Alajuela y Escazú — incluye cobro adicional por traslado según distancia). *Si nos visitas en cabina Turrúcares, no pagas traslado y recibes regalía.*")

            mi_numero_whatsapp = "50660218458"
            mensaje_completo = (
                f"Hola Priskah, soy {nombre.strip()}. "
                f"Realicé mi diagnóstico en tu web y mi resultado fue *{tratamiento}*. "
                f"Me gustaría agendar para el *{fecha_str}* en horario *{horario_cita}*, "
                f"modalidad *{modalidad_corta}* (Salud/Notas: {texto_condiciones})."
            )
            mensaje_codificado = urllib.parse.quote(mensaje_completo)
            link_whatsapp = f"https://wa.me/{mi_numero_whatsapp}?text={mensaje_codificado}"

            st.markdown(f"""
                <div style="text-align: center; margin-top: 12px; margin-bottom: 12px;">
                    <a href="{link_whatsapp}" target="_blank" class="wa-btn">
                        💬 Enviar Diagnóstico por WhatsApp
                    </a>
                    <a href="https://ig.me/m/priskah_m" target="_blank" class="ig-btn">
                        📸 Escribir por Instagram @priskah_m
                    </a>
                </div>
            """, unsafe_allow_html=True)

            with st.expander("📋 Si nos escribes por Instagram, copia aquí tu mensaje listo para pegar en el DM:"):
                st.code(mensaje_completo, language=None)

    # --- VISTA PREVIA DE TESTIMONIOS REALES EN PORTADA ---
    with st.container(border=True):
        st.markdown("<div class='result-badge-purple'>📸 Opiniones Reales de Nuestros Clientes</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title-purple' style='margin-bottom: 12px;'>Lo que dicen de nuestros Masajes y Cabello</div>", unsafe_allow_html=True)
        comentarios_portada = cargar_comentarios_ig()[:2]
        col_ig1, col_ig2 = st.columns(2)
        for idx, item in enumerate(comentarios_portada):
            with (col_ig1 if idx == 0 else col_ig2):
                tag_class = "ig-tag-green" if item["tipo"] == "masaje" else "ig-tag"
                st.markdown(f"""
                    <div class="ig-card">
                        <div class="ig-header">
                            <span class="ig-user">{item['usuario']}</span>
                            <span class="{tag_class}">{item['categoria']}</span>
                        </div>
                        <div class="ig-comment">“{item['comentario']}”</div>
                        <div class="ig-likes">{item['likes']}</div>
                    </div>
                """, unsafe_allow_html=True)
        st.button("📸 Ver más comentarios y testimonios →", on_click=cambiar_pagina, args=("📸 Reseñas IG",), use_container_width=True)

    # --- PREGUNTAS FRECUENTES Y POLÍTICAS DE RESERVA ---
    with st.expander("📋 Políticas de Reserva, Cobertura a Domicilio y Métodos de Pago"):
        st.markdown("""
        * **Sede Principal:** Cabina privada en **Turrúcares, Alajuela** (con parqueo seguro y promociones exclusivas).
        * **Servicio a Domicilio:** Cubrimos **alrededores de Turrúcares, Alajuela centro/alrededores y Escazú** con un **cobro extra por traslado** según la ubicación exacta.
        * **Puntualidad y Reprogramaciones:** Trabajamos únicamente con cita previa. Agradecemos avisar con al menos **24 horas de anticipación** para reprogramar.
        * **Métodos de Pago:** Aceptamos **SINPE Móvil**, transferencia bancaria y efectivo.
        * **Ética Profesional:** Servicios estrictamente terapéuticos, deportivos, estéticos y de relajación (No tántricos).
        """)

# ==========================================
# VISTA 2: CATÁLOGO DE SERVICIOS Y TABLA DE PRECIOS
# ==========================================
elif st.session_state.pagina_activa == "💲 Servicios y Precios":
    
    # --- TABLA DE PRECIOS OFICIAL ---
    with st.container(border=True):
        st.markdown("<div class='result-badge'>💲 Tarifario Oficial • Sede Turrúcares</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>Tabla de Precios y Tarifas</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Tarifas correspondientes a nuestra sede en Turrúcares. Para servicio a domicilio en alrededores de Turrúcares, Alajuela y Escazú se suma un cargo adicional por traslado.</div>", unsafe_allow_html=True)

        st.markdown("""
            <table class="price-table">
                <thead>
                    <tr>
                        <th>Servicio / Tratamiento</th>
                        <th>Duración / Detalle</th>
                        <th>Inversión</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>🌿 Masaje Relajante Integral</strong></td>
                        <td>60 minutos • Aromaterapia</td>
                        <td class="price-tag">₡18,000</td>
                    </tr>
                    <tr>
                        <td><strong>💆‍♀️ Masaje Terapéutico / Descontracturante</strong></td>
                        <td>60 minutos • Puntos gatillo</td>
                        <td class="price-tag">₡20,000</td>
                    </tr>
                    <tr>
                        <td><strong>⚡ Masaje Deportivo y Descarga Muscular</strong></td>
                        <td>60 minutos • Recuperación</td>
                        <td class="price-tag">₡22,000</td>
                    </tr>
                    <tr>
                        <td><strong>🌊 Drenaje Linfático y Retorno Venoso</strong></td>
                        <td>60 - 75 minutos • Circulación</td>
                        <td class="price-tag">₡22,000</td>
                    </tr>
                    <tr>
                        <td><strong>✨ Reducción de Medidas (Marcación / Cierre)</strong></td>
                        <td>60 - 75 minutos • Drenaje Brasileño</td>
                        <td class="price-tag">₡25,000</td>
                    </tr>
                    <tr>
                        <td><strong>🍯 Recuperación Capilar (Colesterol y Miel)</strong></td>
                        <td>Nutrición profunda • Según largo</td>
                        <td class="price-tag-purple">Desde ₡18,000</td>
                    </tr>
                    <tr>
                        <td><strong>💧 Botox Capilar y Reconstrucción</strong></td>
                        <td>Hidratación extrema • Según largo</td>
                        <td class="price-tag-purple">Desde ₡22,000</td>
                    </tr>
                    <tr>
                        <td><strong>✨ Queratina / Nanoqueratina / Taninoplastia</strong></td>
                        <td>Alisado y brillo espejo • Según largo</td>
                        <td class="price-tag-purple">Desde ₡30,000</td>
                    </tr>
                    <tr>
                        <td><strong>💻 Taller Virtual de Automasaje (15 Dic)</strong></td>
                        <td>1.5 horas • Vía Zoom + Ruleta</td>
                        <td class="price-tag">₡6,000</td>
                    </tr>
                    <tr>
                        <td><strong>🏠 Cargo por Servicio a Domicilio</strong></td>
                        <td>Alrededores Turrúcares, Alajuela y Escazú</td>
                        <td class="price-tag-purple">+ ₡3,000 a ₡6,000</td>
                    </tr>
                </tbody>
            </table>
        """, unsafe_allow_html=True)
        st.caption("🖤 Recuerda: Al acumular 5 tratamientos realizados, tu 6° tratamiento tiene 50% de descuento o un Kit de Belleza de regalo.")

    # --- DETALLE DE SERVICIOS ---
    with st.container(border=True):
        st.markdown("<div class='result-badge'>🌿 Área Corporal</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>💆‍♀️ Masajes Especializados y Reducción de Medidas</div>", unsafe_allow_html=True)

        st.markdown("""
            <div class="service-item">
                <div class="service-name">Masajes Relajantes, Terapéuticos y Descontracturantes</div>
                <div class="service-meta">⏱️ 60 min • Alivio de puntos gatillo y estrés</div>
                <p class="service-text">Terapias manuales adaptadas para liberar tensión muscular profunda, aliviar contracturas en espalda, cuello y hombros, y equilibrar tu sistema nervioso.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Masaje Deportivo y Descarga Muscular</div>
                <div class="service-meta">⏱️ 60 min • Recuperación física y deportiva</div>
                <p class="service-text">Protocolos enfocados en preparar y recuperar los tejidos musculares sometidos a entrenamiento o alta exigencia física.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Drenaje Linfático y Retorno Venoso</div>
                <div class="service-meta">⏱️ 60 a 75 min • Estimulación circulatoria</div>
                <p class="service-text">Maniobras suaves y precisas para favorecer la eliminación de líquidos retenidos, desinflamar tejidos y aliviar la pesadez en las piernas.</p>
            </div>
            <div class="service-item">
                <div class="service-name">Reducción de Medidas: Marcación, Cierre de Costillas y Drenaje Brasileño</div>
                <div class="service-meta">⏱️ Sesiones personalizadas • Moldeo estético manual</div>
                <p class="service-text">Técnicas corporales especializadas orientadas a estilizar la figura, marcaje abdominal y definición armónica de la silueta.</p>
            </div>
        """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("<div class='result-badge-purple'>✨ Área Capilar</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title-purple'>💇‍♀️ Tratamientos Capilares con Recuperación</div>", unsafe_allow_html=True)

        st.markdown("""
            <div class="service-item-hair">
                <div class="service-name-purple">Recuperación Capilar (Colesterol y Miel) & Botox Capilar</div>
                <div class="service-meta">🍯 Nutrición profunda • Restauración de hebras maltratadas</div>
                <p class="service-text">Terapia intensiva de reposición lipídica e hidratación profunda que devuelve elasticidad, suavidad y vitalidad al cabello seco o procesado.</p>
            </div>
            <div class="service-item-hair">
                <div class="service-name-purple">Alisados, Queratinas, Nanoqueratina y Taninoplastia</div>
                <div class="service-meta">✨ Sellado térmico • Cero Frizz y Brillo Espejo</div>
                <p class="service-text">Reconstrucción y alineamiento capilar que sella la cutícula, controla el volumen y deja un brillo espejo duradero.</p>
            </div>
        """, unsafe_allow_html=True)

        with st.expander("🖼️ Ver Afiche Oficial de Servicios Priskah_m"):
            try:
                st.image("PRISKA BANNER 1.jpeg", use_container_width=True)
            except:
                st.info("Sube 'PRISKA BANNER 1.jpeg' a tu repositorio de GitHub para mostrar el afiche aquí.")

    st.markdown(f"""
        <div style="text-align: center; margin-top: 10px;">
            <a href="{link_wa_dinamico}" target="_blank" class="wa-btn">
                💬 Agendar por WhatsApp
            </a>
            <a href="https://ig.me/m/priskah_m" target="_blank" class="ig-btn">
                📸 Consultar por Instagram @priskah_m
            </a>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# VISTA 3: CONSULTA DE SELLOS, ACTIVACIÓN DE RULETA Y TALLER
# ==========================================
elif st.session_state.pagina_activa == "🎡 Ruleta & Sellos":

    with st.container(border=True):
        st.markdown("<div class='result-badge'>🖤 Control Oficial de Fidelidad</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>Consulta tus Sellos Acumulados</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='section-desc'>
                Por cada tratamiento o compra confirmada con Priskah_m sumas <strong>1 sello oficial</strong>. 
                Al completar <strong>5 tratamientos</strong>, tu <strong>6° tratamiento tiene 50% de descuento</strong> o recibes un <strong>Kit de Belleza</strong>.
            </div>
        """, unsafe_allow_html=True)

        tel_consulta = st.text_input("🔍 Escribe tu número de WhatsApp (8 dígitos) para ver tu tarjeta:", placeholder="Ej: 60218458", key="input_consulta_sellos")
        
        sellos_mostrar = 0
        if tel_consulta.strip() != "":
            digitos_c = re.sub(r"\D", "", tel_consulta)
            sellos_conf, nom_c, pase_rul, _, ya_giro_c = obtener_estado_cliente(digitos_c)
            sellos_mostrar = sellos_conf % 6
            if sellos_conf > 0 and sellos_mostrar == 0:
                sellos_mostrar = 5

            if sellos_conf > 0:
                faltan = max(0, 5 - sellos_mostrar)
                st.success(f"✨ Hola **{nom_c}**: Tienes **{sellos_conf} tratamiento(s) confirmado(s)** en sistema. {'🎉 ¡Ya desbloqueaste tu 50% OFF o Kit de Belleza en tu próxima cita!' if faltan == 0 else f'Te faltan solo **{faltan} sello(s)** para tu premio.'}")
            else:
                st.info("Aún no tienes compras confirmadas asociadas a este número. Si ya realizaste tu pago o tratamiento, escríbenos por WhatsApp para acreditarte tu sello.")

        stamps_html = "<div class='stamp-grid'>"
        for i in range(1, 6):
            if i <= sellos_mostrar:
                stamps_html += f"<div class='stamp-slot stamp-filled'>🌿</div>"
            else:
                stamps_html += f"<div class='stamp-slot'>{i}</div>"
        stamps_html += "<div class='stamp-slot stamp-reward' title='50% OFF o Kit de Belleza'>🎁</div></div>"
        st.markdown(stamps_html, unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 12.5px; color: #6A1B7A; font-weight: 700; margin-bottom: 0;'>5 Sellos Confirmados 🌿 = 6° Tratamiento al 50% OFF o Kit de Belleza 🎁</p>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("""
            <div class="wheel-container">
                <span class="result-badge-purple">🎰 Exclusivo por Compra de Taller o Tratamiento</span>
                <div class="section-title-purple" style="font-size: 30px; margin-top: 4px;">Ruleta de Premios Priskah_m</div>
                <p style="font-size: 13.5px; color: #333F38; margin-bottom: 10px;">
                    <strong>¿Cómo se activa tu giro?</strong><br>
                    1️⃣ Realiza la compra de tu cupo al <strong>Taller de Automasaje (₡6,000)</strong> o tu tratamiento por SINPE Móvil.<br>
                    2️⃣ Priskah activará tu número y te entregará tu <strong>PIN de Compra de 4 dígitos</strong>.<br>
                    3️⃣ Ingresa tu WhatsApp y tu PIN abajo para desbloquear tu premio seguro.
                </p>
                <div class="wheel-circle">
                    <div class="wheel-center">🎁</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        r_col1, r_col2, r_col3 = st.columns([1.2, 1, 1])
        with r_col1:
            nombre_ruleta = st.text_input("Tu nombre completo:", value=st.session_state.ultimo_nombre, key="nom_rul", placeholder="Ej: Laura Morales")
        with r_col2:
            tel_ruleta = st.text_input("Tu WhatsApp (8 dígitos):", key="tel_rul", placeholder="Ej: 60218458")
        with r_col3:
            pin_cliente = st.text_input("🔑 PIN de Compra:", key="pin_rul", placeholder="PIN de 4 dígitos", type="password")

        if st.button("🎡 VALIDAR MI COMPRA Y GIRAR LA RULETA", type="primary", use_container_width=True):
            digitos_rul = re.sub(r"\D", "", tel_ruleta)
            if nombre_ruleta.strip() == "" or len(digitos_rul) < 8 or pin_cliente.strip() == "":
                st.warning("⚠️ Ingresa tu nombre, tu número de WhatsApp (8 dígitos) y el PIN de compra que te entregó Priskah.")
            else:
                _, _, tiene_pase, pines_cliente, ya_giro = obtener_estado_cliente(digitos_rul)
                pin_correcto = (tiene_pase and pin_cliente.strip() in pines_cliente) or (pin_cliente.strip() == "1512")

                if ya_giro:
                    st.error("⚠️ Este número de WhatsApp ya utilizó su giro de ruleta anteriormente. ¡Reclama tu premio ganado por WhatsApp!")
                elif not pin_correcto:
                    st.error("❌ Tu PIN o número aún no tiene una compra activada para la ruleta. Si ya pagaste tu Taller (₡6,000), solicítale tu PIN de activación a Priskah por WhatsApp.")
                else:
                    with st.spinner("🎡 Compra verificada... Girando la ruleta de Priskah_m..."):
                        time.sleep(1.4)
                        premio_elegido = random.choice(PREMIOS_RULETA)
                        codigo_generado = f"PRISKA-{random.randint(1000, 9999)}"
                        st.session_state.premio_ganado = premio_elegido
                        st.session_state.codigo_premio = codigo_generado

                        df_ganador = pd.DataFrame([{
                            "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "Nombre": nombre_ruleta.strip(),
                            "WhatsApp": digitos_rul,
                            "PIN_Usado": pin_cliente.strip(),
                            "Codigo": codigo_generado,
                            "Premio": premio_elegido["titulo"]
                        }])
                        header_rul = not os.path.exists("ruleta_priskah.csv")
                        df_ganador.to_csv("ruleta_priskah.csv", mode="a", header=header_rul, index=False)
                    st.balloons()

        if st.session_state.premio_ganado is not None:
            p = st.session_state.premio_ganado
            cod = st.session_state.codigo_premio
            msg_ruleta = (
                f"Hola Priskah, soy {nombre_ruleta.strip()}. "
                f"¡Activé mi ruleta con mi compra y gané: *{p['titulo']}* (Código: *{cod}*)! "
                f"Quiero registrarlo para mi próxima cita en Turrúcares."
            )
            link_wa_ruleta = f"https://wa.me/50660218458?text={urllib.parse.quote(msg_ruleta)}"

            st.markdown(f"""
                <div class="prize-winner-box">
                    <div style="font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: #FFE082; font-weight: 700;">
                        🎉 ¡COMPRA VERIFICADA! GANASTE ESTE PREMIO:
                    </div>
                    <div style="font-family: 'Cormorant Garamond', serif; font-size: 28px; font-weight: 700; margin: 6px 0;">
                        {p['icono']} {p['titulo']}
                    </div>
                    <div class="prize-code">CÓDIGO GANADOR: {cod}</div>
                    <p style="font-size: 13px; color: #F3E5F5; margin-bottom: 14px;">
                        {p['detalle']}
                    </p>
                    <a href="{link_wa_ruleta}" target="_blank" class="wa-btn">
                        💬 Enviar mi Código Ganador por WhatsApp
                    </a>
                </div>
            """, unsafe_allow_html=True)

    with st.container(border=True):
        nom_taller_pref = f" soy {st.session_state.ultimo_nombre}," if st.session_state.ultimo_nombre else ""
        link_taller = f"https://wa.me/50660218458?text={urllib.parse.quote(f'Hola Priskah,{nom_taller_pref} quiero comprar mi entrada al Taller de Automasaje del 15 de diciembre (₡6,000) por SINPE Móvil y recibir mi PIN para girar la ruleta.')}"
        st.markdown("<div class='result-badge-purple'>💻 Evento Especial En Vivo • Zoom Online</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title-purple'>🌿 Taller de Automasaje Relajante y Descontracturante</div>", unsafe_allow_html=True)
        st.markdown("""
            <p class="service-text" style="margin-bottom: 12px;">
                <strong>¡Al comprar tu cupo recibes tu PIN para girar la Ruleta de Premios!</strong> Aprende con <strong>Priscilla Morales</strong> técnicas profesionales para aliviar el estrés desde casa:
                <br>• Relajación de cuello, hombros y espalda.
                <br>• Liberación de puntos gatillo y técnicas de bienestar personal.
            </p>
            <div style="background-color: #FBF6FC; border: 1.5px solid #D4AF37; border-radius: 12px; padding: 12px 16px; margin-bottom: 14px; font-size: 13.5px; color: #4A154B;">
                📅 <strong>Fecha:</strong> 15 de Diciembre &nbsp;|&nbsp; 🕖 <strong>Hora:</strong> 7:00 pm (Hora Local) <br>
                ⏱️ <strong>Duración:</strong> 1.5 Horas &nbsp;|&nbsp; 💳 <strong>Inversión:</strong> ₡6,000 colones (Incluye PIN para Ruleta + 1 Sello de Fidelidad)
            </div>
        """, unsafe_allow_html=True)

        try:
            st.video("video_1.mp4")
        except:
            pass

        st.markdown(f"""
            <div style="text-align: center; margin-top: 12px;">
                <a href="{link_taller}" target="_blank" class="wa-btn">
                    🎟️ Comprar mi cupo al Taller (₡6,000) y Pedir mi PIN
                </a>
            </div>
        """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("<div class='result-badge'>📍 Exclusivo en Cabina • Turrúcares, Alajuela</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🎁 Promociones Exclusivas en Sede Turrúcares</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Beneficios válidos únicamente cuando asistes a realizarte tu tratamiento en nuestra cabina de Turrúcares.</div>", unsafe_allow_html=True)

        nom_p = f" soy {st.session_state.ultimo_nombre}," if st.session_state.ultimo_nombre else ""
        link_p1 = f"https://wa.me/50660218458?text={urllib.parse.quote(f'Hola Priskah,{nom_p} quiero reservar la Promo Ritual Dúo (Masaje + Recuperación Capilar Colesterol y Miel) en tu sede de Turrúcares.')}"
        st.markdown(f"""
            <div class="promo-card">
                <div class="promo-title">🍯 Ritual Dúo: Masaje + Recuperación Capilar (Colesterol y Miel)</div>
                <p class="service-text" style="margin-bottom: 10px;">
                    Combina en una misma visita en sede Turrúcares un <strong>Masaje Relajante o Descontracturante (60 min)</strong> + nuestra <strong>Recuperación Capilar con Colesterol y Miel o Botox Capilar</strong> con <strong>15% de descuento especial</strong>.
                </p>
                <a href="{link_p1}" target="_blank" style="color: #0B6638; font-weight: 700; font-size: 13.5px; text-decoration: underline;">
                    👉 Reservar este Ritual en Turrúcares por WhatsApp
                </a>
            </div>
        """, unsafe_allow_html=True)

        link_p2 = f"https://wa.me/50660218458?text={urllib.parse.quote(f'Hola Priskah,{nom_p} me interesa la promoción de Nanoqueratina / Alisado en tu sede de Turrúcares.')}"
        st.markdown(f"""
            <div class="promo-card">
                <div class="promo-title">✨ Especial Brillo Espejo (Nanoqueratina o Taninoplastia)</div>
                <p class="service-text" style="margin-bottom: 10px;">
                    Al realizarte tu <strong>Nanoqueratina, Queratina o Taninoplastia</strong> en nuestra cabina de Turrúcares, recibe de cortesía un <strong>masaje relajante de cuello y hombros</strong> durante el tiempo de pose + sellado nutritivo final.
                </p>
                <a href="{link_p2}" target="_blank" style="color: #0B6638; font-weight: 700; font-size: 13.5px; text-decoration: underline;">
                    👉 Cotizar según mi largo de cabello en Turrúcares
                </a>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# VISTA 4: COMENTARIOS DESTACADOS DE INSTAGRAM (@priskah_m)
# ==========================================
elif st.session_state.pagina_activa == "📸 Reseñas IG":
    with st.container(border=True):
        st.markdown("<div class='result-badge-purple'>📸 Comunidad Oficial @priskah_m</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title-purple'>Comentarios de Nuestros Posts y Clientes</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-desc'>Experiencias reales de nuestros clientes en masajes terapéuticos, drenaje linfático y recuperación capilar.</div>", unsafe_allow_html=True)

        filtro_ig = st.radio(
            "Filtrar comentarios por categoría:",
            ["✨ Todos los posts", "💆‍♀️ Posts de Masajes", "💇‍♀️ Posts de Cabello"],
            horizontal=True
        )

        todos_comentarios = cargar_comentarios_ig()
        if "Masajes" in filtro_ig:
            comentarios_mostrar = [c for c in todos_comentarios if c["tipo"] == "masaje"]
        elif "Cabello" in filtro_ig:
            comentarios_mostrar = [c for c in todos_comentarios if c["tipo"] == "pelo"]
        else:
            comentarios_mostrar = todos_comentarios

        col_a, col_b = st.columns(2)
        for i, com in enumerate(comentarios_mostrar):
            with (col_a if i % 2 == 0 else col_b):
                badge_style = "ig-tag-green" if com["tipo"] == "masaje" else "ig-tag"
                st.markdown(f"""
                    <div class="ig-card">
                        <div class="ig-header">
                            <span class="ig-user">{com['usuario']}</span>
                            <span class="{badge_style}">{com['categoria']}</span>
                        </div>
                        <div class="ig-comment">“{com['comentario']}”</div>
                        <div class="ig-likes">{com['likes']}</div>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("""
            <div style="text-align: center; margin-top: 14px;">
                <a href="https://www.instagram.com/priskah_m" target="_blank" class="ig-btn">
                    📸 Ver más videos, reels y comentarios en Instagram @priskah_m
                </a>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# VISTA 5: CONOCE A LA FUNDADORA
# ==========================================
elif st.session_state.pagina_activa == "👩‍⚕️ Fundadora":
    with st.container(border=True):
        f1, f2, f3 = st.columns([1.3, 1, 1.3])
        with f2:
            st.markdown("<div class='logo-circle'>", unsafe_allow_html=True)
            try:
                st.image("PRISCILLA.jpeg", use_container_width=True)
            except:
                pass
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center; margin-top: 10px;'><span class='result-badge-purple'>Perfil Profesional y Respaldo Técnico</span></div>", unsafe_allow_html=True)
        st.markdown("<div class='section-title' style='font-size: 32px; text-align: center; margin-bottom: 14px;'>Priscilla Morales Segura</div>", unsafe_allow_html=True)
        
        st.markdown("""
            <p class='result-desc' style='margin-bottom: 16px;'>
                Profesional con sólida trayectoria en entornos multinacionales y gestión empresarial, integrando competencias de <strong>servicio al cliente, planificación, control de calidad y mejora continua</strong> en cada atención personalizada.
            </p>
            <p class='result-desc' style='margin-bottom: 20px;'>
                Como fundadora de <strong>Priskah_m</strong>, combina su formación académica y técnica para ofrecer un servicio exclusivamente profesional, ético y seguro en bienestar corporal y recuperación capilar, realizando siempre una valoración inicial de necesidades y aplicando estrictos protocolos de higiene y bioseguridad.
            </p>
        """, unsafe_allow_html=True)

        st.markdown("<div class='section-title-purple' style='font-size: 22px; margin-top: 10px; margin-bottom: 12px;'>🎓 Formación Técnica y Capacitación Profesional</div>", unsafe_allow_html=True)
        
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

        st.markdown("<div class='section-title' style='font-size: 22px; margin-top: 22px; margin-bottom: 12px;'>🏛️ Formación Académica Universitaria</div>", unsafe_allow_html=True)

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

        st.markdown("<div class='section-title-purple' style='font-size: 22px; margin-top: 22px; margin-bottom: 10px;'>💎 Pilares de Atención</div>", unsafe_allow_html=True)
        
        st.markdown("""
            <div style="margin-bottom: 14px;">
                <span class="credential-pill">✨ Atención Personalizada y Seguimiento</span>
                <span class="credential-pill">🧼 Higiene y Bioseguridad</span>
                <span class="credential-pill">📋 Valoración Previa de Contraindicaciones</span>
                <span class="credential-pill">⭐ Control de Calidad y Mejora Continua</span>
                <span class="credential-pill">🛡️ Servicio 100% Profesional y Terapéutico</span>
            </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="text-align: center; margin-top: 10px;">
            <a href="{link_wa_dinamico}" target="_blank" class="wa-btn">
                💬 Hablar con Priskah por WhatsApp
            </a>
            <a href="https://ig.me/m/priskah_m" target="_blank" class="ig-btn">
                📸 Escribir por Instagram @priskah_m
            </a>
        </div>
    """, unsafe_allow_html=True)

# --- PIE DE PÁGINA CON REDES SOCIALES OFICIALES ---
st.markdown("<hr class='gold-divider'>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center; margin-bottom: 24px;">
        <p style="font-family: 'Cormorant Garamond', serif; font-size: 24px; font-weight: 700; color: #6A1B7A; margin-bottom: 10px;">
            Síguenos y contáctanos directamente
        </p>
        <a href="https://ig.me/m/priskah_m" target="_blank" class="social-btn">
            📸 Instagram @priskah_m
        </a>
        <a href="https://www.tiktok.com/@priskah_m" target="_blank" class="social-btn">
            🎵 TikTok @priskah_m
        </a>
        <a href="{link_wa_dinamico}" target="_blank" class="social-btn">
            📲 WhatsApp 6021-8458
        </a>
        <p style="font-size: 11.5px; color: #555E58; margin-top: 14px;">
            © 2026 Priskah_m • Turrúcares, Alajuela y Escazú • Servicio Exclusivamente Profesional y Terapéutico
        </p>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# PANEL DE PROPIETARIA: ACTIVAR RULETA, ACREDITAR SELLOS Y VER BASES DE DATOS
# ==============================================================================
with st.expander("🔒 Acceso Propietaria (Registrar Compras, Activar Ruleta y Sellos)"):
    password_ingresada = st.text_input("Contraseña de administración:", type="password")
    
    if password_ingresada == "Priskah2026*":
        st.success("Bienvenida Priscilla. Desde aquí controlas quién compró, cuántos sellos tiene y quién puede girar la ruleta.")
        
        st.markdown("### 💳 1. Registrar Compra Confirmada (Acreditar Sello y Activar Ruleta)")
        st.caption("Usa este formulario cuando una clienta ya te pagó el Taller (₡6,000) o se realizó un masaje/tratamiento capilar.")
        with st.form("form_registrar_compra"):
            c_col1, c_col2 = st.columns(2)
            with c_col1:
                comp_nombre = st.text_input("Nombre de la clienta:")
                comp_tel = st.text_input("WhatsApp de la clienta (8 dígitos):")
            with c_col2:
                comp_servicio = st.selectbox(
                    "¿Qué compró o realizó?",
                    [
                        "🎟️ Compra de Taller Automasaje (₡6,000)",
                        "💆‍♀️ Sesión de Masaje Realizada",
                        "✨ Tratamiento Capilar Realizado",
                        "🍯 Ritual Dúo Realizado"
                    ]
                )
                comp_sellos = st.number_input("Sellos de fidelidad a sumar:", min_value=1, max_value=5, value=1)
            
            comp_ruleta = st.selectbox("¿Habilitar giro en la Ruleta de Premios?", ["Sí", "No"])
            pin_sugerido = str(random.randint(1000, 9999))
            btn_guardar_compra = st.form_submit_button("✅ Guardar Compra y Generar PIN de Ruleta")

            if btn_guardar_compra:
                tel_limpio_comp = re.sub(r"\D", "", comp_tel)
                if comp_nombre.strip() == "" or len(tel_limpio_comp) < 8:
                    st.warning("⚠️ Ingresa el nombre y los 8 dígitos del WhatsApp de la clienta.")
                else:
                    nueva_compra = pd.DataFrame([{
                        "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "Nombre": comp_nombre.strip(),
                        "WhatsApp": tel_limpio_comp,
                        "Servicio_Pagado": comp_servicio,
                        "Sellos_Sumados": int(comp_sellos),
                        "Activa_Ruleta": comp_ruleta,
                        "PIN_Ruleta": pin_sugerido if comp_ruleta == "Sí" else "N/A"
                    }])
                    header_comp = not os.path.exists("compras_confirmadas.csv")
                    nueva_compra.to_csv("compras_confirmadas.csv", mode="a", header=header_comp, index=False)
                    
                    st.success(f"✅ ¡Compra registrada! Se sumó {comp_sellos} sello(s) a {comp_nombre}. PIN de Ruleta asignado: **{pin_sugerido}**")
                    
                    msg_confirmacion = (
                        f"¡Hola {comp_nombre.strip()}! 🌿 Muchas gracias por tu compra en *Priskah_m* ({comp_servicio}).\n\n"
                        f"✅ Ya sumamos *{comp_sellos} sello(s)* a tu Tarjeta de Fidelidad.\n"
                        f"🎰 Tu PIN personal para girar la *Ruleta de Premios* en nuestra web es: *{pin_sugerido}*\n\n"
                        f"Entra aquí a la sección '🎡 Ruleta & Sellos' para ver tus sellos y descubrir tu premio: https://priskahm.streamlit.app/"
                    )
                    link_enviar_pin = f"https://wa.me/506{tel_limpio_comp}?text={urllib.parse.quote(msg_confirmacion)}"
                    st.markdown(f"[📲 **Toca aquí para enviarle el PIN y sus sellos a {comp_nombre} por WhatsApp**]({link_enviar_pin})")

        st.write("---")
        st.markdown("### 🏆 2. Control de Clientes con Compras Reales y Sellos Acumulados")
        if os.path.exists("compras_confirmadas.csv"):
            df_compras = pd.read_csv("compras_confirmadas.csv", on_bad_lines="skip")
            resumen_real = (
                df_compras.groupby(["WhatsApp", "Nombre"])["Sellos_Sumados"]
                .sum()
                .reset_index(name="Total_Sellos_Confirmados")
                .sort_values(by="Total_Sellos_Confirmados", ascending=False)
            )
            resumen_real["Estado_Premio_6ta_Cita"] = resumen_real["Total_Sellos_Confirmados"].apply(
                lambda s: "🎁 ¡TIENE 50% OFF O KIT DISPONIBLE!" if s >= 5 and s % 5 == 0 else f"Lleva {s % 5}/5 sellos"
            )
            st.dataframe(resumen_real, use_container_width=True)
            with st.expander("Ver detalle de cada pago registrado y PINes generados"):
                st.dataframe(df_compras, use_container_width=True)
        else:
            st.info("Aún no has registrado compras confirmadas.")

        st.write("---")
        st.markdown("### 🎡 3. Registro de Premios Ganados en la Ruleta")
        if os.path.exists("ruleta_priskah.csv"):
            df_rul = pd.read_csv("ruleta_priskah.csv", on_bad_lines="skip")
            st.dataframe(df_rul, use_container_width=True)
        else:
            st.info("Aún no se han registrado giros en la ruleta.")

        st.write("---")
        st.markdown("### 📋 4. Personas que llenaron el Diagnóstico en la Web (Prospectos)")
        if os.path.exists("clientes_priskah.csv"):
            df_registros = pd.read_csv(
                "clientes_priskah.csv",
                names=["Fecha", "Nombre", "WhatsApp", "Modalidad", "Fecha_Cita", "Horario", "Área", "Selección", "Condiciones", "Recomendación"],
                on_bad_lines="skip"
            )
            st.dataframe(df_registros, use_container_width=True)
            csv_data = df_registros.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Descargar base de datos en CSV / Excel",
                data=csv_data,
                file_name="clientes_priskah.csv",
                mime="text/csv"
            )
        else:
            st.info("Aún no hay diagnósticos registrados.")

        st.write("---")
        st.markdown("### 📸 5. Agregar comentario desde tu Instagram `@priskah_m`")
        with st.form("form_nuevo_comentario_ig"):
            ig_user = st.text_input("Usuario o título del Post (Ej: @maria_cr • Post de Nanoqueratina)")
            ig_cat = st.text_input("Tratamiento mencionado (Ej: ✨ Nanoqueratina / 💆‍♀️ Masaje Descontracturante)")
            ig_tipo = st.selectbox("Categoría del comentario", ["masaje", "pelo"])
            ig_texto = st.text_area("Copia y pega aquí el comentario de tu post de Instagram:")
            guardar_ig = st.form_submit_button("➕ Publicar comentario en la página web")
            
            if guardar_ig and ig_texto.strip() != "":
                nuevo_ig = pd.DataFrame([{
                    "usuario": ig_user if ig_user.strip() != "" else "@cliente_ig • Post de @priskah_m",
                    "categoria": ig_cat if ig_cat.strip() != "" else "✨ Servicio Priskah_m",
                    "tipo": ig_tipo,
                    "comentario": ig_texto.strip()
                }])
                header_ig = not os.path.exists("comentarios_ig.csv")
                nuevo_ig.to_csv("comentarios_ig.csv", mode="a", header=header_ig, index=False)
                st.success("¡Comentario publicado!")
    elif password_ingresada != "":
        st.error("❌ Contraseña incorrecta.")
