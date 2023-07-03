import time
from validations import validate_number, validate_str
from gestion_prestamo import existe_isbn_en_libros
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
