import os
import time
import gestion_libros
import gestion_clientes
from disponibilidad import consultar_disponibilidad_por_titulo
from gestion_prestamo import mostrar_libros_disponibles, iniciar_prestamo, iniciar_devolucion
from validaciones import validar_respuesta_si_no
from vistas import header

def menu_consulta_disponibilidad():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.7)
    estado = True
    msj_opcion_continuar = '\n¿desea consultar otro libro?  [si/no] '
    opcion_salida = ''
    msj = 'Ingrese el nombre del libro: '
    nombre_libro = ''
    header("Disponibilidad")
    while estado:
        nombre_libro = input(msj)
        consultar_disponibilidad_por_titulo(nombre_libro)
        opcion_salida = validar_respuesta_si_no(msj_opcion_continuar)

        if opcion_salida.lower() == 'no':
            estado = False

def menu_prestamo_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.7)
    header("Prestamos")
    estado = True
    estado_opcion = True
    msj_salida_continuar = '¿deasea hacer otra consulta? [si/no] '
    msj_salida_prestamo = '¿desea registrar otro prestamo? [si/no] '
    msj_salida_continuar_devolucion = '¿desea registrar otra devolucion? [si/no] '
    msj_salida = '¿desea salir? [si/no] '
    opcion_salida = ''
    opcion = ''
    msj = 'ingrese la opcion deseada: '
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
        print(msj_menu_prestamo)
        opcion = input(msj)
        if opcion.lower() == 'a':
            while estado_opcion:
                mostrar_libros_disponibles()
                opcion_salida = validar_respuesta_si_no(msj_salida_continuar)

                if opcion_salida == 'no':
                    estado_opcion = False

        elif opcion.lower() == 'b':
            while estado_opcion:
                iniciar_prestamo()
                opcion_salida = validar_respuesta_si_no(msj_salida_prestamo)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False
        elif opcion.lower() == 'c':
            while estado_opcion:
                iniciar_devolucion()
                opcion_salida = validar_respuesta_si_no(msj_salida_continuar_devolucion)
                if opcion_salida.lower() == 'no':
                    estado_opcion = False
        elif opcion.lower() == 'x':
            estado = False
        else:
            print(msj_opcion_incorrecta)
            print(msj_advertencia)
            time.sleep(1.5)

def menu_gestion_cliente():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.7)
    header("Gestion Clientes")
    estado = True
    estado_opcion = True
    opcion_salida = ''
    opcion = '' 
    msj_alta_cliente = '¿desea salir del alta del clientes? [si/no]'
    msj_consulta_cliente = '\n¿desea hacer otra consulta de cliente? [si/no]'
    msj_modificacion = '¿desea modificar otro cliente? [si/no]'
    msj_eliminacion = '¿desea eliminar otro cliente? [si/no]'
    msj_salida = '¿desea salir del menu? [si/no]'
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

    while estado:
        estado_opcion = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print(msj_menu_gestion)
        opcion = input(msj)
        if opcion.lower() == 'a':
            while estado_opcion:
                gestion_clientes.alta_cliente()
                opcion_salida = validar_respuesta_si_no(msj_alta_cliente)
                if opcion_salida.lower() == 'si':
                    estado_opcion = False
        elif opcion.lower() == 'c':
            while estado_opcion:
                gestion_clientes.consulta_estado()
                opcion_salida = validar_respuesta_si_no(msj_consulta_cliente)
                if opcion_salida.lower() == 'no':
                    estado_opcion = False
        elif opcion.lower() == 'm':
            while estado_opcion:
                gestion_clientes.modificar_cliente()
                opcion_salida = validar_respuesta_si_no(msj_modificacion)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False
        elif opcion.lower() == 'e':
            while estado_opcion:
                gestion_clientes.eliminar_cliente() 
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

    estado = True
    estado_opcion = True
    opcion = '' 
    msj = 'ingrese la opcion deseada: '
    msj_alta = '¿desea dar de alta un libro? [si/no]'
    msj_consulta = '¿desea consultar un libro? [si/no]'
    msj_modificar = '¿desea modificar un libro? [si/no]'
    msj_eliminar = '¿desea eliminar un libro? [si/no]'
    msj_salida = '¿desea salir? [si/no]'
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
        print(msj_menu_gestion)
        opcion = input(msj)

        if opcion.lower() == 'a':
            while estado_opcion:
                #                   #
                #   alta del libro  #
                #                   #
                gestion_libros.menu_gestion_libros()
                # opcion_salida = input(msj_alta)
                opcion_salida = validar_respuesta_si_no(msj_alta)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False

        elif opcion.lower() == 'c':
            while estado_opcion:
                #                   #
                #      consulta     #
                #      de libro     #
                #                   #
                gestion_libros.menu_consulta_libro()
                # opcion_salida = input(msj_consulta)
                opcion_salida = validar_respuesta_si_no(msj_consulta)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False
        elif opcion.lower() == 'm':
            while estado_opcion:
                #                       #
                #      modificacion     #
                #      de libros        #
                #                       #
                gestion_libros.menu_modificacion()
                opcion_salida = validar_respuesta_si_no(msj_modificar)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False

        elif opcion.lower() == 'e':
            while estado_opcion:
                #                       #
                #       eliminacion     #
                #       logica de       #
                #       libros          #
                #                       #
                gestion_libros.menu_eliminacion_libro()
                # opcion_salida = input(msj_eliminar)
                opcion_salida = validar_respuesta_si_no(msj_eliminar)

                if opcion_salida.lower() == 'no':
                    estado_opcion = False

        elif opcion.lower() == 'x':
            estado = False
        else:
            print(msj_opcion_incorrecta)
            print(msj_advertencia)
            time.sleep(3)

def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    estado = True
    opcion = ''
    msj = 'ingrese la opcion deseada: '
    msj_menu ='''
        A - Consulta de disponibilidad
        B - Préstamo de Libro
        C - Gestión del cliente
        D - Gestión de Libro
        X - salir
          '''
    msj_opcion_incorrecta = 'opcion incorrecta!'
    msj_advertencia = 'ingrese una de las opciones brindadas'
    msj_salida = '¿desea salir? [si/no] '

    while estado:
        os.system('cls' if os.name == 'nt' else 'clear')
        header("Menu Principal")

        print(msj_menu)
        opcion = input(msj)

        if opcion.lower() == 'a':
            menu_consulta_disponibilidad()
        elif opcion.lower() == 'b':
            menu_prestamo_libro() #gabriela
        elif opcion.lower() == 'c':
            menu_gestion_cliente() #raquel
        elif opcion.lower() == 'd':
            menu_gestion_libros() #andres
        elif opcion.lower() == 'x':
            opcion = validar_respuesta_si_no(msj_salida)
            if opcion == 'si':
                print("Gracias por usar el sistema de biblioteca.")
                estado = False
        else:
            print(msj_opcion_incorrecta)
            print(msj_advertencia)
            time.sleep(3)
