{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Análisis sobre la tasa de suicidios mundial entre 1985 y 2016\n",
    "\n",
    "https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016\n",
    "\n",
    "\n",
    "Hemos realizado el siguiente análisis basandonos en los datos obtenidos en:\n",
    "https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016\n",
    "\n",
    "Los datos incluidos en la base de datos, son:\n",
    "\n",
    "- country, \n",
    "- year, \n",
    "- sex, \n",
    "- age group, \n",
    "- count of suicides, \n",
    "- population, \n",
    "- suicide rate, \n",
    "- country-year composite key, \n",
    "- HDI for year, \n",
    "- gdp_for_year, \n",
    "- gdp_per_capita, \n",
    "- generation (based on age grouping average)\n",
    "\n",
    "Importamos la Dataset, y las librerias que utilizaremos:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import numpy as np\n",
    "\n",
    "data = pd.read_csv(\"suicide-rates-overview-1985-to-2016.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Es una base bastante limpia, pero aún asi procedemos a la limpieza de la Dataset: empezamos buscando los duplicados:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_no_dupl = data.drop_duplicates()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Seguimos con los registros nulos; la columna \"HDI for year\" tiene mas de 19000 registros nulos: asi que la eliminamos:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "country                   0\n",
       "year                      0\n",
       "sex                       0\n",
       "age                       0\n",
       "suicides_no               0\n",
       "population                0\n",
       "suicides/100k pop         0\n",
       "country-year              0\n",
       "HDI for year          19456\n",
       " gdp_for_year ($)         0\n",
       "gdp_per_capita ($)        0\n",
       "generation                0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "null_cols=data_no_dupl.isnull().sum()\n",
    "null_cols"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_no_dupl1=data_no_dupl.drop(['HDI for year'], axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Eliminamos la columna 'country-year' porque tenemos ya otras 2 columnas que nos facilitan esos datos:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_clean=data_no_dupl1.drop(['country-year'], axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Viendo los datos, me parece relevante calcular el porcentaje de suicidios en función del sexo:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "sex\n",
       "female    23.109261\n",
       "male      76.890739\n",
       "Name: suicides_no, dtype: float64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "suicides_per_sex= data_clean.groupby(['sex'])['suicides_no'].sum()/(1559510+5188910)*100\n",
    "suicides_per_sex"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lo representamos en un grafico, donde claramente se ve la diferencia:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels = 'Male', 'Female'\n",
    "sizes = [76.90, 23.10]\n",
    "explode = (0.1, 0)\n",
    "\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',\n",
    "        shadow=True, startangle=90, colors={'tab:blue', 'tab:pink'})\n",
    "ax1.axis('equal')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Tambien parece relevante ver la evolucion en el tiempo del nº suicidios por año (nº suicidios total de todos los paises estudiados):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7fc00be4d390>]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "suicides_per_year= data_clean.groupby(['year'])['suicides_no'].sum()\n",
    "suicides_per_year\n",
    "plt.plot(suicides_per_year)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Los datos de 2016 son especialmente bajos, por lo que podemos pensar que no son del año completo; aun asi, podemos ver que, afortunadamente, la tendencia del nº de suicidios a nivel mundial es a la baja, desde 2003 aproximadamente."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Para completar nuestro análisis, nos parece básico conocer que paises tienen la tasa de suicidio mas alta del mundo:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "country\n",
       "Lithuania             41.182219\n",
       "Russian Federation    32.777207\n",
       "Sri Lanka             30.483939\n",
       "Belarus               30.344685\n",
       "Hungary               29.717558\n",
       "Name: suicides_no/100k pop, dtype: float64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#seleccionamos las columnas que nos interesan, y calculamos los totales por pais:\n",
    "data_selected= data_clean[['country', 'suicides_no','population']]\n",
    "data_selected_grouped= data_selected.groupby(['country']).sum()\n",
    "#tanto el total de poblacion, como del numero de suicidios, suma los 31 años que ocupa el estudio; para poder interpretar los datos, calculamos la media, y sobre esos datos, calculamos la tasa de suicidio:\n",
    "data_selected_grouped['population(mean)'] = data_selected_grouped['population']/31\n",
    "data_selected_grouped['suicides_no(mean)'] = data_selected_grouped['suicides_no']/31\n",
    "#incluyo una columna con la tasa media de suicidio de cada pais(/100k), de los años de 1985 a 2016:\n",
    "data_selected_grouped['suicides_no/100k pop']= data_selected_grouped['suicides_no(mean)']/data_selected_grouped['population(mean)']*100000\n",
    "#ordenamos los resultados en orden descendente:\n",
    "suicides_per_country_ord=data_selected_grouped.sort_values(by=['suicides_no/100k pop'], ascending=False)\n",
    "suicides_per_country_ord['suicides_no/100k pop'].head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Insertamos un gráfico con dichos paises y la tasa de suicidio media del periodo 1985 a 2016:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "height = [41.18,32.77,30.48,30.34,29.71 ]\n",
    "bars = ('Lithuania', 'Russian Federation','Sri Lanka','Belarus','Hungary')\n",
    "y_pos = np.arange(len(bars))\n",
    "plt.bar(y_pos, height)\n",
    "plt.xticks(y_pos, bars)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
