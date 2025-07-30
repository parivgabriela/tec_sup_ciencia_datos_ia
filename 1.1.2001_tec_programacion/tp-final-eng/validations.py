# validations

def validate_number(message_input, len_min, len_max):
    """return a valid number that its len >= len_n

    Args:
        message_input (str): input message to print
        len_min (int): min require to validate number
        len_max (int): max require to validate number

    Returns:
        str: validate number, but it'll work as a string
    """
    valido = True
    while valido:
        try:
            identificador = input(f"Ingrese numero de {message_input}: ")
            identificador_int = int(identificador)
            if len(identificador) >= len_min and len(identificador) <= len_max:
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

def normalize(word):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ü", "u"),
    )
    for a, b in replacements:
        word = word.replace(a, b).replace(a.upper(), b.upper())
    return word

def validar_respuesta_si_no(mensaje):
    estado = True
    
    while estado:
        opcion_salida = input(mensaje)
        if opcion_salida.lower() != 'no' and opcion_salida.lower() != 'si':
            print("Opción incorrecta. Ingrese si o no")
        elif opcion_salida.lower() == 'no' or opcion_salida.lower() == 'si':
            estado = False
    return opcion_salida.lower()