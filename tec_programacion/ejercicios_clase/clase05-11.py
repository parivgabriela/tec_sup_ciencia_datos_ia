#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
12) Escribir un algoritmo que pregunte al usuario una cantidad a invertir, el interes anual,
    y el numero de años. Mostrar el capital obtenido en la inversión.
"""

def validar_numero(tipo_de_valor):
    valido = True

    while valido == True:
        try:
            nota = float(input(f"Ingrese {tipo_de_valor}: "))
            if nota > 0:
                valido = False
            else:
                print("El valor debe ser mayor a cero")
        except:
            print("Ingrese un valor numerico")
    return nota

cantidad_a_invertir = 0
interes_anual = 0
cantidad_anios = 0
capital_total = 0
cantidad_a_invertir = validar_numero("cantidad a invertir")
interes_anual = validar_numero("interes anual")
cantidad_anios = validar_numero("cantidad de años")

capital_total = round(cantidad_a_invertir + cantidad_a_invertir * interes_anual * cantidad_anios, 2)
print(f"El capital obtenido es de: {capital_total}")