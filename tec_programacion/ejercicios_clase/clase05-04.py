#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def calcular_jornal():
    valido = True
    while valido == True:
        try:
            numHours = int(input("ingrese can de horas trabajadas: "))
            valido = False
        except ValueError:
            print("Debes escribir un numero entero: ")

    while valido == False:
        try:
            pagoJornal = int(input("ingrese el valor de la hora: "))
            valido = True
        except ValueError:
            print("Debes escribir un numero entero")
    calcJornal = pagoJornal * numHours
    print("El valor del jornal es: ", calcJornal)

def convertir_pies_o_pulgadas_a_cm():
    while True:
        try:
            ingOption = int(input("Ingrese 1 para pies, 2 para pulgadas:"))
        except ValueError:
            print("Debes ingresar un numero entero")
        else:
            if not(ingOption > 0 and ingOption < 3):
                print("Opcion incorrecta")
            else:
                break
    while True:
        try:
            ingDistancia = float(input("Ingrese distancia: "))
        except ValueError:
            print("Debes escribir un numero flotante")
        else:
            if ingDistancia <= 0:
                print("El valor debe ser mayor a cero")
            else:
                break
    inches = 2.45
    foot = 12 * inches
    if ingOption == 1:
        dist_total = round(foot * ingDistancia, 2)
    else:
        dist_total = round(inches * ingDistancia, 2)

    print(f"La distancia es: {dist_total}")

def celcius_to_farenheit():
    valido = True
    while valido == True:
        try:
            gCelcius = float(input("Ingrese temperatura en celcius: "))
        except ValueError:
            print("Debe ingresar un valor de correcto debe ser numerico entero o decimal")
        else:
            if gCelcius < 0:
                print("El valor debe ser mayor a cero")
            else:
                valido = False
    gFar = gCelcius * 1.8 + 32
    print(f"{gCelcius} grados celcius equivale a {gFar}") 

celcius_to_farenheit()

