#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
De una lista de productos el operador introducirá el código del producto seleccionado, 
se mostrará el precio, se le pedirá la cantidad y luego se mostrará el precio final de la factura.
"""
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

def validar_cadena(tipo_de_valor):
    valido = True

    while valido == True:
        try:
            nota = str(input(f"Ingrese {tipo_de_valor}: "))
            if len(nota) >= 0:
                valido = False
        except:
            print("Ingrese un valor")
    return nota

def obtener_precio(codigo):
    lista_codigos = list(productos.keys())
    if codigo in lista_codigos:
        return productos[codigo]["precio"]

productos = { "300":{"nombre": "lapiz", "cantidad":"100", "precio":"50"}, "250":{"nombre": "lapicera", "cantidad":"100", "precio":"50"},
             "6980":{"nombre":"cartuchera","cantidad":"100", "precio":"50"}, "643":{"nombre":"plasticola","cantidad":"100", "precio":"50"}}

def imprimir_catalogo(productos):
    lista_codigos = list(productos.keys())
    for elemento in lista_codigos:
        print(f"{productos[elemento]['nombre']}:{elemento}" )
    pass
# imprimir catalogo
imprimir_catalogo(productos)
# pedir codigo
codigo = validar_cadena(" codigo del producto")
print(type(codigo))
precio = obtener_precio(codigo)
# mostrar precio
print(f"El precio del producto es: {precio}")
# pedir cantidad
cantidad = validar_numero("la cantidad")
# mostrar precio final
precio_total = cantidad * float(precio)
print(f"el precio total es de: {precio_total}")
