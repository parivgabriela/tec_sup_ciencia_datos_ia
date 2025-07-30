#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
nomArchivo = "demo.txt"
ArchObj = open(nomArchivo, 'w')
ArchObj.write("creamos un archivo segunda iteracion")
ArchObj.close()
ArchObj = open("demo.txt", 'r')
ArchObj.seek(5)
veo = ArchObj.read()
ArchObj.close()
print("veo: ", veo)

with open("demo.txt", 'w') as ObjArch:
    renglon_nuevo = input("ingrese untexto para grabar: ")
    ObjArch.write("le estoy escribiendo")
    ObjArch.write("segunda linea")
    ObjArch.write("tercera line")
    ObjArch.write(renglon_nuevo)

with open("demo.txt", 'w') as objArch:
    contenido = objArch.read()
    objArch.close()
print("demo.txt")
"""

with open("costumbres_argentinas.txt", 'r+') as cArchi:
    contenido = cArchi.read()
    final_del_archivo = cArchi.tell()
    cArchi.write("Que buena cancion!")
    cArchi.seek(final_del_archivo)
    contenido_agregado = cArchi.read()
    print("contenido: ", contenido)
    print("segudno: ", contenido_agregado)
    print(final_del_archivo)
    cArchi.close()
