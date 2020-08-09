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
    st.error(" Usted posee sintomas compatibles. Por favor consulte con su médico")


if chk_anosmia + chk_area + chk_contacto + chk_dolor_cabeza + chk_fiebre + chk_odinofagia + chk_personal + chk_resp + chk_tos + chk_vomitos + chk_diarrea == 1:
    st.success("Usted no presenta síntomas compatibles")

# Sidebar
def main():
   
    st.sidebar.title("Menú Principal")
    st.sidebar.markdown("### Asistencia")
    

    phone = ["...", "Ministerio de Salud", "CABA", "Buenos Aires", "WhatsApp", ]
    tel = st.sidebar.selectbox("Teléfonos útiles", phone)
    
    #Cuadros HTML tel
    #Min Salud
    html_temp = """
	<div style="background-color:LIGHTSTEELBLUE;padding:10px;box-shadow: 3px 2px 7px 1px rgba(158,160,183,0.37);">
	<h1 style="color:black;text-align:center;">Ministerio de salud de la Nación</h1>
    <h2 style="color:white;text-align:justify;text-shadow: 1px 2px 2px #708090;">Llamá al 120, es gratuito desde cualquier lugar del país y te atienden las 24 horas.</h2>
	</div>
    """
    #CABA
    html_temp_caba = """
	<div style="background-color:LIGHTSTEELBLUE;padding:10px;box-shadow: 3px 2px 7px 1px rgba(158,160,183,0.37);">
	<h1 style="color:black;text-align:center;">Ciudad Autónoma de Buenos Aires</h1>
    <h2 style="color:white;text-align:justify;text-shadow: 1px 2px 2px #708090;">   Llamá al 107.</h2>
	</div>
    """

    #Buenos Aires
    html_temp_bsas = """
	<div style="background-color:LIGHTSTEELBLUE;padding:10px;box-shadow: 3px 2px 7px 1px rgba(158,160,183,0.37);">
	<h1 style="color:black;text-align:center;">Provincia de Buenos Aires</h1>
    <h2 style="color:white;text-align:justify;text-shadow: 1px 2px 2px #708090;">Llamá al 148.</h2>
	</div>
    """

    #wPP
    html_temp_wpp = """
	<div style="background-color:LIGHTSTEELBLUE;padding:10px;box-shadow: 3px 2px 7px 1px rgba(158,160,183,0.37);">
	<h1 style="color:black;text-align:center;">WhatsApp</h1>
    <h2 style="color:white;text-align:justify;text-shadow: 1px 2px 2px #708090;">Escribí "Hola" (sin comillas) al número +54 9 11 2256-0566 y comenzá a chatear..</h2>
	</div>
    """

    if tel == "Ministerio de Salud":
        st.markdown(html_temp, unsafe_allow_html=True)
    
    if tel == "CABA":
        st.markdown(html_temp_caba, unsafe_allow_html=True)
    
    if tel == "Buenos Aires":
        st.markdown(html_temp_bsas, unsafe_allow_html=True)

    if tel == "WhatsApp":
        st.markdown(html_temp_wpp, unsafe_allow_html=True)
    
    st.sidebar.markdown("### Información")



    #HTML Info
    #Caso Sospechoso
    html_caso_sosp = """
	<div style="background-color: lightsteelblue; padding: 10px; box-shadow: 3px 2px 7px 1px rgba(158,160,183,0.37);">
<h1 style="color: black; text-align: left;">DEFINICI&Oacute;N DE CASO SOSPECHOSO COVID-19</h1>
<h2 style="color: white; text-shadow: #708090 1px 2px 2px; padding-left: 30px;">Criterio 1.</h2>
<p><strong>Toda persona que (de cualquier edad) que presente dos o m&aacute;s de los siguientes s&iacute;ntomas</strong></p>
<ul type="disc">
<li>Fiebre (37.5&deg;C o m&aacute;s)</li>
<li>Tos</li>
<li>Odinofagia</li>
<li>Dificultad respiratoria</li>
<li>Perdida repentina del gusto o del olfato</li>
<li>Cefalea</li>
<li>Diarrea y/o v&oacute;mitos</li>
</ul>
<p>Este criterio incluye toda enfermedad respiratoria aguda severa.<br />sin otra etiolog&iacute;a que explique completamente la presentaci&oacute;n cl&iacute;nica</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2 style="color: white; text-shadow: #708090 1px 2px 2px; padding-left: 30px;">Criterio 2.</h2>
<p><strong>Toda persona que:</strong></p>
<ul>
<li><strong>Sea trabajador de salud</strong></li>
<li><strong>Resida o trabaje en instituciones cerradas o de internaci&oacute;n prolongada*</strong></li>
<li><strong>Sea Personal esencial**</strong></li>
<li><strong>Resida en barrios populares o pueblos originarios***</strong></li>
<li><strong>Sea contacto estrecho de caso confirmado de COVID-19, que dentro de los 14 d&iacute;as posteriores al contacto:</strong></li>
</ul>
<p>Presente&nbsp;<strong>1 o m&aacute;s</strong>&nbsp;de estos s&iacute;ntomas: fiebre (37.5&deg;C o m&aacute;s), tos, odinofagia, dificultad respiratoria, perdida repentina del gusto o del olfato.</p>
<p><em>*penitenciarias, residencias de adultos mayores, instituciones neuropsiqui&aacute;tricas, hogares de ni&ntilde;as y ni&ntilde;os<br />**se considera personal esencial:<br />Fuerzas de seguridad y Fuerzas Armadas<br />Personas que brinden asistencia a personas mayores</em><br /><em>*** Se considera barrio popular a aquellos donde la mitad de la poblaci&oacute;n no cuenta con t&iacute;tulo de propiedad, ni acceso a dos o m&aacute;s servicios b&aacute;sicos. Fuente: Registro Nacional de Barrios Populares</em></p>
</div>
    """
