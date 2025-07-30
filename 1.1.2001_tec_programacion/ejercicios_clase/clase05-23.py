#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

"""
Calcular y mostrar la serie Fibonacci hasta el 100. (cada número es la suma de sus dos predecesores, comenzando por 0 y 1)
Empieza: 011235....

nros_serie_fibonacci = 0
order = 0
numero_n = 0
numero_n_2 = 1

while nros_serie_fibonacci <= 100:
    #print(f"n{numero_n} n2 {numero_n_2} fib{nros_serie_fibonacci} ")
    print (nros_serie_fibonacci)
    if order < 1:
        nros_serie_fibonacci = numero_n + numero_n_2
    else:
        nros_serie_fibonacci = numero_n + numero_n_2
    
        numero_n = numero_n_2
        numero_n_2 = nros_serie_fibonacci
    order += 1
"""
 
"""
Resolucion profe 
# serie Fibonacci
maxi = int(input("Ingrese el maximo: "))
serie = [0,1]  # 0 1 1 2 3 5 8...
uno = 0
dos = 1
suma = 0
while suma < maxi:
	suma = uno + dos
	print(uno, dos, suma)
	if suma < maxi:
		serie.append(suma)
	uno = dos
	dos = suma
print(serie)
#otra resolucion

serieFibo = fibo(num)   
print(serieFibo)
"""
"""
Se pide obtener de que tipo de triángulo se trata. Sabiendo que ingresan 3 datos correspondientes 
al largo de cada  lado. Recordar: el triángulo equilátero tiene los 3 lados iguales, 
el isósceles 2 lados iguales y el escaleno los 3 lados distintos.

lado_1 = 0
lado_2 = 0
lado_3 = 0
print("Ingrese los datos del triangulo")
lado_1 = validar_numero("lado 1: ")
lado_2 = validar_numero("lado 2: ")
lado_3 = validar_numero("lado 3: ")

if lado_1 == lado_2 == lado_3:
    print("Triangulo equilatero")
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("Triangulo isosceles")
else:
    print("Triangulo escaleno")
"""

"""
Definir una función que calcule la longitud de una lista o una cadena dada.
lista_ingresada = input("Ingrese lo valores de la lista separados por una coma")
lista = lista_ingresada.split(',')
# print(f"longitud: {len(lista)}")
contador = 0
for element in lista:
    contador += 1
print(f"longitud lista {contador}")
"""

"""Invertir una cadena (frase o palabra) ingresada
def invertir_frase(una_frase):
    return una_frase[::-1]

frase = input("Ingrese una cadena: ")
frase_invertida = invertir_frase(frase)
print(frase_invertida)

#otra forma
otra_lista = []
for elemento in frase:
    otra_lista.insert(0, elemento)
print("otra forma ", ''.join(otra_lista))
"""

"""Definir una funcion que se llame es_palidromo() que devuelva si una palabra ingresada es palíndromo o no
"""
frase = input("Ingrese una cadena: ")
mitad_cadena = int(len(frase))
for letra in range(mitad_cadena):
    if True:
        print("true")