import time
from constants import ARCHIVO_CLIENTES, ARCHIVO_LIBROS, NULL, ESTADO_CLIENTE_LIBRE, ESTADO_CLIENTE_OCUPADO,\
     ESTADO_LIBRO_LIBRE, ESTADO_LIBRO_OCUPADO, ESTADO_CLIENTE_ELIMINADO

"""
1 - Préstamo de Libro / Película : puede tener un sub-Menú que tenga las opciones:
     A - Consultar todos los títulos/películas disponible (verificando el campo estado)
     B - Registrar préstamo (deberá buscar el libro o película y cambiar el campo de estado a "P" de prestado y en el cliente con "O" de ocupado)
     C - Registrar Devolución (pedir datos necesarios para buscar el cliente y libro o pelicula 
"""

CLIENTES = "CLIENTES"
LIBROS = "LIBROS"


COL_IDENTIFICADOR = 0

def leer_archivo(path):
    """Retorna una lista con las lineas del archivo
    Args:
        path (string): se le brinda una ruta por la cua va a buscar al archivo
    """
    list_file = []
    with open(path, 'r') as file:
        list_file = file.readlines()

    return list_file


def listar_libros_disponibles():
    """Retornara la lista de los libros con el estado"""
    libros_disponibles = []
    with open(ARCHIVO_LIBROS, 'r') as file:
        list_file = file.readlines()
        for libros in list_file:
            datos_libro = libros.split(',')
            if datos_libro[3] == 'D':
                titulo_compuesto = 'ISBN: '+ datos_libro[COL_IDENTIFICADOR] + ' Titulo: ' + datos_libro[1] + ' Autor: '+ datos_libro[2]
                libros_disponibles.append(titulo_compuesto)
    return libros_disponibles

def mostrar_libros_disponibles():
    """Generar la vista de los libros disponibles"""
    libros_disponibles = listar_libros_disponibles()
    print("######################################################\n   ")
    print("\t\tLibros Disponibles\n")
    for libros in libros_disponibles:
        print(libros)

def buscar_estado_id_archivo(id, archivo):
    """Retorna el estado de un id dado, verifica segun el path en 'archivo' que tipo de dato es
        y devuelve un dict con el estado de ese id
    Args:
        id (string): nro identificatorio unico
        archivo (string): ruta del archivo
    """
    lista_archivo = leer_archivo(archivo)
    estado_id = ''
    # busca linea a linea
    for linea in lista_archivo:
        # separo la linea en elementos
        datos_linea = linea.split(',')
        identificador_linea = datos_linea[COL_IDENTIFICADOR]
        if archivo == ARCHIVO_CLIENTES:
            if id == identificador_linea:
                estado_cliente_linea = datos_linea[4]
                estado_id = estado_cliente_linea
        elif archivo == ARCHIVO_LIBROS:
            if id == identificador_linea:
                estado_libro_linea = datos_linea[3]
                estado_id = estado_libro_linea
    return estado_id

def esta_disponible(id, tipo_de_dato):
    """devuele true o false si es ese elemento esta disponible

    Args:
        id (string): id del elemento puede ser dni de cliente o isbn de un libro
        tipo_de_dato (string): se indica que tipo de elemento es, asi puede buscarlo en el archivo correcto
    """
    if tipo_de_dato == CLIENTES:
        respuesta = buscar_estado_id_archivo(id,ARCHIVO_CLIENTES)
        #evaluo en disponible si el estado es L(libre)
        disponible = respuesta == ESTADO_CLIENTE_LIBRE
    else:
        respuesta = buscar_estado_id_archivo(id, ARCHIVO_LIBROS)
        disponible = respuesta == ESTADO_LIBRO_LIBRE

    #evaluo en disponible si el estado es L(libre)
    return disponible


# print(buscar_estado_id_archivo('5454654656546', ARCHIVO_LIBROS))
# print(buscar_estado_id_archivo('123456789', ARCHIVO_CLIENTES))

def cambiar_estado_cliente(dni_cliente, nuevo_estado):
    """cambiar estado_cliente

    Args:
        dni_cliente (string): dni del cliente a modificar
        nuevo_estado (string): nuevo estado puede ser L, O, B
    """
    posicion_estado_cliente = 4

    cambiar_estado_archivo(id_identificador=dni_cliente,
                   nuevo_estado=nuevo_estado,
                   posicion=posicion_estado_cliente,
                   archivo=ARCHIVO_CLIENTES)

