import matplotlib.pyplot as plt
import pandas as pd
import os

# Ejercicio 9.8: Comparando especies en parques y en veredas

# Se crean rutas y se obtienen los datasets para el análissi
dir = 'ejercicios_python/Data'
arbolado1 = 'arbolado-en-espacios-verdes.csv'
arbolado2 = 'arbolado-publico-lineal-2017-2018.csv'

ruta_arbolado1 = os.path.join(dir, arbolado1)
ruta_arbolado2 = os.path.join(dir, arbolado2)

columnas_sel_parques = ['altura_tot', 'diametro', 'nombre_cie']     # Columnas imprescindibles
columnas_sel_veredas = ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']

df_parques = pd.read_csv(ruta_arbolado1)
df_veredas = pd.read_csv(ruta_arbolado2)

df_parques_sel = df_parques[columnas_sel_parques]   # Dataframes con la información necesaria
df_veredas_sel = df_veredas[columnas_sel_veredas]

# Convertir las columnas de nombres de especies a minúsculas para facilitar la búsqueda
df_parques_sel['nombre_cie'] = df_parques_sel['nombre_cie'].str.lower()
df_veredas_sel['nombre_cientifico'] = df_veredas_sel['nombre_cientifico'].str.lower()

# Filtrar filas correspondientes a las tipas en ambos DataFrames
df_tipas_parques = df_parques_sel[df_parques_sel['nombre_cie'] == 'tipuana tipu'].copy()
df_tipas_veredas = df_veredas_sel[df_veredas_sel['nombre_cientifico'] == 'tipuana tipu'].copy()

# Normalización y reasignación de nombres en las columnas
df_tipas_parques.rename(columns={'altura_tot': 'altura', 'diametro': 'diametro_altura_pecho'}, inplace=True)
df_tipas_veredas.rename(columns={'altura_arbol': 'altura', 'diametro_altura_pecho': 'diametro_altura_pecho'}, inplace=True)

# Creación de columna ambiente
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

# Unión de los dos datasets filtrados
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

# Se realizan los boxplot de diámetros y alturas
df_tipas.boxplot(column='diametro_altura_pecho', by='ambiente')
plt.title('Diámetro a la altura del pecho de las Tipas por ambiente')
plt.suptitle('')  # Elimina el título por default
plt.xlabel('Ambiente')
plt.ylabel('Diámetro a la altura del pecho [cm]')
plt.show()

df_tipas.boxplot(column='altura', by='ambiente')
plt.title('Altura de las Tipas por ambiente')
plt.suptitle('')
plt.xlabel('Ambiente')
plt.ylabel('Altura [m]')
plt.show()

'''
La guía pregunta qué hacer si queremos buscar otra especie y si es apropiado una función para ello.
La respuesta es que lo único que tendríamos que hacer es modificar la especie a filtrar, en el ejemplo está por defecto 'tipuana tipu'.
Y si, es altamente recomendable definir una función para ésto ya que sólo tendríamos que pasarle como parámetro la especie que elijamos.
Además, se puede seguir modularizando para un código más limpie, y también realizar una función para los ploteos de los gráficos, donde se
    pasan por parámetros las columnas/variables a evaluar y lo títulos personalizados para cada plot. (También podríamos pasarle DF y tipo de PLOT)
'''