import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""
markdown2 = "Todos los ejemplos que se mostraran en esta pagina fueron desarrollados por la Central de Geointeligencia S.A de C.V. en el año 2024. El objetivo es mostrar un poco de lo mucho que podemos realizar mediante análisis Geoespaciales. .  A continuación, selecciona alguno de los proyectos que hemos realizado y los resultados se mostraran de manera automática."

options = list(['Censo forestal urbano de Cd. Cuauhtémoc, Chihuahua','Censo forestal urbano de Monterrey, NL (2024)','Detección, ubicación y conteo de arboles en el Municipio de Carichi, Chihuahua','Análisis ambientales en el sector privado mediante imágenes de Dron','Delimitación de las construcciones de Monterrey, NL mediante segmentación de imágenes satelitales','Detección de las construcciones en Ciudad Cuauhtémoc, Chihuahua','Análisis de incendios ocurridos en Marzo del 2025 en Monterrey, NL','Herramienta creada mediante IA para el conteo de cítricos en el árbol '])
index = options.index('Censo forestal urbano de Cd. Cuauhtémoc, Chihuahua')

grafica_zorro = pd.DataFrame({"Puntos de presencia":['México: 5817','Nuevo León: 118'], "value": [5817,118]})
grafica_tortuga = pd.DataFrame({"Puntos de presencia":['México: 1063','Nuevo León: 343'], "value": [1063,343]})
grafica_aguila = pd.DataFrame({"Puntos de presencia":['México: 2333','Nuevo León: 241'], "value": [2333,241]})
grafica_venado = pd.DataFrame({"Puntos de presencia":['México: 8864','Nuevo León: 333'], "value": [8864,333]})
grafica_puma = pd.DataFrame({"Puntos de presencia":['México: 1450','Nuevo León: 60'], "value": [1450,60]})
grafica_coyote = pd.DataFrame({"Puntos de presencia":['México: 4503','Nuevo León: 179'], "value": [4503,179]})
grafica_jabali = pd.DataFrame({"Puntos de presencia":['México: 117','Nuevo León: 11'], "value": [117,11]})
grafica_oso = pd.DataFrame({"Puntos de presencia":['México: 861','Nuevo León: 273'], "value": [861,273]})
grafica_lince = pd.DataFrame({"Puntos de presencia":['México: 2131','Nuevo León: 58'], "value": [2131,58]})

c = alt.Chart(grafica_zorro).mark_arc().encode(theta="value",color="Puntos de presencia")
c2 = alt.Chart(grafica_tortuga).mark_arc().encode(theta="value",color="Puntos de presencia")
c3 = alt.Chart(grafica_aguila).mark_arc().encode(theta="value",color="Puntos de presencia")
c4 = alt.Chart(grafica_venado).mark_arc().encode(theta="value",color="Puntos de presencia")
c5 = alt.Chart(grafica_puma).mark_arc().encode(theta="value",color="Puntos de presencia")
c6 = alt.Chart(grafica_coyote).mark_arc().encode(theta="value",color="Puntos de presencia")
c7 = alt.Chart(grafica_jabali).mark_arc().encode(theta="value",color="Puntos de presencia")
c8 = alt.Chart(grafica_oso).mark_arc().encode(theta="value",color="Puntos de presencia")
c9 = alt.Chart(grafica_lince).mark_arc().encode(theta="value",color="Puntos de presencia")
#st.sidebar.title("About")
#https://discuss.streamlit.io/t/streamlit-hyperlink/29831

url = 'https://brayancarichi.github.io/CentralGeointeligenciav4/Contacto/index.html'
#st.write("Si estas interesado en lo que realizamos, ¡Contactanos! [Aquí](%s)" % url)
st.sidebar.image("Imagenes/CenGeo.jpeg")
st.sidebar.write("Si estas interesado en lo que realizamos, ¡Contactanos! [Aquí](%s)" % url)
st.sidebar.info(markdown2)
markdown3 = ""
#st.sidebar.altair_chart(c,use_container_width=True)






