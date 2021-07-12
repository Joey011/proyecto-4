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
def menu_programa(encabezado,opciones,funciones):
    print(encabezado) #titulo del menu
    print()           #salto de linea
    #se forma un texto con las opciones que se imprimiran
    texto = ''
    for i in range(len(opciones)):
        texto += str(i+1)+'~ '+opciones[i]+'\n'
    texto += '0~ Salir\n'
    #interruptor encendido
    interruptor = True
    #mientras el interruptor este encendido
    while interruptor:
        #se imprime menu
        print(texto)
        opcion = input('Ingrese su opción: ')
        #la opcion es valida si es realmente un caracter numerico
        if opcion.isnumeric(): #metodo con respuesta booleana #True/False
            opcion = int(opcion)
            #si es una opcion valida
            if opcion in range(len(opciones)+1):
                if opcion == 0:
                    interruptor = False
                else:
                    #se ejecuta funcion alojada en la lista
                    #correspondiente a la opcion seleccionada
                    funciones[opcion-1]()
            else:
                print('Opción no válida')
        else:
            print('Opción no válida')
def uno():
    for i in range(len(data_rangos)):
        print(str(i+1)+'~',data_rangos[i])
    rango = input('Seleccione rango etario: ')
    if rango.isnumeric():
        rango = int(rango)
        if rango in range(1,len(lista_rangos)+1):
            #se escoje fila con el rango escogido
            #se consideran 7 ultimos datos
            fechas = lista_fechas[-7:]
            plt.plot(range(7),lista_rangos[rango][-7:])
            #etiquetas del eje x
            plt.xticks(range(7),labels=fechas,rotation=45)
            plt.grid(True) #cuadricula
            plt.ylabel('Casos')
            plt.title(data_rangos[rango])
            plt.show()
        else:
            print('Opción no válida')
    else:
        print('Opción no válida')      
def dos():
    totales = []
    for i in range(len(lista_rangos)):
        totales.append(lista_rangos[i][-1])
    plt.bar(range(len(data_rangos)),totales)
    plt.title('Rango etario con mayor tasa de contagios')
    plt.grid(True) #cuadricula
    plt.ylabel('Casos Totales')
    plt.xticks(range(len(data_rangos)),labels=data_rangos,rotation=90)
    plt.text(0, max(totales), 'maximo:'+data_rangos[totales.index(max(totales))], fontsize=14)
    plt.show()     
def tres():
    totates_h = [] 
    totales_m = []
    for i in range(len(lista_rangos_h)):
        totates_h.append(lista_rangos_h[i][-1])
    for i in range(len(lista_rangos_m)):
        totales_m.append(lista_rangos_m[i][-1])
    T = [sum(totates_h),sum(totales_m)]
    plt.bar(range(2),T)
    plt.grid(True)
    X = 'Hombres'
    if T[0] != max(T):
        X = 'Mujeres'
    plt.ylabel('Casos Totales')
    plt.text(0, max(T), 'mayor indice de contagios: '+X, fontsize=14)
    plt.xticks(range(2),['Hombres','Mujeres'])
    plt.show()
