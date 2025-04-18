'''
3 - Gestión de Libro: tendrá un sub-menu:
    A - Alta de Libro-- 
    C - Consultar un libro(mostrando todos sus datos)--
    M - Modificar Libro
    E - Eliminar Libro
'''
import os
import time

def validacion_caracteres(isbm):
	contador = 0
	for caracter in isbm:
		if caracter == '0' or caracter == '1' or caracter == '2' or caracter == '3' or caracter == '4' or caracter == '5' or caracter == '6' or caracter == '7' or caracter == '8' or caracter == '9':
			contador = contador + 1 
			return False
		else:
			print('hay un caracter incorrecto, ingrese nuevamente el ISBM ')
			print('intente nuevamente ')
			return True

def validacion_longitud (isbm):
	longitud = 0
	estado = True
	for letra in isbm:
		longitud = longitud + 1
	
	if longitud != 13:
		print('longitud incorrecta ')
		print('intente nuevamente ')
		return estado
	else:
		#print('longitud correcta ')
		estado = validacion_caracteres(isbm)
		return estado
	

def validacion():
	isbm = 0
	estado = True
	while estado:
		try:
			isbm = input('ingrese el ISBM del libro: ')
			estado = validacion_longitud(isbm)
		except ValueError:
			print('hay un caracter invalido intente nuevamente ')
	return isbm

def creacion_archivo_libros():
	with open('libros.txt', 'w') as libros:
		libros.close()

def verificacion():
	resultado = os.path.exists('libros.txt')
	if resultado == True:
		print()
	else:
		creacion_archivo_libros()	
		
 

def verificacion_existencia(isbm):
	contador = 0
	with open('libros.txt', 'r') as archivo:
		lineas = archivo.readlines()

		for linea in lineas:
			if isbm in linea:
				renglon = linea.split(',')
				if renglon[0] == isbm:
					contador = contador + 1 
		
	if contador == 1:
		return True
	elif contador == 0:
		return False
# ------------------------------------------------FIN FUNCIONES GENERALES---------------------------------------------- #

#agrega isbn, titulo, autor, estado, dni_cliente
#en ese orden
def agregar_libro(isbm, titulo_libro, autor_libro, estado_libro, dni_cliente):
	verificacion()
	
	estado = verificacion_existencia(isbm)
	if estado == True:
		print('isbm en uso')
		print('ingrese otro')
	elif estado == False:
			with open('libros.txt', 'a') as archivo:
				archivo.write('\n%s,%s,%s,%s,%s'%(isbm, titulo_libro, autor_libro, estado_libro, dni_cliente))
				print('agregado satisfactoriamente')
				
			archivo.close()

def menu_gestion_libros():
    #declaracion de varables
	isbn = ''
	titulo = ''
	autor = ''
	estado = ''
	dni_cliente = ''
	
	os.system('cls')

	isbn = validacion()
	titulo = input('ingrese el titulo: ')
	autor = input('ingrese el autor: ')
	estado = 'L'
	dni_cliente = ''
    
    
	agregar_libro(isbn, titulo, autor, estado, dni_cliente)
	

# ------------------------------------------------FIN GGESTION DE LIBROS------------------------------------------------ #

def consulta_libro(nombre):

	with open('libros.txt', 'r') as archivo:
		lineas = archivo.readlines()

		for linea in lineas:
			if nombre in linea:
				renglon = linea.split(',')
				if renglon[3] == 'B': # DEBE SER MODIFICADO PARA LOS DISTINTOS ESTADOS
					print(renglon[1]+' de '+ renglon[2] + ' esta dado de baja')
				elif renglon[3] == 'L':
					print(renglon[1],' | ',renglon[2],' | ',renglon[3])
				elif renglon[3] == 'p':
					print(renglon[1],' de ',renglon[2],' fue prestado a ',renglon[4])
					
def menu_consulta_libro():
	isbm = ''

	isbm = validacion()
	consulta_libro(isbm)

	
# ------------------------------------------------FIN CONSULTA--------------------------------------------------------- #


def modificar(isbm):
	estado = True
	opcion = ''
	with open ('libros.txt', 'r') as R_archivo:
		with open('copialibros.txt', 'w') as W_archivo:
			linea = R_archivo.readline()
			while linea != '':
				renglon = linea.replace('\n','').split(',')


				if isbm == renglon[0]:
					print('se modificara nombre del libro y el nombre del autor ')
									
					nombre_libro = input('ingrese el nuevo nombre del libro: ')
					renglon[1] = nombre_libro
					
					nombre_autor = input('ingrese el nombre de autor: ')
					renglon[2] = nombre_autor

					W_archivo.writelines(renglon[0]+','+renglon[1]+','+renglon[2]+','+renglon[3]+','+renglon[4])
					print('se ha modificado correctamente ')
				else:
					
					W_archivo.writelines(linea)


				linea = R_archivo.readline()
		W_archivo.close()
	R_archivo.close()

	
	with open('copialibros.txt', 'r') as copia_archivo:
		with open('libros.txt', 'w') as archivo_original:
			for renglon in copia_archivo:
				archivo_original.write(renglon)
			copia_archivo.close()
		archivo_original.close()


def menu_modificacion():
	isbm = validacion()
	modificar(isbm)

# ------------------------------------------------FIN MODIFICACION------------------------------------------------------ #


def eliminacion_libro(isbm):
	'''
		se hara una baja logica
		se mantendra el regitro
	'''
	estado = True
	opcion = ''
	with open ('libros.txt', 'r') as R_archivo:
		with open('copialibros.txt', 'w') as W_archivo:
			linea = R_archivo.readline()
			while linea != '':
				renglon = linea.split(',')


				if isbm == renglon[0]:
					print('se eliminara el libro ')
					print(renglon[1]+ ', del autor '+renglon[2])
									
					renglon[3] = 'B'

					W_archivo.writelines(renglon[0]+','+renglon[1]+','+renglon[2]+','+renglon[3]+','+renglon[4])
					print('eliminado correctamente ')
				else:
					
					W_archivo.writelines(linea)


				linea = R_archivo.readline()
		W_archivo.close()
	R_archivo.close()

	
	with open('copialibros.txt', 'r') as copia_archivo:
		with open('libros.txt', 'w') as archivo_original:
			for renglon in copia_archivo:
				archivo_original.write(renglon)
			copia_archivo.close()
		archivo_original.close()

def menu_eliminacion_libro():

	isbm = validacion()
	eliminacion_libro(isbm)