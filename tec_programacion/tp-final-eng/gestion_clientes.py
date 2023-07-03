import os
import time

from constants import ARCHIVO_CLIENTES
from validations import validate_number, validate_str
from gestion_libros import existe_dni_en_clientes, cambiar_estado_archivo
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

def update_data_client(new_data, position):
    POS_ADDRESS = 3
    POS_PHONE = 2
    dni = validate_number('dni', 7)
    consulta = existe_dni_en_clientes(dni)
    if consulta != '':
        print("Modificando datos...")
        if position == POS_ADDRESS:
            cambiar_estado_archivo(dni, new_data,POS_ADDRESS, ARCHIVO_CLIENTES)
        else:
            cambiar_estado_archivo(dni, new_data, POS_PHONE, ARCHIVO_CLIENTES)
        time.sleep(0.5)
        print("Modificacion exitosa")

def modify_client_information():
    # ask for address or phone number
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.7)
    menu = '''
        Modificar datos del cliente
        A - Modificar dirección
        B - Modificar telefono
    '''
    print(menu)
    option = input("Ingrese una opcion: ")

    if option.lower() == 'a':
        new_address = input("Nueva direccion: ")
        update_data_client(new_address, 3)
    elif option.lower() == 'b':
        new_phone = validate_number("telefono", 7)
        update_data_client(new_phone, 2)
    else:
        print("Opción incorrecta")