def existe_elemento_en_archivo(identificador, archivo, posicion):
    lista_archivo = leer_archivo(archivo)
    # busca linea a linea
    for linea in lista_archivo:
        linea_archivo = linea.replace('\n', '')
        datos_linea = linea_archivo.split(',')
        linea_elemento = ''

        if identificador == datos_linea[posicion]:
            linea_elemento = datos_linea
            break

    return linea_elemento

def obtener_isbn_cliente(dni_cliente):
    isbn = ''
    renglon_info = existe_elemento_en_archivo(dni_cliente, ARCHIVO_CLIENTES,COL_IDENTIFICADOR)
    if renglon_info != '':
        isbn = renglon_info[5]
    return isbn

def existe_dni_en_clientes(dni_cliente):
    dni_encontrado = existe_elemento_en_archivo(identificador=dni_cliente,
                                                archivo=ARCHIVO_CLIENTES,
                                                posicion=COL_IDENTIFICADOR)
    if dni_encontrado[4] == ESTADO_CLIENTE_ELIMINADO:
        dni_encontrado = ''

    return dni_encontrado

def existe_isbn_en_libros(isbn):
    return existe_elemento_en_archivo(identificador=isbn,
                               archivo=ARCHIVO_LIBROS,
                               posicion=COL_IDENTIFICADOR)

def cambiar_estado_libros(isbn, nuevo_estado):
    """cambiar el estado del archivo libros por el nuevo estado

    Args:
        isbn (string)): numero identificatorio
        nuevo_estado (string): nuevo estado del libro puede ser L, P
    """
    posicion_estado_libros = 3

    cambiar_estado_archivo(id_identificador=isbn,
                   nuevo_estado=nuevo_estado,
                   posicion=posicion_estado_libros,
                   archivo=ARCHIVO_LIBROS)

def cambiar_estado_archivo(id_identificador, nuevo_estado, posicion, archivo):
    """cambia el estado de un elemento

    Args:
        id_identificador (string): id unico que identifica al elemento
        nuevo_estado (string): nuevo estado por el que se modificara
        posicion (string): _description_
    """
    list_archivo_actualizado = []
    datos_actualizados = ''

    list_archivo = leer_archivo(archivo)
    indice = 0
    for linea in list_archivo:
        linea_archivo = linea.replace('\n', '')
        datos_linea = linea_archivo.split(',')
        if id_identificador == datos_linea[COL_IDENTIFICADOR]:
            # marcar al cliente como ocupado
            datos_linea[posicion] = nuevo_estado
            datos_actualizados = ','.join(datos_linea)
            # se agrega el salto de linea
            renglon_nuevo = datos_actualizados + '\n'
            break
        indice += 1

    list_archivo_actualizado = list_archivo[:indice] + list(renglon_nuevo) + list_archivo[indice+1:]
    # escribir archivo con el dato actualizado
    nuevo_texto = ''.join(list_archivo_actualizado)
    with open(archivo, 'w') as file:
        file.write(nuevo_texto)

def validar_codigo_identificador(mensaje):
    valido = True
    while valido:
        try:
            identificador = input(f"Ingrese {mensaje}: ")
            identificador_int = int(identificador)
            if len(identificador) >= 7:
                valido = False
            else:
                print("El numero ingresado es muy corto")
        except:
            print("Ingrese un valor numerico valido")
    return identificador

def pedir_datos_usuario():
    isbn_ingresado = validar_codigo_identificador('ISBN (sin puntos)')
    dni_ingresado = validar_codigo_identificador("dni de cliente(sin puntos)")
    # verifico que libro este exista
    temp_libro = existe_isbn_en_libros(isbn_ingresado)
    if temp_libro == NULL:
        print("El ISBN No existe")
        isbn_ingresado = validar_codigo_identificador('ISBN (sin puntos)')
        temp_libro = existe_isbn_en_libros(isbn_ingresado)

    # verifico que el cliente exista
    temp_cliente = existe_dni_en_clientes(dni_ingresado)
    if temp_cliente == NULL:
        print("El dni del cliente no existe")
        dni_ingresado = validar_codigo_identificador("dni de cliente(sin puntos)")
        temp_cliente = existe_dni_en_clientes(dni_ingresado)

    if temp_libro == NULL: isbn_ingresado = ''
    if temp_cliente == NULL: dni_ingresado = ''
        
    return isbn_ingresado, dni_ingresado

