
from math import sqrt
from unittest import result
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dCohen(dataraw):
    print("[dCohen]")
    dataA = dataraw[(dataraw.Categorica == 0)]
    dataB = dataraw[(dataraw.Categorica == 1)]
    result_d = abs(dataA.Cuantitativa.mean() - dataB.Cuantitativa.mean())/(dataraw.Cuantitativa.std())
    #print("The result for dCohen is {}".format(result_d))
    #dataShow = pd.concat([dataA.Cuantitativa,dataB.Cuantitativa],axis = 1)
    #ax = dataShow.boxplot()
    return result_d

def fCohen(dataraw):
    print("[fCohen]")
    #Necesitamos coger las muestras de los grupos correspondientes
    #1.Nombres de las columnas

    col_names = []
    cond = True
    print("Introduzca las columnas a analizar")

    while(cond):
        print("Introduzca la columna >>>")
        name = input()
        col_names.append(name)
        print("¿Desea introducir más columnas?[Y/N]")
        ans = input()
        if(ans == 'N') | (ans == 'n'):
            cond = False

    size = len(col_names)
    #2.Nuevo DatFrame con las columnas a evaluar(grupos)
    new_df = pd.DataFrame(dataraw,columns=col_names)
    mean_vec = []
    std_vec = []
    group_samples_vec = []
    #3.Obtenemos las medias,desviacion tipica y el numero de elementos de los grupos estudiados
    for i in range(size):
        mean_vec.append(new_df[col_names[i]].mean())
        std_vec.append(new_df[col_names[i]].std())
        group_samples_vec.append(new_df[col_names[i]].size)     
    mean_vec = np.array(mean_vec)
    grand_mean = mean_vec.mean()

    # SSbetween & SSerror(Sum of squares)
    sum_mean = 0
    sum_std = 0

    for j in range(size):
        sum_mean += group_samples_vec[j]*((mean_vec[i]- grand_mean)**2)
        sum_std += (group_samples_vec[j] - 1) * (std_vec[j])**2

    #Estadistico eta cuadrado
    Eta_squared = (sum_mean)/(sum_mean + sum_std)

    result_f = sqrt(Eta_squared/(1 - Eta_squared))
    return result_f

def menu():
    print("1.Analisis entre Cuantitativa y Categórica")
    print("2.Exit")

print("Bienvenido a Stat ¿Qué opcion desea?")

while(1):
    menu()
    ans = int(input())
    if(ans == 1):
        filepath = "~/pyProjects/Smarta.csv"
        dataraw = pd.read_csv(filepath)

        result_d = dCohen(dataraw)
        result_f = fCohen(dataraw)

        print("=================")
        print("dCohen:{}|fCohen:{}".format(result_d,result_f))
        print("=================")


    
