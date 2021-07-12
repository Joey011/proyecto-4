import numpy as np
import matplotlib.pyplot as plt

#with auto cierra los archivos que abre
with open('CasosGeneroEtarioEtapaClinica.csv','r',encoding='utf-8') as archivo:
    lista_fechas = archivo.readline() #pasa una linea y la retorna
    lista_fechas = lista_fechas.strip().split(',')[3:-1]
    lista_rangos = [] #contendra la info de los casos por fecha y rango
    lista_rangos_h = []
    lista_rangos_m = []
    data_rangos  = [] #contendra orden de los rangos
    data = archivo.readlines()
    data1 = data[:34]
    data2 = data[34:]
    for linea in data1[:17]:
        linea = linea.strip()
        fila  = linea.split(',')
        data_rangos.append(fila[0])
        fila = fila[3:-1]
        for j in range(len(fila)): 
            fila[j] = int(float(fila[j]))
        lista_rangos.append(fila)
        lista_rangos_h.append(fila)
    for i in range(17):
        linea = data1[i+17]
        linea = linea.strip()
        fila  = linea.split(',')
        fila  = fila[3:-1]
        for j in range(len(fila)): 
            fila[j] = int(float(fila[j]))
            lista_rangos[i][j] += fila[j]
        lista_rangos_m.append(fila)
    confirmados = []
    probables   = []
    for i in range(len(data2)): 
        linea = data2[i]
        linea = linea.strip()
        fila  = linea.split(',')
        if fila[2]=='CONFIRMADA':
            confirmados.append(int(float(fila[-1])))
        elif fila[2]=='PROBABLE':
            probables.append(int(float(fila[-1])))