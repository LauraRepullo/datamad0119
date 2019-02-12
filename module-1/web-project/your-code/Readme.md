 
 
   # WEB-PROYECT
   
                   Laura Repullo



   #### El objetivo del proyecto es obtener información a través de Web Scraping y consultas a una API, y agregar la información.


        Para ello, he seguido los siguientes pasos:
        
        1) Importamos las librerias que vamos a emplear en los distintos procesos: requests, Beautifulsoup, pandas, etc...
        
        2) En mi caso empezaré el ejercicio haciendo Web Scraping en distintas URL de la web < https:\\www.rollingstone.com > localizamos distitas listas de canciones y sus autores, y hacemos las peticiones a traves de requests.
        
        3) Con BeautifulSoup haremos que la informacion se nos muestre más estructurada. En el HTML, buscamos los nombres de las canciones y de sus autores, y creamos una lista
        
        4)Limpiamos las listas (split, strit, remove).
        
        5)Separamos los elementos de las listas en 2: una con los autores, y otra con el título de las canciones.

        6)Creamos la DataFrame de cada consulta con los resultados, y posteriormente las unimos todas (append). Reseteamos los indices para que nos muestre los correspondientes a la nueva DataFrame.
        
        7)Exportamos los resultados de la DataFrame total a un .csv ('dataframe_from_API.csv').
        
        8)Una vez que tenemos los datos de la Web, procedemos a localizar los que nos interesan de la API. Las peticiones a la API requieren que informemos del autor y del título de la canción; para ello, creamos dos listas.
        
        9)Creamos una función que recibe autor y título, y nos devuelve la letra de la canción. Generamos una lista con las 400 primeras, ya que si intentamos pedir las de las 1000 canciones que hemos obtenido de Web Scraping, nos salta un error.
        
        10)Para poder incluir las letras en una columna de la DataFrame que tenemos con la informacion obtenida a traves del Web Scaping, seleccionamos las primeras 400 filas de la DataFrame. Creamos una nueva columna en el dataframe, llamada "Lyrics", y le asignamos las letras de las canciones obtenidas de la API.
        
        11)Podemos ver como hemos conseguido la mayoria de las letras de nuestra lista. 
        
        12)Finalizamos guardando el DataFrame en un .csv con el nombre 'Lyrics_songs400.csv'.