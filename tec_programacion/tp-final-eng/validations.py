# validations

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