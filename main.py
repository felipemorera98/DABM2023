import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()
archivo = cwd + "/ecg_data.csv"
data = pd.read_csv(archivo)
time = data['time']
signal = data['signal']



#deteccion de datos
cont = 0
rango = []
maxY = []
maxX = []

for punto in ecg_data.signal:
    if (punto <= ecg_data.promedio_dinamico[cont]) and (len(rango)<1) :
        cont += 1
    elif punto > ecg_data.promedio_dinamico[cont]:
        rango.append(punto)
        cont += 1
    else:
        maximo = max(rango)
        maxY.append(maximo)
        maxxs = cont-len(rango)+rango.index(maximo)
        maxX.append(maxxs)
cont=0
dist=[]

while cont < len(maxxs) -1:
    distancia = maxX[cont+1]-maxX[cont]
    distancia = distancia/100
    dist.append(distancia)
    cont+=1

bpm = 60/np.mean(dist)

print("BPM: ",round(bpm,1))