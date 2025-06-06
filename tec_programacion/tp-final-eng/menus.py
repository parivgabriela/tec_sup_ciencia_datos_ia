import os
import time
from gestion_prestamo import mostrar_libros_disponibles, iniciar_prestamo, iniciar_devolucion
from disponibilidad import consultar_disponibilidad_por_titulo
from gestion_clientes import new_client, client_status, modify_client_information, delete_client_view
from gestion_libros import new_book_view, get_book_view, modify_book_view, delete_book_view
from validations import validar_respuesta_si_no

# constants
HEADER = """
    ######################################

            Sistema Biblioteca
    
    ######################################

"""
EXIT_MESSAGE = 'desea salir? [si/no] '
SELECT_OPTION_MSG = 'Elija una opcion: '

def menu_consulta_disponibilidad():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.7)
    estado = True
    msj_opcion_continuar = '\n¿desea consultar otro libro?  [si/no] '
    opcion_salida = ''

    msj = 'ingrese el nombre del libro: '
    nombre_libro = ''
    
    while estado:
        nombre_libro = input(msj)
        consultar_disponibilidad_por_titulo(nombre_libro)

        opcion_salida = validar_respuesta_si_no(msj_opcion_continuar)
        
        if opcion_salida.lower() == 'no':
            estado = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            estado = True

def menu_prestamo_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.7)

    estado = True
    estado_opcion = True
    msj_salida_consulta = '¿deasea hacer otra consulta? [si/no] '
    msj_salida_prestamo = '¿desea registrar otro prestamo? [si/no] '
    msj_salida_devolucion = '¿desea registrar otra devolucion? [si/no] '
    opcion_salida = ''
    opcion = ''
    msj_menu_prestamo = '''

        A - Consultar todos los títulos libro disponible
        B - Registrar préstamo
        C - Registrar Devolución
        X - salir
    '''
    msj_opcion_incorrecta = 'opcion incorrecta!'
    msj_advertencia = 'ingrese una de las opciones brindadas'
    


    while estado:
        estado_opcion = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print(HEADER + msj_menu_prestamo)
        opcion = input(SELECT_OPTION_MSG)
        if opcion.lower() == 'a':
            while estado_opcion:
                mostrar_libros_disponibles()
                opcion_salida = validar_respuesta_si_no(msj_salida_consulta)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')

        elif opcion.lower() == 'b':
            while estado_opcion:
                iniciar_prestamo()
                opcion_salida = validar_respuesta_si_no(msj_salida_prestamo)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False

        elif opcion.lower() == 'c':
            while estado_opcion:
                iniciar_devolucion()
                opcion_salida = validar_respuesta_si_no(msj_salida_devolucion)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False

                os.system('cls' if os.name == 'nt' else 'clear')

        elif opcion.lower() == 'x':
            estado = False

        else:
            print(msj_opcion_incorrecta)
            print(msj_advertencia)
            time.sleep(1.5)

