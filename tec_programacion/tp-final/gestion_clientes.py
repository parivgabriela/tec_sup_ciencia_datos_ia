import re
import menus
import time
import validaciones
from gestion_prestamo import esta_disponible, CLIENTES
#------------------------------ALTA del cliente----------------------------------
#1er tendría que fijarme que el usuario no existe
def imprimo_cliente(mensaje,dni,nombreCompleto,telefono,direccion, estado):
    print(f"{mensaje} \n \t\t   DNI: {dni}\n \t\t   Nombre y Apellido: {nombreCompleto}\n \t\t   Telefono: {telefono}\n \t\t   Dirección: {direccion}\n \t\t   Estado: {estado}\n")
    
def alta_cliente_en_archivo(dniAlta):
    #DNI, Nombre Completo, Telefono, direccion, estado, codigo de barra o ISBN si es libro
    mensajeTelefono = "Ingrese Teléfono - (Código de Área)- Número - (011) XXXX XXXX: "
    nombre = input("Ingrese el Nombre Completo - (Nombre y Apellido): ")
    nombreCompletoAlta = validar_campo_vacio(nombre,"Ingrese el Nombre Completo - (Nombre y Apellido): ")
    
    telefonoAlta = validar_telefono(mensajeTelefono)
    
    direccionAlta = validar_direccion("Ingrese dirección - Calle número piso depto : ")
    estadoAlta = "L"
    mensaje = "Los datos ingresado son: "
    imprimo_cliente(mensaje,dniAlta,nombreCompletoAlta,telefonoAlta,direccionAlta, estadoAlta)
    mensajeSalida = "Es correcto? [si/no]: "
    opcionSalida = validaciones.validar_respuesta_si_no(mensajeSalida)
    if opcionSalida == "si":    
        #ahora todo esto lo tengo que guardar en el archivo
        with open("clientes.txt", "a") as archivo:
            archivo.seek(0, 2) # Mover el puntero al final del archivo
            archivo.write(dniAlta +","+ nombreCompletoAlta+","+telefonoAlta+","+direccionAlta+","+estadoAlta+",\n")
        print('Se dio de alta al cliente satisfactoriamente.')
    else:
        print("Vuelva a intentarlo.")
        alta_cliente()

def alta_cliente():
    mensajeDNI = "Ingrese el DNI, éste debe contener 8 dígitos: "
    dni = valido_DNI(mensajeDNI)
    with open("clientes.txt", "r") as archivo: 
        existeCliente=verificar_cliente(archivo, dni)

    if existeCliente == True:
        print("El cliente ya existe!!")
        time.sleep(0.7)
        menus.menu_gestion_cliente()
        
    else:
        alta_cliente_en_archivo(dni)
def buscar_cliente(parametro):
    #como recibo una cadena de datos, lo que tengo que hacer es parcearlo la coma
    cliente = ""
    with open("clientes.txt", "r") as archivo:
        for linea in archivo:
            #Teniendo una linea, tendria que buscar el cliente(por ejemplo)
            clienteTemp = linea.split(",")
            #print(clienteTemp)
            if clienteTemp[0] == parametro: #Validar si tiene espacios TRIM
                cliente = clienteTemp
                #print(clienteTemp)
        return cliente
def verificar_cliente(archivo, parametro):
    #como recibo una cadena de datos, lo que tengo que hacer es parcearlo la coma
    existe = False
    for linea in archivo:
        #Teniendo una linea, tendria que buscar el cliente(por ejemplo)
        separado = linea.split(",")
        if separado[0] == parametro: #Validar si tiene espacios TRIM
            #print("El cliente ya está ingresado en el sistema")
            existe = True
    return existe
#------------------------------CONSULTA del cliente----------------------------------

def consulta_estado():

    mensajeDNI = "Ingrese el DNI, éste debe contener 8 dígitos: "
    mensaje = "El cliente ingresado tiene el estado: "
    dni_consulta = valido_DNI(mensajeDNI)
    with open("clientes.txt", "r") as archivo: 
        existeCliente=verificar_cliente(archivo, dni_consulta)
        if existeCliente != True:
            print("El cliente no existe")
        else:
            cliente=buscar_cliente(dni_consulta)
            imprimo_cliente(mensaje,cliente[0],cliente[1],cliente[2],cliente[3],cliente[4])
            #print("El estado del cliente es ",cliente[4])

#------------------------------MODIFICAR datos del cliente----------------------------------

def buscar_cliente_bool(parametro):
    #como recibo una cadena de datos, lo que tengo que hacer es parcearlo la coma
    existeCliente = False
    with open("clientes.txt", "r") as archivo:
        for linea in archivo:
            #Teniendo una linea, tendria que buscar el cliente(por ejemplo)
            cliente = linea.strip().split(",")
            #print(clienteTemp)
            if cliente[0] == parametro  and cliente[4] != 'B': 
                #print("El cliente existe")
                existeCliente = True
    return existeCliente

def modificar_telefono_cliente(dni, nuevo_telefono):
    with open("clientes.txt", "r+") as archivo:
        lineas = archivo.readlines()
        
        for i, linea in enumerate(lineas):
            cliente = linea.strip().split(",")
            
            if cliente[0] == dni:
                cliente[2] = nuevo_telefono
                lineas[i] = ",".join(cliente) + '\n'
                break
        
        archivo.seek(0)
        archivo.writelines(lineas)
    archivo.close()
    print("El teléfono del cliente ha sido modificado correctamente.")

