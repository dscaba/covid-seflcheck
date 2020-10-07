import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly as pt
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time
# Config

st.beta_set_page_config(page_title="COVID-19 SelfCheck",
                        page_icon="https://www.aso-apia.org/sites/default/files/field/image/coronavirus-4947717_1280_2.png", layout='wide', initial_sidebar_state='auto')
# ----------------------

geo = """
    <div class="container-fluid mb-1">
    <h2 style='font-family: Helvetica, Verdana, sans serif;font-size: 26px; border: 1px outset;border-radius: 10px 10px 10px 10px; text-align: center; color: white; background-color: black;'> Mapa de casos COVID-19 por provincia 🗺 </h2></div>
    
    """


def main():

    st.sidebar.title("Menú Principal")
    choice = st.sidebar.radio(
        "", ("🏡 Home", "🔎 Realizar Autodiagnostico", "🏥 Centros de emergencia", "☎ Teléfonos útiles", "📊 Gráfico de casos", "🗺 Mapa de casos"))
    if choice == "🏡 Home":
        st.write(home())
    if choice == "🔎 Realizar Autodiagnostico":
        st.write(diagnostico())
        if st.sidebar.checkbox("Criterio de caso sospechoso"):
            criterio()
    if choice == "🏥 Centros de emergencia":
        st.write(hospitales())
    if choice == "📊 Gráfico de casos":
        st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
    if choice == "🗺 Mapa de casos":
        st.markdown(geo, unsafe_allow_html=True)
        mapa_casos()
    if choice == "☎ Teléfonos útiles":
        st.write(telefonos())


def mapa_casos():
    mapa = pd.read_html(
        "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Argentina_medical_cases_by_province", header=0)[0]

    MAPBOX_ACCESS_TOKEN = (
        "pk.eyJ1IjoiZGVtNTAwIiwiYSI6ImNrZnk1ZWU1ejA4dXMyeW50cTF3cGlsMmMifQ.XZoeyQKxIZK__0QQ0g2pmA")

    pcias = pd.read_csv(
        "https://infra.datos.gob.ar/catalog/modernizacion/dataset/7/distribution/7.7/download/provincias.csv")

    mapa = mapa.drop(mapa.index[[25, 26]])

    mapa = mapa.drop('Region', axis=1)
    mapa = mapa.drop(
        columns=['Recov.[a][b]', 'Cases/100k[a][c]', 'Ref.'])
    mapa = mapa.rename(columns={'Region.1': 'provincia',
                                'Cases[a][b]': 'Casos', 'Deaths[a]': 'Fallecidos'})
    mapa.iat[2, 0] = "Buenos Aires"
    mapa.iat[1, 0] = "Ciudad Autónoma de Buenos Aires"
    mapa.iat[23, 0] = "Tierra del Fuego"
    mapa = mapa.drop([0, 0])
    mapa = mapa.reset_index()

    pcias = pcias.drop(columns=['categoria', 'fuente', 'id', 'iso_id',
                                'nombre', 'nombre_completo'])
    pcias = pcias.rename(columns={'centroide_lat': 'lat', 'centroide_lon': 'lon',
                                  'iso_nombre': 'provincia'})
    pcias = pcias.sort_values(['provincia'], axis=0, ascending=True,
                              na_position='last', ignore_index=False, key=None)
    mapa_n = pd.merge(mapa, pcias)
    mapa_n['Casos'] = mapa_n.Casos.astype(int)

    fig = px.scatter_mapbox(mapa_n, lat="lat", lon="lon", hover_name="provincia", hover_data=["Casos", "Fallecidos"], size="Casos", color="Casos",
                            color_continuous_scale=px.colors.sequential.OrRd, zoom=3.8, height=800, width=800)

    fig.update_layout(mapbox_style="dark",
                      mapbox_accesstoken=MAPBOX_ACCESS_TOKEN)
    fig.update_layout(
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "type": 'circle',
                "circle": {
                    'radius': 1200}

            }
        ])

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    st.plotly_chart(fig, use_container_width=True)