def iniciar_prestamo():
    isbn_valido, dni_valido = pedir_datos_usuario()
    if isbn_valido != '' and dni_valido != '':
        registrar_prestamo(isbn_valido, dni_valido)
    elif isbn_valido == '' and dni_valido == '':
        print("Error al cargar los datos tanto DNI como ISBN no existen.\nVuelva a intentar")
    elif isbn_valido == NULL:
        print("El ISBN no existe, no se puede proceder al prestamo")
    elif dni_valido == NULL:
        print("El dni ingresado existe, no se puede proceder al prestamo")


def registrar_prestamo(isbn, dni_cliente):
    """registra el prestamo de un libro cambiando el estado a P 
        cambia el estado del cliente a P
        todo: verificar que el usuario exista y que tenga estado L(libre) 
        todo: verificar que dado isbn el libro este disponible/exista
    Args:
        isbn (string): numero unico que identifica un libro
        dni_cliente (string): numero unico que identifica al cliente
    """

    if esta_disponible(isbn, LIBROS) and esta_disponible(dni_cliente, CLIENTES):
        # cambiar estado de isbn a P
        cambiar_estado_libros(isbn, ESTADO_LIBRO_OCUPADO)
        # cambiar estado de cliente con el dni a P
        cambiar_estado_cliente(dni_cliente, ESTADO_CLIENTE_OCUPADO)
        # agrego el isbn al cliente y el dato dni_cliente al archivo libros
        cambiar_estado_archivo(id_identificador=isbn,
                               nuevo_estado=dni_cliente,
                               posicion=4,
                               archivo=ARCHIVO_LIBROS)
        cambiar_estado_archivo(id_identificador=dni_cliente,
                               nuevo_estado=isbn,
                               posicion=5,
                               archivo=ARCHIVO_CLIENTES)
        time.sleep(0.7)
        print("Se registro el prestamo exitosamente")
    else:
        print("No se puede concretar el prestamo")
        if not esta_disponible(isbn, LIBROS):
            print(f"El libro con ISBN {isbn} no se encuentra libre")
        if not esta_disponible(dni_cliente, CLIENTES):
            print(f"El cliente con dni {dni_cliente} tiene un prestamo en curso.")

def iniciar_devolucion():
    isbn_ingresado = validar_codigo_identificador("ISBN")
    temp_libro = existe_isbn_en_libros(isbn_ingresado)

    # verifico que el libro exista y este ocupado
    if len(temp_libro) > 0 and temp_libro[3] == ESTADO_LIBRO_OCUPADO:
        registrar_devolucion(isbn=isbn_ingresado, dni_cliente=temp_libro[4])
    elif temp_libro[3] != ESTADO_LIBRO_OCUPADO:
        print("El libro no se encuentra ocupado")
    else:
        print(f"El ISBN {isbn_ingresado} no existe")

def registrar_devolucion(isbn, dni_cliente):
    """registra la devolucion de un libro cambiando el estado a D 
        cambia el estado del cliente a L
        todo: verificar que el usuario exista y que tenga estado L(libre) 
        todo: verificar que dado isbn el libro este disponible/exista
    Args:
        isbn (int): numero unico que identifica un libro
    """

    # procesar devolucion
    # cambiar estado de ambos libro y cliente
    cambiar_estado_libros(isbn, ESTADO_LIBRO_LIBRE)
    cambiar_estado_cliente(dni_cliente, ESTADO_CLIENTE_LIBRE)
    # quito el isbn del cliente y el dato dni_cliente del archivo libros
    cambiar_estado_archivo(id_identificador=isbn,
                           nuevo_estado=NULL,
                           posicion=4,
                           archivo=ARCHIVO_LIBROS)
    cambiar_estado_archivo(id_identificador=dni_cliente,
                           nuevo_estado=NULL,
                           posicion=5,
                           archivo=ARCHIVO_CLIENTES)
    time.sleep(0.7)
    print("Se registro la devolucion")
