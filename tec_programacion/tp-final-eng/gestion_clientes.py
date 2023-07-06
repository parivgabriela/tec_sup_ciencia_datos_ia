import os
import time

from constants import ARCHIVO_CLIENTES, ESTADO_CLIENTE_LIBRE
from validations import validate_number, validate_str
from gestion_prestamo import existe_dni_en_clientes, cambiar_estado_archivo, cambiar_estado_cliente, existe_isbn_en_libros

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
        isbn_info = existe_isbn_en_libros(consulta[5])
        print(f"\nEl cliente {consulta[1]} tiene en prestamo el libro: {isbn_info[1]}\n")
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
    else:
        print("No existe un dni asociado")

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

def delete_client(dni):
    cambiar_estado_cliente(dni, 'B')
    time.sleep(0.7)
    print("Eliminación exitosa")

def delete_client_view():
    datos_cliente = "Cliente: {dni}, nombre conpleto {nombre}"
    MSG_CONFIRMATION = 'Desea continuar? [si/no] '
    dni = validate_number('dni', 7)
    consulta = existe_dni_en_clientes(dni)

    if consulta != '':
        if consulta[4] == ESTADO_CLIENTE_LIBRE:
            print(datos_cliente.format(dni=dni,nombre=consulta[1]))
            option = input(MSG_CONFIRMATION)
            if option.lower() == 'si':
                delete_client(dni)
            elif option.lower() == 'no':
                print("Operación cancelada")
        else:
            print("Operación cancelada. El cliente no se encuentra libre de prestamos")
    else:
        print(f"El número de dni {dni} no existe")