url = 'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
df = pd.read_csv(url)
df.rename(columns={"osm_admin_level_4": "provincia"}, inplace=True)
df.drop(['dia_cuarentena_dnu260', 'osm_admin_level_2', 'osm_admin_level_8', 'nue_casosconf_diff', 'nue_fallecidos_diff', 'tot_recuperados',
         'tot_terapia', 'test_RT-PCR_negativos', 'test_RT-PCR_total',
         'transmision_tipo', 'informe_tipo', 'informe_link', 'observacion',
         'covid19argentina_admin_level_4'], axis=1, inplace=True)
booleans = []
for provincias in df.provincia:
    if provincias == "Indeterminado":
        booleans.append(True)
    else:
        booleans.append(False)
is_long = pd.Series(booleans)
casos_nacion = df[is_long]
df['fecha'] = pd.to_datetime(df['fecha'])
fig = px.scatter_3d(casos_nacion, x='fecha', y='tot_fallecidos', z='tot_casosconf', color='tot_casosconf', title="Evolución casos COVID-19", size_max=100000000,
                    width=1000, height=800, labels={"fecha": "Fecha",  "tot_casosconf": "Total de casos confirmados", "tot_fallecidos": "Total de fallecidos"})
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})


def home():
    st.markdown("<h1 container-fluid mt-5 style='font-size: 40px; font-family: San Francisco, BlinkMacSystemFont, sans-serif;;border: 1px outset;border-radius: 10px 10px 10px 10px;background-color: black; text-align: center; height 100px; width: 100%;color: white;'>Bienvenido al sistema de autodiagnóstico 🩺🦠</h1>",
                unsafe_allow_html=True)
    st.markdown("<h2 style='font-family: Helvetica, Verdana, sans serif;font-size: 20px; border: 2px outset;border-radius: 10px 10px 10px 10px; text-align: center; color: black;'>¿Qué es el Coronavirus?</h2>",
                unsafe_allow_html=True)
    video = """


        <iframe width="100%" height="800" src="https://www.youtube-nocookie.com/embed/PvJpC97EpuA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """
    st.markdown(video, unsafe_allow_html=True)


def diagnostico():
    st.info("**ℹ    Esta aplicación bajo ningún punto de vista reemplaza la consulta con un profesional. Ante cualquier duda, no deje de consultar con su médico.**")

    marcar = """<div class="container-fluid mb-3">
    <h2 style='font-family: Helvetica, Verdana, sans serif;font-size: 20px; border: 1px outset;border-radius: 10px 10px 10px 10px; text-align: center; color: white; background-color: black;'>Seleccione en caso que corresponda ✅</h2></div>
    """
    st.markdown(marcar, unsafe_allow_html=True)

    # Contacto estrecho
    if st.checkbox("Contacto estrecho con caso confirmado de COVID-19 (dentro de los 14 días posteriores al contacto)", value=False):
        chk_contacto = 1
    else:
        chk_contacto = 0

    # Area de riesgo
    if st.checkbox("Resida en Areas de riesgo determinadas por el gobierno(ej :AMBA, barrios populares o pueblos originarios)", value=False):
        chk_area = 1
    else:
        chk_area = 0

    # Personal de salud
    if st.checkbox("Personal de salud", value=False):
        chk_personal = 1
    else:
        chk_personal = 0
    sintomas = """<div class="container-fluid mb-3 justify-content-center">
    <h2 style='font-family: Helvetica, Verdana, sans serif;font-size: 20px; border: 1px outset;border-radius: 10px 10px 10px 10px; text-align: center; color: white; background-color: black;'>Seleccione sus síntomas 🌡</h2></div>
    """
    st.markdown("")
    st.markdown(sintomas, unsafe_allow_html=True)

    # Fiebre
    if st.checkbox("Fiebre (37.5° o más)", value=False):
        chk_fiebre = 1
    else:
        chk_fiebre = 0

    # Tos
    if st.checkbox("Tos", value=False):
        chk_tos = 1
    else:
        chk_tos = 0

    # Dolor de cabeza
    if st.checkbox("Dolor de cabeza", value=False):
        chk_dolor_cabeza = 1
    else:
        chk_dolor_cabeza = 0

    # Anosmia
    if st.checkbox("Pérdida del sentido del olfato o del gusto", value=False):
        chk_anosmia = 1
    else:
        chk_anosmia = 0

    # Odinofagia
    if st.checkbox("Odinofagia (Dolor de garganta)", value=False):
        chk_odinofagia = 1
    else:
        chk_odinofagia = 0

    # Dificultad Respiratoria
    if st.checkbox("Dificultad Respiratoria", value=False):
        chk_resp = 1
    else:
        chk_resp = 0

    # Diarrea
    if st.checkbox("Diarrea", value=False):
        chk_diarrea = 1
    else:
        chk_diarrea = 0

    # Vomitos
    if st.checkbox("Vomitos", value=False):
        chk_vomitos = 1
    else:
        chk_vomitos = 0

    #   Criterios

    if chk_anosmia + chk_area + chk_contacto + chk_dolor_cabeza + chk_fiebre + chk_odinofagia + chk_personal + chk_resp + chk_tos + chk_vomitos + chk_diarrea >= 2 and chk_anosmia + chk_area + chk_contacto + chk_dolor_cabeza + chk_fiebre + chk_odinofagia + chk_personal + chk_resp + chk_tos + chk_vomitos + chk_diarrea < 12:
        time.sleep(1)
        st.error(
            "☣ Usted presenta síntomas compatibles con la enfermedad COVID-19. Por favor consulte con su médico de inmediato.")

    if chk_anosmia + chk_area + chk_contacto + chk_dolor_cabeza + chk_fiebre + chk_odinofagia + chk_personal + chk_resp + chk_tos + chk_vomitos + chk_diarrea == 1:
        time.sleep(1)
        st.success(
            "😄 Usted no presenta síntomas compatibles compatibles con la enfermedad COVID-19.")


