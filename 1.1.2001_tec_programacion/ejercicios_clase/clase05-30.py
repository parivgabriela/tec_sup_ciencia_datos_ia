#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto. 
Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400.
def es_bisiesto(year):
    return year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0)
"""

"""
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que 
# decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
"""

def son_rimas(palabra_1, palabra_2):
    ultimas_3_palabra_1 = palabra_1[-3:]
    ultimas_3_palabra_2 = palabra_2[-3:]
    ultimas_2_palabra_1 = palabra_1[-2:]
    ultimas_2_palabra_2 = palabra_2[-2:]


    if ultimas_3_palabra_1 == ultimas_3_palabra_2:
        print("Riman")
    elif ultimas_2_palabra_1 == ultimas_2_palabra_2:
        print("Riman un poco")
    else:
        print("No riman")

def validar_palabra():
    valido = True
    while valido == True:
        palabra_1 = input("Ingrese una palabra: ")
        if len(palabra_1) > 3:
            valido = False
    return palabra_1        

palabra_1 = validar_palabra()
palabra_2 = validar_palabra()

son_rimas(palabra_1, palabra_2)


"""
Escribe una función llamada "elimina_duplicados"
que elimine los elementos duplicados en una lista  y los devuelva en una nueva lista.
"""