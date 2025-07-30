#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#leer archivo
#construya una lista con las palabras leidas del texto

def mostrar_menu():
    print("----menu----")
    print("Ingrese solo los numeros de las opciones")
    print("Buscar contacto--> Opcion 1()")
    print("Modificar contacto--> Opcion 2()")
    print("Eliminar contacto--> Opcion 3()")

def validar_numero(tipo_de_valor):
    valido = True

    while valido == True:
        try:
            numero = int(input(f"Ingrese {tipo_de_valor}: "))
            if numero >= 0:
                valido = False
        except:
            print("Ingrese un valor numerico")
    return numero


def es_cliente(un_cliente):
    list_nombres_clientes = list(dic_clientes.keys())
    return un_cliente in list_nombres_clientes

def eliminar_cliente(un_cliente):
    pass

def transformar_a_dict(list_clients):
    dic_clientes = {}

    for cliente in list_clients:
        #quitar enter
        temp_cliente = cliente.split('\n')    
        cliente, telefono = temp_cliente.pop(0).split(',')
        dic_clientes[cliente] = int(telefono)
    return dic_clientes
#escribir un programa para que gestione nombres y telefonos del clientes

#leer cliente 
#inicializar
#si no existe guardarlo

with open('archivo.txt', 'r') as file:
    list_clients = file.readlines()
    print(list_clients)
dic_clientes = transformar_a_dict(list_clients)
#debe poder añadir el numero de un cliente
mostrar_menu()
opcion_valida = validar_numero()
cliente_ingresado = input("Ingres un cliente") 
#se puede elimiar el numero de un cliente
if not es_cliente(cliente_ingresado):
    numero = input("Ingrese numero del cliente")
else:
    respuesta = input("desea eliminar cliente? 1(Si)/ 0 (No)")
    if respuesta == 1:
        print("falta eliminar")
        eliminar_cliente(cliente_ingresado)

#se debe guardar en listado.txt grabar la lista en el txt

#cada cliente con 

"""
Diseña un programa que cuente la cantidad de caracteres de un archivo incluyendo los saltos de linea
cant_lineas = 0
with open('un_archivo.txt', 'r') as file:
    lista_elementos = file.readlines()
    
    for elemento in lista_elementos:
        cant_lineas = cant_lineas + len(elemento)

    print(cant_lineas)
"""