def telefonos():
    st.markdown("<h1 container-fluid mt-5 style='font-size: 40px; font-family: San Francisco, BlinkMacSystemFont, sans-serif;;border: 1px outset;border-radius: 10px 10px 10px 10px;background-color: black; text-align: center; height 100px; width: 100%;color: white;'>📞 Asistencia telefónica  </h1>",
                unsafe_allow_html=True)
    components.html("""
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <div class="alert alert-primary" role="alert">
    <div class="container-fluid">
        <h4 mt-5 mb-2>🏛 Ministerio de Salud</h4>
            <p>Llamá al <strong>120</strong>, es <strong>gratuito</strong> desde cualquier lugar del país y te atienden <strong>las 24 horas</strong>.</p>
            <p><a href="tel:120" title="" class="btn btn-success btn-sm">Si estás en tu celular, llamá ahora</a></p><hr><h4>📱 Whatsapp</h4><p>Envianos un mensaje vía WhatApp para que podamos ayudarte.</p><p>Escribí "Hola" (sin comillas) al número <strong>+54 9 11 2256-0566</strong> y comenzá a chatear.</p></div>
    </div>
    """, height=600)


def criterio():

    adver_html = """<div class="element-container" style="text-align: center; width: 100%;"><div class="alert alert-warning stAlert" style="width: 100%;"><div class="markdown-text-container"><h2>DEFINICIÓN DE CASO SOSPECHOSO COVID-19</h2><h3>Toda persona que (de cualquier edad) que presente dos o más de los síntomas mencionados anteriormente:</h3><p>
    <h2 class= "text-center"> 
    <img src="https://www.argentina.gob.ar/sites/default/files/30-fiebre-11-junio.png"; width= "200px"; height= "200px" />
    <img src="https://www.argentina.gob.ar/sites/default/files/31-tos-11-junio.png"; width= "200px"; height= "200px" />
    <img src="https://www.argentina.gob.ar/sites/default/files/32-dolor-garganta-11-junio.png"; width= "200px"; height= "200px" />
    <img src="https://www.argentina.gob.ar/sites/default/files/33-dificultad-respirar-11-junio.png"; width= "200px"; height= "200px" />
    <img src="https://www.argentina.gob.ar/sites/default/files/34-olfato-11-junio.png"; width= "200px"; height= "200px" /></h2></p></div></div></div>"""

    st.markdown(adver_html, unsafe_allow_html=True)