#st.se

i = 1


with st.expander("See source code"):
        selec = st.sidebar.selectbox("Proyecto a visualizar",options,index)
        print(selec + "lo seleccionado fue")
        cities = 'Matorral/Zorra.csv'
        cities2 = 'Matorral/Tortuga.csv'
        cities3 = 'Matorral/Aguila.csv'
        cities4 = 'Matorral/Venado.csv'
        cities5 = 'Matorral/Puma.csv'
        cities6 = 'Matorral/Coyote.csv'
        cities7 = 'Matorral/Jabali.csv'
        cities8 = 'Matorral/Oso.csv'
        cities9 = 'Matorral/Lince.csv'
        opcion = selec 
        if opcion == 'Censo forestal urbano de Cd. Cuauhtémoc, Chihuahua':
            seleccionado = cities
            logo = 'Imagenes/Cuauhtemoc.jpg'
            grafico = c
            markdown3 = "Proyecto realizado en ciudad Cuauhtémoc, chihuahua mediante una imagen área adquirida por el gobierno del Estado en diciembre del 2020. La zona fue dividida en 20 partes y mediante una Red Neuronal Convolucional, se detectaron y digitalizaron los arboles no caducifolios."
            url2 = ''
            imagenPromocional = 'Imagenes/Layout1.png'
            textoPromocional = 'Imagen de los resultados obtenidos. La figura (a) son los puntos en donde se detectó y ubicó un árbol no caducifolio. La figura (b) son las zonas de la ciudad que tienen una mayor densidad de arboles detectados. Este análisis es bastante útil en el sentido de conocer las zonas en donde hay una mayor cantidad de zonas verdes, algo que es muy importante en temas relacionados con islas de calor.'
            tituloPromocional = 'Censo forestal urbano de Cd. Cuauhtémoc, Chihuahua'
            imagen2 = 'Imagenes/Imagen 3.png'
            textoPromocional2 = 'La Red Neuronal Convolucional para hacer las detecciones utiliza el formato Oriented Bounding Boxes. Esto permite ubicar espacialmente los cuadros delimitadores mediante las coordenadas de cada vértice y la proyección de la imagen satelital utilizada.'
            print(seleccionado)
            
        elif opcion == 'Censo forestal urbano de Monterrey, NL (2024)':
            seleccionado = cities2
            logo = 'Imagenes/Monterrey.jpg'
            grafico = c2
            tituloPromocional = 'Censo forestal urbano de Monterrey, NL (2024)'
            url2 = 'https://censo-forestal-urbano-nl-central-geointeligencia.streamlit.app/'
            imagenPromocional = 'Imagenes/MonterreyAR.png'
            markdown3 = "Para la realización de este proyecto se obtuvieron 450 imágenes satelitales con una resolución de 15 centímetros y en escala 1:6157. Estas imágenes fueron capturadas en diciembre del 2024 y todas juntas tienen un peso de alrededor de 350 GB. Los arboles detectados incluyen sus coordenadas exactas en base al sistema de coordenadas WGS84 Zona 14 Norte. Esto nos convierte en los primeros en hacer un censo forestal urbano mediante esta tecnología."
            textoPromocional = 'Se detectaron 6 millones de arboles y se analizaron alrededor de 32 mil hectáreas. Este análisis es muy importante para temas de reforestación pero además, cuando haya incendios, se pueden contabilizar de manera exacta los arboles que fueron afectados por los incendios.'
            imagen2 = 'Imagenes/MonterreyAR2.png'
            textoPromocional2 = 'Cada árbol detectado cuenta con sus coordenadas especificas en el sistema de coordenadas WGS84 Zona 14 Norte. Adicionalmente, se obtuvieron las alturas de cada árbol mediante datos LIDAR.'
            print(seleccionado)
            
        elif opcion == 'Detección, ubicación y conteo de arboles en el Municipio de Carichi, Chihuahua':
            seleccionado = cities3
            logo = 'Imagenes/Carichi.jpg'
            tituloPromocional = 'Censo Forestal de Carichi, Chihuahua'
            url2 = ''
            markdown3 = 'Para la detección, ubicación y conteo de arboles del municipio de Carichi, Chihuahua se utilizaron imágenes satelitales de alta resolución provenientes de Google. Se analizaron 331 imágenes satelitales. Al igual que en los demás censos realizados, se entrenó una red neuronal profunda para la detección de arboles en la zona y con las imágenes especificas de Google.'
            imagenPromocional = 'Imagenes/ArbolesCarichi.png'
            imagen2 = 'Imagenes/ArbolesCarichi2.png'
            textoPromocional = 'Se detectaron alrededor de 3 millones de arboles y se analizaron casi 500 Gb de información satelital. Somos propietarios de una red neuronal especialmente entrenada para la detección de árboles en imágenes satelitales de alta resolución de Google.'
            textoPromocional2 = 'Por cada árbol detectado se obtuvo la coordenada en formato WGS84 Zona 13 Norte. Y adicionalmente, se obtuvieron las alturas de cada árbol haciendo uso de imágenes de radar, Machine Learning y datos LIDAR.   '
            grafico = c3
            
        elif opcion == 'Análisis ambientales en el sector privado mediante imágenes de Dron':
            seleccionado = cities4
            logo = 'Imagenes/DJI.png'
            url2 = ''
            tituloPromocional = 'Análisis ambientales en el sector privado mediante imágenes de Dron'
            markdown3 = 'No nos enfocamos solamente en el sector público si no también en el privado. Cualquier persona puede contar nuestros servicios. Un ejemplo claro es que recientemente hicimos un análisis de conteo de arboles en un rancho privado ubicado en Nuevo León.'
            imagenPromocional = 'Imagenes/pretexto.png'
            imagen2 = 'Imagenes/pretexto2.png'
            textoPromocional = 'En este caso práctico, un orto mosaico generado con Dron se tuvo que dividir en 430 partes para hacer las detecciones mucho más eficientes. Una vez que se hicieron las detecciones estas tuvieron que ser ubicadas especialmente para que coincidieran con el orto mosaico.'
            textoPromocional2 = 'Para la ubicación espacial de los cuadros delimitadores hicimos uso de las coordenadas extremas de cada uno de los vértices de las detecciones. Además, el modelo detecta de manera correcta cada árbol individual sin tener presencia de falsos positivos.   '
            grafico = c4
        elif opcion == 'Delimitación de las construcciones de Monterrey, NL mediante segmentación de imágenes satelitales':
            seleccionado = cities5
            logo = 'Imagenes/samgeo.png'
            tituloPromocional = 'Delimitación de las construcciones de Monterrey, NL mediante segmentación de imágenes satelitales'
            url2 = ''
            markdown3 = 'La segmentación de objetos en imágenes a diferencia de la detección de objetos dibuja el contorno exacto de todo lo que se detecta. En este caso, se delimitaron las construcciones de Monterrey, NL. Algo muy útil para conocer la dinámica de las ciudades, pero además, puede apoyar a los tomadores de decisiones de catastro.'
            imagenPromocional = 'Imagenes/ConstruccionesMon.png'
            imagen2 = 'Imagenes/ConstruccionesMon2.png'
            textoPromocional = 'En este caso se detectaron cada una de las construcciones que hay en Monterrey Nuevo León. Se contabilizaron 791 mil construcciones. Y al ser detectado en imágenes satelitales con proyección, fue posible ubicar espacialmente cada una de las segmentaciones.'
            textoPromocional2 = 'A diferencia de las detecciones, las segmentaciones detectan exactamente la forma de los objetos. Esto es especialmente útil para tomar decisiones basadas en datos exactos.'
            grafico = c5
        elif opcion == 'Detección de las construcciones en Ciudad Cuauhtémoc, Chihuahua':
            seleccionado = cities6
            logo = 'Imagenes/Edificio.jpg'
            tituloPromocional = 'Detección de las construcciones en Ciudad Cuauhtémoc, Chihuahua'
            url2 = ''
            markdown3 = 'Al igual que como se realizó con las construcciones de Monterrey, se analizaron imágenes satelitales de alta resolución y segmentación de objetos para obtener las construcciones de Ciudad Cuauhtémoc, Chihuahua.'
            imagenPromocional = 'Imagenes/ConstruccionesCua.png'
            imagen2 = 'Imagenes/ConstruccionesCua2.png'
            textoPromocional = 'Para Ciudad Cuauhtémoc, Chihuahua se detectaron y delimitaron 40 mil construcciones, incluyendo el corredor comercial. Cada una de las detecciones se encuentra ubicada espacialmente por lo que pueden realizar análisis espaciales exactos.'
            textoPromocional2 = ''
            grafico = c6
        elif opcion == 'Análisis de incendios ocurridos en Marzo del 2025 en Monterrey, NL':
            seleccionado = cities7
            logo = 'Imagenes/incendios.jpg'
            tituloPromocional = 'Análisis de incendios ocurridos en marzo del 2025 en Monterrey, NL'
            url2 = 'https://brayancarichi.github.io/AnalisisIncendiosMonterrey2025CenGeo/'
            markdown3 = 'El análisis de los incendios se hizo sin fines de lucro. La intención fue solamente colaborar para comprender porque estaban sucediendo esa cantidad de incendios en Monterrey, NL.'
            imagenPromocional = 'Imagenes/Densidad.png'
            imagen2 = 'Imagenes/Analisis de cambio.png'
            textoPromocional = 'Se realizó un análisis de densidad de los incendios para saber cuales fueron las zonas en donde las personas tuvieron un mayor riesgo en ser afectadas por el fuego. '
            textoPromocional2 ='Adicionalmente, se realizó un análisis de cambios en la cobertura de usos del suelo para saber si esto es un factor determinante en la propagación de incendios.  '
            grafico = c7

        elif opcion == 'Herramienta creada mediante IA para el conteo de cítricos en el árbol ':
             seleccionado = cities7
             logo = 'Imagenes/naranjas.jpg'
             tituloPromocional = 'Herramienta creada mediante IA para el conteo de cítricos en el árbol'
             url2 = 'https://conteonaranjasnl-bsfls82ymrnqrpvry5tkfv.streamlit.app/'
             markdown3 = 'Aplicación desarrollada mediante Inteligencia Artificial y cuyo fin es el conteo de cítricos que aun se encuentran en el árbol a partir de una fotografía.'
             imagenPromocional = 'Imagenes/naranjas2.png'
             imagen2 = 'Imagenes/naranjas3.png'
             textoPromocional = 'La aplicación web permite subir una imagen directamente desde nuestro dispositivo. Se pueden subir imágenes en formato PNG o JPG. '
             textoPromocional2 = 'Como resultados se obtiene una nueva imagen a la que le fue modificado el color para visualizar de mejor manera los resultados. En la parte inferior nos indica los cítricos que fueron detectados. También, podemos detectar los cítricos verdes y los maduros.  '
             rafico = c7
    
        
        st.sidebar.image(logo)
        st.sidebar.info(markdown3)

        
        
        
        
        
        regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'
        regions2 = 'Nl.geojson'
        raster = 'Chile.tif'

        
        #m.add_raster(raster,colormap="terrain",layer_name='DEM')
        
       
        
   
#m.to_streamlit(height=800)
st.title(tituloPromocional)
st.write("Pagina oficial del análisis [Aquí](%s)" % url2)
st.image(imagenPromocional)
st.write(textoPromocional)
st.image(imagen2)
st.write(textoPromocional2)


#streamlit run .\Pages\split_map.py --server.port 8888