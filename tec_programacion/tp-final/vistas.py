import shutil

def print_titulo_relleno():
    columns =  shutil.get_terminal_size().columns
    relleno = '*'*(columns-2)
    titulo = 'SISTEMA BIBLIOTECA'
    print(relleno + '\n')
    print(titulo.center(shutil.get_terminal_size().columns))
    print('\n' + relleno)

def print_subtitulo(s):

    print(s.center(shutil.get_terminal_size().columns))
    columns =  shutil.get_terminal_size().columns
    relleno = '*'*(columns-2)
    print(relleno + '\n')

def header(subtitulo):
    print_titulo_relleno()
    print_subtitulo(subtitulo)

# '{:*^99}'.format(imprimir)