def hospitales():
    hosp = """
    <div class="container-fluid mb-1">
    <h2 style='font-family: Helvetica, Verdana, sans serif;font-size: 26px; border: 1px outset;border-radius: 10px 10px 10px 10px; text-align: center; color: white; background-color: black;'>🏥 Centros de emergencia </h2></div>
    
    """
    mapa_caba = """
    <iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d44189.88856275537!2d-58.47822444654176!3d-34.59320779300904!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1shospital!5e0!3m2!1ses!2sar!4v1598547200214!5m2!1ses!2sar" width="100%" height="600" frameborder="50" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
    """

    mapa_oeste = """
    <iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d74281.64006194951!2d-58.71598674810404!3d-34.63409708237743!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1shospitales!5e0!3m2!1ses!2sar!4v1599591842978!5m2!1ses!2sar" width="100%" height="600" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
    """
    mapa_norte_a = """
    <iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d105245.70622343953!2d-58.707113908843255!3d-34.479342620888524!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1shospital!5e0!3m2!1ses!2sar!4v1599592486411!5m2!1ses!2sar" width="100%" height="600" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
    """
    mapa_norte_b = """
    <iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d62640.36801897223!2d-58.88566582323964!3d-34.398071834072546!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1shospital!5e0!3m2!1ses!2sar!4v1599592659795!5m2!1ses!2sar" width="100%" height="600" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
    """
    mapa_sur = """
    <iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d104877.20025863609!2d-58.420106547634894!3d-34.77038925770628!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1shospital!5e0!3m2!1ses!2sar!4v1599592267416!5m2!1ses!2sar" width="100%" height="600" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
    """
    st.markdown(hosp, unsafe_allow_html=True)
    mapa_sel = st.selectbox(
        "", ["CABA", "Zona Oeste", "Zona Norte 1", "Zona Norte 2", "Zona Sur"])
    if mapa_sel == "CABA":
        st.markdown(mapa_caba, unsafe_allow_html=True)
    if mapa_sel == "Zona Oeste":
        st.markdown(mapa_oeste, unsafe_allow_html=True)
    if mapa_sel == "Zona Norte 1":
        st.markdown(mapa_norte_a, unsafe_allow_html=True)
    if mapa_sel == "Zona Norte 2":
        st.markdown(mapa_norte_b, unsafe_allow_html=True)
    if mapa_sel == "Zona Sur":
        st.markdown(mapa_sur, unsafe_allow_html=True)


if __name__ == '__main__':
    main()


icono = st.sidebar._html(
    """
    <html>
<head>
<style>
a{
    text-decoration: none;
}
i {
color: slategray;
}

i:hover {
  transform: scale(1.5);
  transition-duration: 500ms;
  opacity: 0.5;
}

h3 {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
h4{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 10px;
    color: gray;
}

h5{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 10px;
    color: slategray;
}

whatsapp {
  position:fixed;
  
  
 
  text-align:center;
  
  z-index:100;
  transform: scale(1.5);
  transition-duration: 500ms;
  opacity: 0.5;
  }

whatsapp-icon {
  margin-top:13px;
 
}

</style>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>


     <script src="https://kit.fontawesome.com/5e48316ef8.js" crossorigin="anonymous"></script>
    
   
    <footer class="container">
    <h3>Developed by Demián Scaba</h3>
    <h4>Contact me</h4>
    <a href="https://www.linkedin.com/in/dscaba" target="_blank">
    <i class="fab fa-linkedin fa-2x"></i>
    </a>
    <a href="mailto: d.scaba@gmail.com">
    <i class="fas fa-envelope fa-2x"></i></a>
	<a href="https://wa.me/541130106895?text=Hola, me comunico a traves de COVID-19 SelfCheck" class="whatsapp" target="_blank"> <i class="fa fa-whatsapp whatsapp-icon  fa-2x"></i></a>
    <a href="https://www.instagram.com/demi.500/" target="_blank">
    <i class="fab fa-instagram fa-2x"></i></a>
    <h5>© 2020 All Rights Reserved</h5>
    </footer>

</html>
    """
)
