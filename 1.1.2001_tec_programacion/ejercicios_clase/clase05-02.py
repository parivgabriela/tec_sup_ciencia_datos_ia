#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6) Escriba el algoritmo para determinar la cantidad de minutos (y segundos) 
de acuerdo a una cantidad de segundo ingresados.

inicio
    minutos_total = 0
    segundos_restates = 0
    leer total_segundos
    minutos_total = total_segundos / 60
    segundos_restantes = total_segundos % 60

minutos_total = 0
segundos_restantes = 0
total_segundos = int(input("Ingrese segundos "))
minutos_total = total_segundos // 60
segundos_restantes = total_segundos % 60

print(f"minutos {minutos_total}, segundos {segundos_restantes}")
"""

"""
# 7) Escriba un algoritmo que pida una distancia en pies y pulgadas y que escriba dicha distancia en centímetros. 
#  Se recuerda que:
#  1 PIE = 12 pulgadas 
#  1 pulgada = 2,54 cm
pulgada = 2.54
un_pie = 12 * pulgada

medida_pies_ingresada = float(input("Ingrese distancia en pies "))
medida_pulgadas_ingresada = float(input("Ingrese distancia en pulgadas "))
distancia_pies_a_cm = medida_pies_ingresada * un_pie
distancia_pulgadas_a_cm = medida_pulgadas_ingresada * pulgada

print(f"la distancia ingresada en pies es de {distancia_pies_a_cm} cm")
print(f"la distancia ingresada en pulgadas es de {distancia_pulgadas_a_cm} cm")
"""

"""
Escriba un algoritmo que pida una temperatura en grados Celsius y que convierta dicha
# temperatura en grados Fahrenheit. Se recuerda que la relacion entre grados Celsius (C)
# y grados Fahrenheit (F) es la siguiente: F = 1,8 * C + 32.
def celcius_to_farenheit(celcius):
    return 1.8 * celcius +32

celcius = float(input("Ingrese temperatura en celcius"))
grado_en_farenheit = round(celcius_to_farenheit(celcius), 2)
print(f"Conversion de temperatura en Celcius {celcius} a Farenheit {grado_en_farenheit}")
"""

"""
9) Escriba un algoritmo que pregunte al usuario el número de horas trabajadas y el costo
#  por hora. Determinar el pago de jornal que le corresponde.
# numHoras = int(input("Ingrese cantidad de horas trabajadas por día: "))
"""

valido = True
while valido == True:
    try:
        horas_trabajadas = int(input("Ingrese horas trabajadas: "))
        costo_hora = float(input("Ingrese el costo por hora: "))
        jornal_total = horas_trabajadas * costo_hora
        print(f"Jornal {jornal_total}")
        valido = False
    except ValueError:
        valido = False
        print("Please insert a correct value")
