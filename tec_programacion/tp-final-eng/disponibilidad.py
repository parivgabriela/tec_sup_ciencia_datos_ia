# pto 0
from gestion_libros import ARCHIVO_LIBROS, leer_archivo, ESTADO_LIBRO_LIBRE, ESTADO_LIBRO_OCUPADO,\
    existe_elemento_en_archivo, ARCHIVO_CLIENTES

def buscar_existencia_titulo(titulo):
    list_archivo = leer_archivo(ARCHIVO_LIBROS)
    encontrados = []
    for linea in list_archivo:
        # todo esto busca en toda la linea, sea titulo o no
        if titulo.lower() in linea.lower():
            linea_separada = linea.split(',')
            if linea_separada[3] == ESTADO_LIBRO_LIBRE:
                datos_libro = f"Titulo: {linea_separada[1]}. Disponible"
                encontrados.append(datos_libro)
            elif linea_separada[3] == ESTADO_LIBRO_OCUPADO:
                # buscar nombre de la persona
                dni_cliente = linea_separada[0]
                datos_cliente = existe_elemento_en_archivo(dni_cliente, ARCHIVO_CLIENTES, 0)
                datos_libro = f"Titulo: {linea_separada[1]}. En prestado a cliente: {datos_cliente[1]} "
                encontrados.append(datos_libro)
    return encontrados

def consultar_disponibilidad_por_titulo(nombre):
    # buscar todas las existencias con el titulo
    lista_encontrados = buscar_existencia_titulo(nombre)

    if len(lista_encontrados) > 0:
        print("Elementos encontrados:\n")
        for renglon in lista_encontrados:
            print(renglon)
    else:
        print(f"No se encontraron libros con el nombre {nombre}")