#Definición de caso confirmado
    html_caso_conf = """
    <div style="background-color: lightsteelblue; padding: 10px; box-shadow: 3px 2px 7px 1px rgba(158,160,183,0.37);">
<h1>Definici&oacute;n de caso confirmado:</h1>
<h2><span style="color: #ffffff; ; text-shadow: #708090 1px 2px 2px; padding-left: 30px;"><strong>Caso confirmado por laboratorio:</strong></span></h2>
<ul>
<li>Todo caso sospechoso con resultado detectable para la detecci&oacute;n de genoma viral de SARS CoV-2 por t&eacute;cnicas directas.</li>
</ul>
<h2  style="color: #ffffff; ; text-shadow: #708090 1px 2px 2px; padding-left: 30px;"><strong>Caso confirmado por criterio cl&iacute;nico-epidemiol&oacute;gico:</strong></h2>
<ul>
<li>Se considerar&aacute; Caso confirmado por criterio cl&iacute;nico epidemiol&oacute;gico a todo contacto estrecho conviviente(1) con un caso de COVID-19 confirmado por laboratorio, que cumpla con la definici&oacute;n de caso sospechoso vigente, en &aacute;reas con transmisi&oacute;n comunitaria. Estos casos son considerados confirmados a los efectos de las medidas de prevenci&oacute;n y control, y no requerir&aacute;n estudios para el diagn&oacute;stico etiol&oacute;gico (salvo en los grupos exceptuados que se listan a continuaci&oacute;n).</li>
</ul>
<p>Los casos con criterio cl&iacute;nico epidemiol&oacute;gico que formen parte de los siguientes grupos, deber&aacute;n ser estudiados todos por laboratorio para el diagn&oacute;stico etiol&oacute;gico para SARS CoV-2 por t&eacute;cnicas moleculares:</p>
<ul>
<li>Pacientes que presenten criterios cl&iacute;nicos de internaci&oacute;n</li>
<li>Personas con factores de riesgo</li>
<li>Personas gestantes</li>
<li>Pacientes que residan o trabajen en instituciones cerradas &oacute; de internaci&oacute;n prolongada.</li>
<li>Trabajadores y trabajadoras de salud</li>
<li>Personal esencial</li>
<li>Personas fallecidas, sin causa conocida</li>
</ul>
<p><strong>Importante:</strong>&nbsp;Las medidas de control a implementar tanto ante todo caso confirmados por laboratorio o por criterio cl&iacute;nico-epidemiol&oacute;gico son:</p>
<ul>
<li>Aislamiento y control cl&iacute;nico del caso,</li>
<li>Identificaci&oacute;n y aislamiento de contactos estrechos(2).</li>
</ul>
<p><strong>El alta epidemiol&oacute;gica se otorgar&aacute; a los 10 d&iacute;as desde el comienzo de la fecha de inicio de los s&iacute;ntomas, siempre que se encuentre asintom&aacute;tico y tenga evoluci&oacute;n favorable, sin necesidad de internaci&oacute;n.</strong></p>
<p><em>(1). Conviviente: Toda persona que comparta habitaci&oacute;n, ba&ntilde;o o cocina con casos confirmados de COVID-19.</em><br /><em>(2). Aislamiento de contactos estrechos: Las personas convivientes identificadas como contactos estrechos se tratar&aacute;n como una cohorte. En este sentido, si alguien entre los contactos comienza con s&iacute;ntomas y se confirma por nexo, todo el resto de la cohorte que no son casos deber&aacute; reiniciar el per&iacute;odo de los 14 d&iacute;as de aislamiento.</em></p>
</div>

    """    
