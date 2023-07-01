#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6)Ingresar una frase y determinar la cantidad de espacios que contiene.

"""
frase = input("ingrese una frase")
cant_espacios = 0
#cantidad de espacios
for letra in frase:
    if letra == ' ':
        cant_espacios += 1
print(f"cantidad de espacios {cant_espacios}")