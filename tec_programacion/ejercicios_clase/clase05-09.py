"""
10) Calcular la distancia recorrida por un auto a velocidad constante y en un tiempo determinado. 
Tener en cuenta la fórmula de Movimiento Rectilineo Uniforme:
Distancia = Velocidad * Tiempo
def calcular_distancia(velocidad:float, tiempo:float):
    distancia_total = round(velocidad * tiempo, 2)
    return distancia_total


valido = True
while valido == True:
    try:
        velocidad = float(input("Ingrese velocidad: "))
        if velocidad > 0:
            valido = False
        else:
            print("El valor debe ser mayor a cero")
    except:
        print("Ingrese un valor numerico")

valido = True

while valido == True:
    try:
        tiempo = float(input("Ingrese tiempo: "))
        if tiempo > 0:
            valido = False
        else:
            print("El valor debe ser mayor a cero")
    except:
        print("Ingrese un valor numerico")


distancia = calcular_distancia(velocidad, tiempo)
#istancia = calcular_distancia(velocidad, "sdfds")

print(f"Distancia total {distancia}")
"""


"""
11) Calcular el promedio de notas obtenidas por un alumno, teniendo 7 notas en el año.
"""

def validar_numero():
    valido = True

    while valido == True:
        try:
            nota = float(input("Ingrese nota: "))
            if nota > 0:
                valido = False
            else:
                print("El valor debe ser mayor a cero")
        except:
            print("Ingrese un valor numerico")
    return nota

total_notas = 2
suma_notas = 0
indice = 0
valido = True
for indice in range(total_notas):
    nota_ingresada = validar_numero()
    suma_notas += nota_ingresada

promedio = round(suma_notas/float(total_notas), 2)
print(f"el prodio es {promedio}")

#validar_numero()