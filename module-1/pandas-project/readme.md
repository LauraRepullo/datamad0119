

# PANDAS PROYECT

   ## Proyecto SHARKATTACK
   

        Una vez importada la Data Set relativa a los ataques de tiburones registrados en todo el mundo, he llevado a cabo algunas operaciones para depurar y organizar los datos, para un mejor tratamiento y una correcta interpretacion de los mismos.

       He localizado las columnas que más valores nulos tenian, y he eliminado aquellas que tenian mas de 5.000 (el dataset cuenta con 5.992 filas en total)

    Despues de analizar las columnas que quedan, elimino las que incluyen datos que no me resultan relevantes para mi análisis ('pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2', 'Name').

    Muestro los datos de la columna ";creo que lo mas consistente es que seleccione los datos recabados a partir de 1600; elimino las filas con stos anteriores a esa fecha.

    En la columna Fatal(Y/N), donde como mucho deberia haber 3 tipos de dato (Y/N/Unknown) observo que hay mas; renombramos para homogeneizar la columna.

    Incluyo la columna N_Attacks, donde se recoge el numero de ataques registrados.

    Para tener una mejor visión, ordeno los datos en funcion de Year, Country y Area.

    Me parece interesante localizar los paises donde mas ataques de tiburones se han dado; creo una tabla donde se recogen el numero de ataques por pais. Los tres paises donde mas accidentes de este tipo han sucedido son USA (2.099 casos), Australia (1262) y Soth Africa (557).

    Posteriormente incluyo el año en ese analisis; los años en los que mas ataques de tiburones ha habido registrados, han sido en 2015 (72 ataques), 2007 (66) y 2014 (65).

    Tambien es relevante saber el resultado provocado por dichos ataques; en el 72.65% de los ataques las victimas sobrevivieron; en un 25.46% fallecieron, y no tenemos datos sobre el 1.89%.


    