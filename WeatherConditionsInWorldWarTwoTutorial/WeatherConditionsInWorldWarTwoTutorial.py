import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # visualization library
import matplotlib.pyplot as plt # visualization library
import plotly.plotly as py # visualization library
#from plotly.offline import init_notebook_mode, iplot # plotly offline mode
#init_notebook_mode(connected=True) 
import plotly.graph_objs as go # plotly graphical object

import os
mainDir = "../WeatherConditionsInWorldwarTwoTutorial"
print(os.listdir(mainDir))
import warnings            
warnings.filterwarnings("ignore") # if there is a warning after some codes, this will avoid us to see them.
plt.style.use('ggplot') 

aerial = pd.read_csv(mainDir+"/operations.csv")
weather_station_location = pd.read_csv(mainDir+"/Weather Station Locations.csv")
weather = pd.read_csv(mainDir+"/Summary_of_Weather.csv")

aerial = aerial[pd.isna(aerial.Country)==False] #DROP COUNTRIES COM VALORES NaN //NaN -> RETORNO DE NÚMERO REAL NÃO VÁLIDO
aerial = aerial[pd.isna(aerial['Target Longitude'])==False] #DROP Target Longitude COM VALORES NaN //NaN -> RETORNO DE NÚMERO REAL NÃO VÁLIDO
aerial = aerial[pd.isna(aerial['Takeoff Longitude'])==False] #DROP Takeoff Longitude COM VALORES NaN //NaN -> RETORNO DE NÚMERO REAL NÃO VÁLIDO

#DROP ATRIBUTOS NÃO UTILIZADOS
drop_list = ['Mission ID','Unit ID','Target ID','Altitude (Hundreds of Feet)','Airborne Aircraft',
             'Attacking Aircraft', 'Bombing Aircraft', 'Aircraft Returned',
             'Aircraft Failed', 'Aircraft Damaged', 'Aircraft Lost',
             'High Explosives', 'High Explosives Type','Mission Type',
             'High Explosives Weight (Pounds)', 'High Explosives Weight (Tons)',
             'Incendiary Devices', 'Incendiary Devices Type',
             'Incendiary Devices Weight (Pounds)',
             'Incendiary Devices Weight (Tons)', 'Fragmentation Devices',
             'Fragmentation Devices Type', 'Fragmentation Devices Weight (Pounds)',
             'Fragmentation Devices Weight (Tons)', 'Total Weight (Pounds)',
             'Total Weight (Tons)', 'Time Over Target', 'Bomb Damage Assessment','Source ID']

aerial.drop(drop_list, axis=1,inplace = True)
aerial = aerial[aerial.iloc[:,8]!="4248"] #DROP ESTA takeoff latitude 
aerial = aerial[aerial.iloc[:,9]!=1355]   #DROP ESTA takeoff longitude
aerial.info()

print('==========================================================')
weather_station_location = weather_station_location.loc[:,["WBAN","NAME","STATE/COUNTRY ID","Latitude","Longitude"] ]
weather_station_location.info()
print('==========================================================')

