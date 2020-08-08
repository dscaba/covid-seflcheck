import streamlit as st

st.title("COVID-19 SelfCheck")


st.header("Bienvenido al sistema de autodiagnóstico. ")
st.info("**Esta aplicación bajo ningún punto de vista reemplaza la consulta con un profesional. Ante cualquier duda, no deje de consultar con su médico.**")

st.markdown("")

st.markdown("### Seleccione en caso que corresponda")

#Contacto estrecho
if st.checkbox("Contacto estrecho con caso confirmado de COVID-19 (dentro de los 14 días posteriores al contacto)", value=False):
    chk_contacto = 1
else :
    chk_contacto = 0

#Area de riesgo
if st.checkbox("Resida en Areas de riesgo determinadas por el gobierno(ej :AMBA, barrios populares o pueblos originarios)", value=False):
    chk_area = 1
else:
    chk_area = 0

#Personal de salud
if st.checkbox("Personal de salud", value=False):
    chk_personal = 1
else: 
    chk_personal = 0

st.markdown("")
st.markdown("### Seleccione sus síntomas")


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

#Diarrea
if st.checkbox("Diarrea", value=False):
    chk_diarrea = 1
else:
    chk_diarrea = 0

#Vomitos
if st.checkbox("Vomitos", value=False):
    chk_vomitos = 1
else:
    chk_vomitos = 0


#   Criterios


if chk_anosmia + chk_area + chk_contacto + chk_dolor_cabeza + chk_fiebre + chk_odinofagia + chk_personal + chk_resp + chk_tos + chk_vomitos + chk_diarrea >= 2 and chk_anosmia + chk_area + chk_contacto + chk_dolor_cabeza + chk_fiebre + chk_odinofagia + chk_personal + chk_resp + chk_tos + chk_vomitos + chk_diarrea < 12:
    st.error("Sintomas compatibles")


if chk_anosmia + chk_area + chk_contacto + chk_dolor_cabeza + chk_fiebre + chk_odinofagia + chk_personal + chk_resp + chk_tos + chk_vomitos + chk_diarrea == 1:
    st.success("Sintomas insuficientes")

# Sidebar
def main():
    st.sidebar.title("Menú Principal")
    st.sidebar.markdown("### Asistencia")
    

    phone = ["...", "Ministerio de Salud", "CABA", "Buenos Aires", "WhatsApp", ]
    tel = st.sidebar.selectbox("Teléfonos útiles", phone)
    html_temp = """
	<div style="background-color:LIGHTSTEELBLUE;padding:10px;box-shadow: 3px 2px 7px 1px rgba(158,160,183,0.37);">
	<h1 style="color:black;text-align:center;">Ministerio de salud de la Nación</h1>
    <h2 style="color:white;text-align:justify;text-shadow: 1px 2px 2px #708090;">Llamá al 120, es gratuito desde cualquier lugar del país y te atienden las 24 horas.</h2>
	</div>
    """
    
    if tel == "Ministerio de Salud":
        st.markdown(html_temp, unsafe_allow_html=True)
    
    st.sidebar.markdown("### Información")
    options = ["...", "Criterio de caso sospechoso", "Definición de caso confirmado", "Definición de contacto estrecho"]
    choice = st.sidebar.selectbox("Más información", options)
    
if __name__ == '__main__':
    main()
