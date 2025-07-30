import time
import os
from validations import validate_number
from gestion_prestamo import existe_isbn_en_libros, cambiar_estado_archivo, cambiar_estado_libros
from constants import ARCHIVO_LIBROS, NULL

'''
3 - Gestión de Libro: tendrá un sub-menu:
        A - Alta de Libro
        C - Consultar un libro (mostrando todos sus datos)
        M - Modificar Libro
        E - Eliminar Libro
'''
def add_new_book(isbn, title, author):
    """add new book to libros.txt file

    Args:
        isbn (int): id number of the book, this is unique
        title (str): name of the book
        author (str): full name of the author
    """
    print("Cargando datos...")
    new_line = f'\n{isbn},{title},{author},D,'
    try:
        with open(ARCHIVO_LIBROS, 'a') as file:
            file.write(new_line)
        time.sleep(0.5)
        print("Nuevo libro guardado correctamente")
    except:
        print("error al guardar cliente nuevo")


def new_book_view():
    #isbn, titulo, autor
    isbn =  validate_number('ISBN', 11)
    title = input("Ingrese el titulo del libro: ")
    author = input("Ingrese autor/a: ")
    # validar isbn
    temp_isbn = existe_isbn_en_libros(isbn)
    if temp_isbn == NULL:
        add_new_book(isbn, title, author)
    else:
        print(f"Error: Existe otro registro con el mismo ISBN {isbn}")

def get_book_info(temp_isbn):

    print(f"ISBN: {temp_isbn[0]}\nTitulo: {temp_isbn[1]}\nAutor/a: {temp_isbn[2]}\nEstado: {temp_isbn[3]}")


def get_book_view():
    isbn =  validate_number('ISBN', 1)
    temp_isbn = existe_isbn_en_libros(isbn)
    if temp_isbn != NULL:
        get_book_info(temp_isbn)
    else:
        print(f"Error: No existe el ISBN {isbn} en nuestro registro")

def modify_book(isbn, new_data, position):
    # Cambiar información del libro

    print("Modificando datos...")
    try:
        cambiar_estado_archivo(isbn, new_data,position, ARCHIVO_LIBROS)
        time.sleep(0.5)
        print("Modificacion exitosa")
    except:
        print("Error durante la actualización de datos")


def modify_book_view():
    view_menu_modify = '''
        Modificar datos del libro
        A - Modificar título
        B - Modificar autor/a
    '''
    
    print("Complete el codigo del libro a ser modificado")
    isbn =  validate_number('ISBN', 1)
    isbn_obtenido = existe_isbn_en_libros(isbn)
    if isbn_obtenido != NULL:
        #clear after pritn menu
        os.system('cls' if os.name == 'nt' else 'clear')
        print(view_menu_modify)
        # todo mostrar data anterior
        option = input("Ingrese una opcion de menu: ")
        if option.lower() == 'a':
            print("Titulo anterior: ", isbn_obtenido[1])
            new_title = input("Nuevo titulo: ")
            modify_book(isbn, new_title, 1)
        elif option.lower() == 'b':
            print("Autor/a anterior: ", isbn_obtenido[2])
            new_name = input("Nuevo nombre:")
            modify_book(isbn, new_name, 2)
        else:
            print("Opción incorrecta")
    else:
        print("No se encontro un libro con el código ingresado")

def delete_book(isbn):
    cambiar_estado_libros(isbn, 'B')
    time.sleep(0.7)
    print("Eliminación exitosa")

def delete_book_view():
    print("Complete el codigo del libro a ser eliminado")
    isbn =  validate_number('ISBN', 1)
    isbn_obtenido = existe_isbn_en_libros(isbn)
    if isbn_obtenido != NULL:
        get_book_info(isbn_obtenido)
        delete_book(isbn)
    else:
        print("No se encontro un libro con el ISBN ingresado")
