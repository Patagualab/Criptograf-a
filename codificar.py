# -*- coding: utf-8 -*-
'''
@author: Patricia Aguado Labrador
Programa para codificar un texto.
'''

# Suma dos elementos del cuerpo F16
def sumar(num1, num2):
    resultado =''
    
    for i in range(len(num1)):
        
        if num1[i] == num2[i]:  # Compara cada cifra del primer numero con la del segundo
            resultado += '0'    # Si las cifras son iguales la suma XOR me dara 0
        else:
            resultado += '1'    # Si las cifras son distintas me dara 1
            
    return resultado

# Multiplica dos elementos del cuerpo F16
def multiplicar(num1, num2):
    
    v1 = alphas.get(num1)   # Obtengo el valor del primer numero
    v2 = alphas.get(num2)   # Obtengo el valor del segundo numero
    
    if (v1 == 0 or v2 == 0):
        resultado = 0
    else:    
        resultado = v1 + v2     # Sumo los valores por la multiplicacion en F16 es como la suma en Z15
    
    while (resultado > 15): # Hago modulo 15 si el resultado es mayor que 15
        resultado -= 15
    
    for key in alphas:      # Busco por clave si hay algun valor igual que el resultado obtenido
        if alphas[key] == resultado:
            return key      # Devuelvo la clave cuyo valor coincide con el buscado

# Codifica un mensaje de un fichero a Ascii y devuelve una lista con cada letra codificada en ascii
def codingAscii(mensaje):
    f = open(lectura, 'r+')
    mensaje = f.read()
    f.close()
    
    lista = []
    
    for i in mensaje:
        num = bin(ord(i))[2:]      
        while len(num)<8:   # Hacer que la longitud de la palabra sea 8
            i = 8-len(num)
            num = i*'0' +num
        
        lista.append(num)
    return(lista)    

# Codifica el Ascii utilizando el codigo    
def codificar(mensaje):
    numero = ''
    codificacion = []
    for n in mensaje:   # Dividir la letra en bloques de 4 digitos
        parte1 = n[:4]
        parte2 = n[4:]
        
        for i in range(0,4):    # Multiplicar por la generatriz
            n1 = multiplicar(parte1, g[0][i])
            n2 = multiplicar(parte2, g[1][i])
            
            numero += sumar(n1, n2)
            
        codificacion.append(numero) # Añadir letra codificada, ahora de longitud 16 a una lista
        numero=''
        
    f = open (escritura, 'w' ) 
    for i in codificacion:    
        f.write(i)
    f.close()

# Matriz generatriz
g = [['0010','0011','0001','0000'],
     ['0110','0111','0000','0001']]

# Diccionario de elementos en F16
alphas = {'0000': 0, '0010': 1, '0100': 2, '1000': 3, '0011': 4, '0110': 5, '1100': 6, '1011': 7, '0101': 8,
          '1010': 9, '0111': 10, '1110': 11, '1111': 12, '1101': 13, '1001': 14, '0001': 15}

# Validar ficheros
while True:
    lectura = input("Escriba el nombre del fichero a codificar (con extension .txt): ")
    if(lectura[len(lectura)-4:] == '.txt'):
        break
    
while True:
    escritura = input("Escriba el nombre del fichero de escritura de la codificacion (con extension .txt): ")
    if(escritura[len(escritura)-4:] == '.txt'):
        break


cAscii = codingAscii(lectura)
codificacion = codificar(cAscii)
print("Operacion finalizada")
    
