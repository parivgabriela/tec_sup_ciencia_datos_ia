#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1)Mostrar el incremento de cant desde 1 a 100 utilizando while y otra usando for.

def mostrar_hasta_n(tope):
    for i in range(tope):
        print(i+1)

def mostrar_hasta_n_v2(tope):
    i = 0
    while i < tope:
        i += 1
        print(i)

numero = 10
print("for")
mostrar_hasta_n(numero)
print("while")
mostrar_hasta_n_v2(numero)
"""

"""2)Dadas 10 notas ingresadas, informar cuántos aprobaron (se aprueba con 4)."""
def validar_numero(tipo_de_valor):
    valido = True

    while valido == True:
        try:
            nota = int(input(f"Ingrese {tipo_de_valor}: "))
            if nota >= 0:
                valido = False
        except:
            print("Ingrese un valor numerico")
    return nota

total_notas = 10
contador_aprobados = 0

for nota in range(1, total_notas + 1):
    nota_valida = validar_numero(f"nota {nota}")
    if nota_valida >= 4:
        contador_aprobados += 1

print(f"Cantidad de aprobados: {contador_aprobados}")