def menu_gestion_cliente():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.7)

    estado = True
    estado_opcion = True
    opcion_salida = ''
    opcion = '' 
    msj_alta_cliente = '¿desea salir del alta del clientes? [si/no] '
    msj_consulta_cliente = '¿desea hacer otra consulta de cliente? [si/no] '
    msj_modificacion = '¿desea modificar otro cliente? [si/no] '
    msj_eliminacion = '¿desea eliminar otro cliente? [si/no] '
    msj_salida = '¿desea salir del menu? [si/no] '
    msj = 'ingrese la opcion deseada: '
    msj_menu_gestion = '''
        A - Alta de cliente
        C - Consulta estado del cliente
        M - Modificar teléfono o dirección del cliente
        E - Eliminar cliente 
        X - salir
    '''
    msj_opcion_incorrecta = 'opcion incorrecta!'
    msj_advertencia = 'ingrese una de las opciones brindadas'

    print(HEADER + msj_menu_gestion)

    while estado:
        estado_opcion = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print(msj_menu_gestion)
        opcion = input(msj)
        if opcion.lower() == 'a':
            while estado_opcion:
                new_client()
                opcion_salida = validar_respuesta_si_no(msj_alta_cliente)

                if opcion_salida.lower() == 'si':
                    estado_opcion = False
                os.system('cls' if os.name == 'nt' else 'clear')

        elif opcion.lower() == 'c':
            while estado_opcion:
                client_status()
                opcion_salida = validar_respuesta_si_no(msj_consulta_cliente)

                if opcion_salida.lower() =='no':
                    estado_opcion = False

        elif opcion.lower() == 'm':
            while estado_opcion:
                modify_client_information()
                opcion_salida = validar_respuesta_si_no(msj_modificacion)

                if opcion_salida.lower() =='no':
                    estado_opcion = False

        elif opcion.lower() == 'e':
            while estado_opcion:
                delete_client_view()
                opcion_salida = validar_respuesta_si_no(msj_eliminacion)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False 

        elif opcion.lower() == 'x':
            estado = False
        else:
            print(msj_opcion_incorrecta)
            print(msj_advertencia)
            time.sleep(1.5)


def menu_gestion_libros():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.7)

    estado = True
    estado_opcion = True
    opcion = '' 
    msj = 'ingrese la opcion deseada: '
    msj_alta = '¿desea dar de alta otro libro? [si/no] '
    msj_consulta = '¿desea consultar otro libro? [si/no] '
    msj_modificar = '¿desea modificar otro libro? [si/no] '
    msj_eliminar = '¿desea eliminar otro libro? [si/no] '
    msj_menu_gestion = '''
        A - Alta de libro
        C - Consultar un libro
        M - Modificar Libro
        E - Eliminar Libro 
        X - salir
    '''
    msj_opcion_incorrecta = 'opcion incorrecta!'
    msj_advertencia = 'ingrese una de las opciones brindadas'

    while estado:
        estado_opcion = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print(HEADER + msj_menu_gestion)
        opcion = input(msj)

        if opcion.lower() == 'a':
            while estado_opcion:
                new_book_view()
                opcion_salida = validar_respuesta_si_no(msj_alta)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False

        elif opcion.lower() == 'c':
            while estado_opcion:
                get_book_view()
                opcion_salida = validar_respuesta_si_no(msj_consulta)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False

        elif opcion.lower() == 'm':
            while estado_opcion:
                modify_book_view()
                opcion_salida = validar_respuesta_si_no(msj_modificar)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False

        elif opcion.lower() == 'e':
            while estado_opcion:
                delete_book_view()
                opcion_salida = validar_respuesta_si_no(msj_eliminar)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False

        elif opcion.lower() == 'x':
            estado = False

        else:
            print(msj_opcion_incorrecta)
            print(msj_advertencia)
            time.sleep(1.5)

def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.7)

    estado = True
    opcion = ''
    msj = 'ingrese la opcion deseada: '
    msj_menu ='''
    ######################################

            Sistema Biblioteca
    
    ######################################

        A - Consulta de disponibilidad
        B - Préstamo de Libro
        C - Gestión del cliente
        D - Gestión de Libro
        X - salir
    
    ######################################
          '''
    msj_opcion_incorrecta = 'opcion incorrecta!'
    msj_advertencia = 'ingrese una de las opciones brindadas'

    while estado:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(msj_menu)
        opcion = input(msj)

        if opcion.lower() == 'a':
            menu_consulta_disponibilidad()
        elif opcion.lower() == 'b':
            menu_prestamo_libro()
        elif opcion.lower() == 'c':
            menu_gestion_cliente()
        elif opcion.lower() == 'd':
            menu_gestion_libros()
        elif opcion.lower() == 'x':
            print("Gracias por usar el sistema.")
            estado = False
        else:
            print(msj_opcion_incorrecta)
            print(msj_advertencia)
            time.sleep(1.5)
