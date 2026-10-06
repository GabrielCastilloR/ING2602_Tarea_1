# -*- coding: utf-8 -*-
"""
Autor: Gabriel Andres Castillo Rosales

Objetivo:
    Estudiar el error en la derivada de f(x) = sin(x) en x_0 = 1.0
"""

import matplotlib.pyplot as plt
import numpy as np

def errorDifProg(vecH, x_0):
    """errorDifProg : Calcula la diferenciacion finita progresiva para cada paso h en vecH, luego calcula el error absoluto para cada diferenciacion obtenida
    Args:
        vecH (array-like): Pasos de diferenciacion h
        x_0 (float): Centro de la diferenciacion
    Returns:
        numpy array: Arreglo de errores absolutos de cada paso h
    """
    D_h = [ ((np.sin(x_0+h) - np.sin(x_0))/h) for h in vecH ]
    return np.array([ np.abs(np.cos(x_0) - dh) for dh in D_h ])

def errorDifCent(vecH, x_0):
    """errorDifReg : Calcula la diferenciacion finita centrada para cada paso h en vecH, luego calcula el error absoluto para cada diferenciacion obtenida
    Args:
        vecH (array-like): Pasos de diferenciacion h
        x_0 (float): Centro de la diferenciacion
    Returns:
        numpy array: Arreglo de errores absolutos de cada paso h
    """
    D_h = [ ((np.sin(x_0 + h) - np.sin(x_0 - h))/(2*h)) for h in vecH ]
    return np.array([ np.abs(np.cos(x_0) - dh) for dh in D_h ])

def plotLog2(x, errorProg, errorCent):
    """plotLog2 : Grafica los errores absolutos obtenidos en el ejercicio.
    Args:
        x (array_like): vector de pasos h en escala logaritmica.
        f1 (array_like): Valores evaluados usando diferencia hacia adelante O(h).
        f2 (array_like): Valores evaluados usando diferencia hacia centrada O(h).
    """
    #Preparacion lineas de referencia O(h), O(h^2) y puntos de error minimo
    refLineal, refCuadratica = x, x**2
    minProg, minCent = np.where(errorProg == errorProg.min())[0], np.where(errorCent == errorCent.min())[0]
    minProg, minCent =x[minProg[0]], x[minCent[0]]

    #Ploteo
    plt.cla() #Limpia el plot para asegurar que no se muestren imagenes fantasma.
    
        # Asegura escala logaritmica y permite el uso de scatter plots
    plt.xscale("log")
    plt.yscale("log")

    plt.plot(x, refLineal, c="black", lw=0.75, ls="--", label="O(h)") #Ploteo referencia O(h)
    plt.plot(x, refCuadratica, c="black", lw=0.75, ls="-.", label="O(h^2)") #Ploteo referencia O(h^2)
    
    plt.scatter(x, errorProg, c="blue", lw=0.7, marker="+", label=f"Progesiva (h* = {minProg})") #Ploteo Error Difereneciacion Progresiva
    plt.scatter(x, errorCent, c="green", lw=0.7, marker="x", label=f"Centrada (h* = {minCent})") #Ploteo Error Difereneciacion Centrada

    #Leyendas y texto
    plt.title("Estudio Diferenciación Finita de f(x) = sin(x) centrada en x = 1.0")
    plt.xlabel("Tamaño del paso h")
    plt.ylabel("Error Absoluto del esquema")
    plt.grid(visible=True, which="both", axis="both")
    plt.legend()
    plt.show() # Muestra el ploteo
        # Para guardar el ploteo, comentar linea 65 y descomentar lineas 67 y 68
    #plt.savefig("Grafico_1.png", format="png", metadata={"Author": "Gabriel Castillo Rosales", "Title": "Estudio Diferenciación Finita de f(x) = sin(x) centrada en x = 1.0"})
    #plt.close()

def main():
    h = np.logspace(0, -14, 60)
    plotLog2(h, errorDifProg(h, 1), errorDifCent(h, 1))

main()