def modificar_direccion_cliente(dni, nuevaDireccion):
    with open("clientes.txt", "r+") as archivo:
        lineas = archivo.readlines()
        
        for i, linea in enumerate(lineas):
            cliente = linea.strip().split(",")
            
            if cliente[0] == dni:
                cliente[3] = nuevaDireccion
                lineas[i] = ",".join(cliente) + '\n'
                break
        
        archivo.seek(0)
        archivo.writelines(lineas)
    archivo.close()
    print("La dirección del cliente ha sido modificado correctamente.")

def modificar_cliente():
    mensajeDNI = "Ingrese el dni, éste debe contener 8 dígitos: "
    dni = valido_DNI(mensajeDNI)
    encontreCliente = buscar_cliente_bool(dni) #encontre cliente
    if encontreCliente == True:
        opcion_mod=int(input("Ingrese [1] - Para modificar el teléfono \nIngrese [2] - Para modificar la dirección: "))
        ### Opción 1 - Modificar teléfono
        if opcion_mod == 1: 
            mensajeTelefono = "Ingrese el nuevo Teléfono - (Código de Área)- Número - 011 XXXX XXXX: "
            telefonoNuevo = validar_telefono(mensajeTelefono)
            modificar_telefono_cliente(dni, telefonoNuevo)
        ### Opción 2 - Modificar dirección
        elif opcion_mod == 2:
            mensajeDireccion = "Ingrese la nueva dirección: "
            direccionNueva = validar_direccion(mensajeDireccion)
            modificar_direccion_cliente(dni, direccionNueva)
        else:
            print("Elija una opción válida")
            modificar_cliente()
    else:
        print("El cliente no existe.")
        modificar_cliente()
        encontreCliente = False

#------------------------------BAJA del cliente----------------------------------
def eliminar_cambio_estado(dni):
    with open("clientes.txt", "r+") as archivo:
        lineas = archivo.readlines()
        
        for i, linea in enumerate(lineas):
            cliente = linea.strip().split(",")
            
            if cliente[0] == dni:
                cliente[4] = "B"
                lineas[i] = ",".join(cliente) + '\n'
                break
        
        archivo.seek(0)
        archivo.writelines(lineas)
    archivo.close()
    print("El cliente ha sido eliminado correctamente.")

def eliminar_cliente():
    dni = input("Ingrese el usuario a buscar (DNI): ")
    encontreCliente = buscar_cliente_bool(dni) #encontre cliente 
    if encontreCliente == True:
        if not esta_disponible(dni, CLIENTES):
            print("No se puede eliminar el cliente, adeuda libro")
        else:
            Mensaje = input("Está seguro que desea eliminar el cliente? Presione S/N: ")
            #Convertir a minuscula
            if Mensaje == 's':
                eliminar_cambio_estado(dni)
            else:
                print("El usuario no se ha eliminado")
    else:
        print("No se encontro el cliente")   
#------------------------------VALIDACIONES----------------------------------

def validar(parametro, longitud, mensaje):
    #Solo sirve para validar DNI, que puede tener 7 u 8 dígitos
    ok = 0
    while ok == 0:
        if (len(parametro) >= longitud - 1) & (len(parametro) <= longitud):
            ok = 1
        else:
            print("La longitud es incorrecta. Ingrese nuevamente.")
            parametro=input(mensaje)
    return parametro
def validar_campo_vacio(parametro, mensaje):
    ok = 0
    while ok == 0:
        if len(parametro) != 0:
            ok = 1
        else:
            print("Campo requerido, no puede estar vacio")
            parametro=input(mensaje)
    return parametro
def valido_DNI(mensaje):
    validoDNI = False
    while validoDNI == False:
        dni = input(mensaje)
        dniValido=validar(dni,8,mensaje)
        esNumero=validar_es_numero(dniValido)
        if esNumero:
            dniAlta = dniValido
            validoDNI = True
        else:
            print("El DNI tiene que contener solo números")
    return dniAlta 



def validar_es_numero(dni):
    patron = r'^[0-9]+$'
    if re.match(patron, dni):
        return True
    else:
        return False

def validar_telefono(mensaje):
    patron = r'^[0-9\s()-]+$'
    ok=True
    while ok:
        telefono = input(mensaje)
        if re.match(patron, telefono):
            ok = False
        else:
            print("El teléfono ingresado es inválido, ingrese el código de Área seguido por el número: ")
    return telefono       
# def validar_estado(parametro, longitud, mensaje):
#     ok = 0
#     while ok == 0:
#         if (not parametro.isdigit()) & (len(parametro) == longitud):
#             ok = 1
#         else:
#             print("Texto inválido. Debe ser un caracter.")
#             parametro=input(mensaje)
#     return parametro

def validar_direccion(mensaje):
    patron = r'^(?=.*[a-zA-Z])(?=.*[0-9\s]).+$'
    ok=True
    while ok:
        direccion = input(mensaje)
        if re.match(patron, direccion):
            ok = False
        else:
            print("La dirección ingresada es inválida, debe contener números y letras.")
    return direccion 

