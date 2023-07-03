from constants import ARCHIVO_CLIENTES


'''
        A - Alta de cliente
        C - Consulta estado del cliente
        M - Modificar teléfono o dirección del cliente
        E - Eliminar cliente 
        X - salir
'''
def validate_number(message_input, len_n):
    """return a valid number that its len >= len_n

    Args:
        message_input (str): input message to print
        len_n (int): min require to validate number

    Returns:
        str: validate number, but it'll work as a string
    """
    valido = True
    while valido:
        try:
            identificador = input(f"Ingrese numero de {message_input}: ")
            identificador_int = int(identificador)
            if len(identificador) >= len_n:
                valido = False
            else:
                print("El numero ingresado es muy corto")
        except:
            print("Ingrese un valor numerico valido")
    return identificador

def validate_str(message_input, len_n):
    """return a valid number that its len >= len_n

    Args:
        message_input (str): input message to print
        len_n (int): min require to validate number

    Returns:
        str: validate number, but it'll work as a string
    """
    valido = True
    while valido:
        try:
            cadena = input(f"Ingrese {message_input} del cliente: ")
            # todo check punctuations input
            if cadena.isalpha() and len(cadena) >= len_n:
                valido = False
            else:
                print(f"El {message_input} no debe contener números y no ser muy corto")
        except:
            # todo check accents in prints
            print(f"Por favor intente nuevamente")
    return cadena

def new_client():
    len_n = 7 # longitud minima de un documento
    dni = validate_number('DNI', len_n)
    name = validate_str('nombre', 2)
    last_name = validate_str('apellido', 2)
    full_name = name + ' ' + last_name
    address = input("Ingrese dirección completa: ")
    phone = validate_number("numero de telefono", 8)
    add_new_client(dni, full_name, address, phone)

def add_new_client(dni, full_name, address, phone_number):
    new_client_line = f"\n{dni},{full_name},{phone_number},{address},L,"
    try:
        with open(ARCHIVO_CLIENTES, 'a') as file:
            file.write(new_client_line)
        print("Nuevo cliente guardado correctamente")
    except:
        print("error al guardar cliente nuevo")
