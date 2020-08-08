import streamlit as st

st.title("COVID-19 SelfCheck")
st.subheader("Bienvenido al sistema de autodiagnóstico. Por favor seleccione sus síntomas")

#Contacto estrecho
if st.checkbox("Contacto estrecho", value=False):
    chk_contacto = 1
else :
    chk_contacto = 0

#Area de riesgo
if st.checkbox("Contagio en conglomerado(Areas definidas por el gobierno, ej: AMBA)", value=False):
    chk_area = 1
else:
    chk_area = 0

#Personal de salud
if st.checkbox("Personal de salud que reside en áreas con transmisión local de SARS-Cov-2", value=False):
    chk_personal = 1
else: 
    chk_personal = 0

#Fiebre
if st.checkbox("Fiebre (37.5° o más)", value=False):
    chk_fiebre = 1
else:
    chk_fiebre = 0

#Tos
if st.checkbox("Tos", value=False):
    chk_tos = 1
else: 
    chk_tos = 0

#Dolor de cabeza
if st.checkbox("Dolor de cabeza", value=False):
    chk_dolor_cabeza = 1
else:
    chk_dolor_cabeza = 0

#Anosmia
if st.checkbox("Pérdida del sentido del olfato o del gusto", value=False):
    chk_anosmia = 1
else:
    chk_anosmia = 0

#Odinofagia
if st.checkbox("Odinofagia (Dolor de garganta)", value=False):
    chk_odinofagia = 1
else:
    chk_odinofagia = 0

#Dificultad Respiratoria
if st.checkbox("Dificultad Respiratoria", value=False):
    chk_resp = 1
else:
    chk_resp = 0


#   Criterios


if chk_anosmia + chk_area + chk_contacto + chk_dolor_cabeza + chk_fiebre + chk_odinofagia + chk_personal + chk_resp + chk_tos >= 2:
    st.error("Sintomas compatibles")

if chk_anosmia == 1 and chk_area + chk_contacto + chk_dolor_cabeza + chk_fiebre + chk_odinofagia + chk_personal + chk_resp + chk_tos == 0:
    st.warning("Reposo 72hs")

if chk_area + chk_contacto + chk_dolor_cabeza + chk_fiebre + chk_odinofagia + chk_personal + chk_resp + chk_tos == 1:
    st.success("Sintomas insuficientes")