#Contacto estrecho
    html_contacto_est = """
    <div style="background-color: lightsteelblue; padding: 10px; box-shadow: 3px 2px 7px 1px rgba(158,160,183,0.37);">
<h1>Definici&oacute;n de contacto estrecho:</h1>
<h4>Para todos los casos, el periodo de contacto se considerar&aacute; desde las 48 horas previas al inicio de s&iacute;ntomas del caso de COVID-19</h4>
<h2><span style="color: #ffffff; ; text-shadow: #708090 1px 2px 2px; padding-left: 30px;"><strong>Caso confirmado por laboratorio:</strong></span></h2>
<p>Se considerar&aacute; como&nbsp;<strong>contacto estrecho a:</strong></p>
<ul>
<li>Toda persona que haya proporcionado cuidados a un caso confirmado mientras el caso presentaba s&iacute;ntomas o durante las 48 horas previas al inicio de s&iacute;ntomas y que no hayan utilizado las medidas de protecci&oacute;n personal adecuadas.</li>
<li>Cualquier persona que haya permanecido a una distancia menor a 2 metros con un caso confirmado mientras el caso presentaba s&iacute;ntomas, o durante las 48 horas previas al inicio de s&iacute;ntomas. durante al menos 15 minutos. (ej. convivientes, visitas, compa&ntilde;eros de trabajo).</li>
</ul>
<p><span style="text-decoration: underline;"><em><strong>Adicionalmente debe considerarse:</strong></em></span></p>
<p><strong>Contacto estrecho en barrios populares, pueblos originarios, instituciones cerradas o de internaci&oacute;n prolongada a:</strong></p>
<ul>
<li>Toda persona que comparta habitaci&oacute;n, ba&ntilde;o o cocina con casos confirmados de COVID-19.</li>
<li>Toda persona que concurra a centros comunitarios (comedor, club, parroquia, paradores para personas en situaci&oacute;n de calle, etc) y haya mantenido estrecha proximidad con un caso confirmado, mientras el caso presentaba s&iacute;ntomas (menos de 2 metros, durante 15 minutos).</li>
</ul>
<h2><span style="color: #ffffff; ; text-shadow: #708090 1px 2px 2px; padding-left: 30px;"><strong>Contacto estrecho en personal de salud:</strong></span></h2>
<p>Se considerar&aacute; personal de salud expuesto a SARS-CoV-2 a quienes sin emplear correctamente equipo de protecci&oacute;n personal apropiado:</p>
<ul>
<li>Permanezcan a una distancia menor de dos metros de un caso confirmado de COVID-19 durante por lo menos 15 minutos (por ejemplo, compartir un consultorio o una sala de espera).</li>
<li>Tengan contacto directo con secreciones (por ejemplo, tos, estornudo, etc.).</li>
<li>Tengan contacto directo con el entorno en el que permanece un paciente confirmado (como habitaci&oacute;n, ba&ntilde;o, ropa de cama, equipo m&eacute;dico, entre otros, incluye los procedimientos de limpieza de estos).</li>
<li>Permanezcan en el mismo ambiente durante la realizaci&oacute;n de procedimientos que generen aerosoles.</li>
</ul>
<p>No se considerar&aacute; personal de salud expuesto a SARS-CoV-2 a quienes hayan empleado correctamente el equipo de protecci&oacute;n personal apropiado en todo momento.</p>
</div>
    """


    options = ["...", "Criterio de caso sospechoso", "Definición de caso confirmado", "Definición de contacto estrecho"]
    choice = st.sidebar.selectbox("Más información", options)
    
    if choice == "Criterio de caso sospechoso":
        st.markdown(html_caso_sosp, unsafe_allow_html=True)
    if choice == "Definición de caso confirmado":
        st.markdown(html_caso_conf, unsafe_allow_html=True)
    if choice == "Definición de contacto estrecho":
        st.markdown(html_contacto_est, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
