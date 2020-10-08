# -*- coding:utf-8 -*-
'''
@author: Patricia Aguado Labrador
Programa para descodificar un texto.
'''
# Escribe la descodificacion de un fichero en otro
def decodificar(ficheroLec, ficheroEsc):
    f = open(ficheroLec, 'r+')
    n=8
    descodificacion= []
    
    while True: # Leer mientras haya contenido en el fichero
        bit = f.read(1)
        if not bit:
            break
        
        f.seek(n)   # Colocar puntero de ñectura en el bit 8 de la palabra
        letra = f.read(8)   # Leer los ultimos 8 bits de la palabra codificada
        n += 16
        descodificacion.append(chr(int(letra,2)))    # Añadir a una lista la letra a la que corresponden esos 8 bits en ascii
    f.close()
    
    f=open(ficheroEsc, 'w')
    for i in descodificacion:
        f.write(i)
    f.close()

# Validar ficheros
while True:
    lectura = input("Escriba el nombre del fichero a descodificar (con extension .txt): ")
    if(lectura[len(lectura)-4:] == '.txt'):
        break
    
while True:
    escritura = input("Escriba el nombre del fichero de escritura de la descodificacion (con extension .txt): ")
    if(escritura[len(escritura)-4:] == '.txt'):
        break

decodificar(lectura,escritura)
print("Operacion finalizada")

