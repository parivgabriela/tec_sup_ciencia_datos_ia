def definir_votantes():
    """ inicio
	    cant_votos_cand_1 = 0
	    cant_votos_cand_2 = 0
	    cant_votos_cand_3 = 0
	    cantidad_votantes = 160
        candidato_1 = "candidato 1"
        candidato_2 = "candidato 2"
        candidato_3 = "candidato 3" 
        inicio para indice hasta cantidad_votantes
            escribir("ingrese voto")
            leer voto
            Si voto == candidato_1:
                candidato_1 += 1
            Si voto == candidato_2:
                candidato_2 += 1
            Si voto == candidato_3:
                candidato_3 += 1
        fin para
        mayor_votado = maximo(candidato1, candidato_2, candidato_3)
        return mayor votado
    """
    # dic_candidatos = {"candidato 1":0, "candidato 2": 0, "candidato 3": 0}
    lista_candidatos = ["candidato 1", "candidato 2", "candidato 3"]
    lista_votos_candidatos = [0, 0, 0]
    cantidad_votantes = 160
    for voto in range(0, cantidad_votantes):
        voto_ingresado = input("Ingrese voto ")
        if voto_ingresado == lista_candidatos[0]:
            lista_votos_candidatos[0] += 1
        elif voto_ingresado == lista_candidatos[1]:
            lista_votos_candidatos[1] += 1
        elif voto_ingresado == lista_candidatos[2]:
            lista_votos_candidatos[2] += 1

    candidato_1 = (lista_candidatos[0], lista_votos_candidatos[0])
    candidato_2 = (lista_candidatos[1], lista_votos_candidatos[1])
    candidato_3 = (lista_candidatos[2], lista_votos_candidatos[2])

    temp_mayor_votado = maximo_entre_dos(candidato_1, candidato_2)
    mayor_votado = maximo_entre_dos(temp_mayor_votado, candidato_3)
    
    return mayor_votado

def maximo_entre_dos(valor_1, valor_2):
    "retorna el maximo de 2 argumentos recibidos"
    if valor_1[1] >= valor_2[1]:
        return valor_1
    elif valor_2[1] > valor_1[1]:
        return valor_2

ganador = definir_votantes()
print(f"candidato ganador {ganador[0]} votos: {ganador[1]}")

# to try check if possible use the dict or not