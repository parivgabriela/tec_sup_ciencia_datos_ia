#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
"""
Realizar un programa cuente el numero de caracteres de un archivo de texto,
incluyendo los saltos de linea. El nombre del archivo se pide al usuario.

#inicio
archivo = validar_ingreso()

archivo_lista = leer_archivo(archivo)

cant_total = contar_caracteres(archivo_lista)

print(f"la cantidad de caracteres es de: {cant_total}")
"""

# leer el archivo
def leer_archivo(path):
    with open(path, 'r') as file:
        list_file = file.readlines()
    return list_file

def contar_caracteres(archivo_lista):
    cant_lineas = 0
    for elemento in archivo_lista:
        cant_lineas = cant_lineas + len(elemento)

    return cant_lineas

def validar_nombre_archivo():
    archivo = input('Ingrese nombre del archivo: ')

    while not os.path.isfile(archivo):
        archivo = input('Ingrese nombre del archivo valido: ')

    return archivo

def existe_palabra_en_archivo(archivo, palabra):
    matches = []
    for renglon in archivo:
        if palabra in renglon:
            matches.append(renglon)
    print(matches)
    return len(matches) > 0


"""
Realizar un programa que, dada una palabra ingresada y un nombre de archivo, 
determine si se encuentra dentro del archivo.
"""
#inicio
palabra_usuario = input("Ingrese una palabra")

archivo = validar_nombre_archivo()
list_arch = leer_archivo(archivo)

if existe_palabra_en_archivo(list_arch, palabra_usuario):
    print("La palabra existe")
else:
    print("La palabra no existe")