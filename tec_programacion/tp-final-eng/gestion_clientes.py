from constants import ARCHIVO_CLIENTES
from validations import validate_number, validate_str
from gestion_libros import existe_dni_en_clientes
'''
        A - Alta de cliente
        C - Consulta estado del cliente
        M - Modificar teléfono o dirección del cliente
        E - Eliminar cliente 
        X - salir
'''


def new_client():
    len_n = 7 # longitud minima de un documento
    dni = validate_number('DNI', len_n)
    name = validate_str('nombre', 2)
    last_name = validate_str('apellido', 2)
    full_name = name + ' ' + last_name
    address = input("Ingrese dirección completa: ")
    phone = validate_number("numero de telefono", 8)
    consulta = existe_dni_en_clientes(dni)
    if consulta == '':
        add_new_client(dni, full_name, address, phone)
    else:
        print("Error: existe otro cliente con el mismo dni")

def add_new_client(dni, full_name, address, phone_number):
    new_client_line = f"\n{dni},{full_name},{phone_number},{address},L,"
    # chequea que exista otro dni 
    try:
        with open(ARCHIVO_CLIENTES, 'a') as file:
            file.write(new_client_line)
        print("Nuevo cliente guardado correctamente")
    except:
        print("error al guardar cliente nuevo")

def client_status():
    dni = validate_number('DNI', 7)
    consulta = existe_dni_en_clientes(dni)
    ##revisar que numero trae
    if consulta == '':
        print("No existe un cliente con el dni ingresado")
    elif consulta[4] == 'O':
        print("Estado: Ocupado")
    elif consulta[4] == 'L':
        print("Estado: Libre")
    elif consulta[4] == 'B':
        print("Estado: Baja.")
