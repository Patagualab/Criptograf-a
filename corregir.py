# -*- coding:utf-8 -*-
'''
@author: Patricia Aguado Labrador
Programa que corrige los posibles errores (uno por palabra) que haya en un fichero codificado
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

# Genera el sindrome de una palabra codificada multiplicando esta por la matriz de control traspuesta
def sindrome(vector):
    sindrome =[]
    suma ='0000'
    for cht in range(2):
        for cv in range(4):
            multi = multiplicar(vector[cv],ht[cv][cht])
            suma = sumar(suma,multi)
            
        sindrome.append(suma)
        suma='0000' 
    return sindrome

# Genera los vectores lideres de peso uno
def vectoresLideres(longitud):
    binarios = []
    for i in range(1,longitud): #numeros en binario del 1 al 15 en este caso
        binario = bin(i)[2:]
        if(i==1):
            binario = 3*'0'+binario
        if(i==2 or i==3):
            binario = 2*'0'+binario
        if(i>3 and i<8):
            binario= 1*'0'+binario
        binarios.append(binario)
        
    for i in binarios:
        vector = []
        v = i+'000000000000'
        n=0
        for _ in range(4):
            vector.append(v[n:n+4])
            n+=4
        sv = sindrome(vector)   # Calcula el sindrome de cada vector lider
        s = sv[0]+sv[1]
        vecSin[s]= v    # Anadir al diccionario de vectores y sindromes
    
    for i in binarios:
        vector = []
        v = '0000'+i+'00000000'
        n=0
        for _ in range(4):
            vector.append(v[n:n+4])
            n+=4
        sv = sindrome(vector)   # Calcula el sindrome de cada vector lider
        s = sv[0]+sv[1]
        vecSin[s]= v    # Anadir al diccionario de vectores y sindromes
    
    for i in binarios:
        vector = []
        v = '00000000'+i+'0000'
        n=0
        for _ in range(4):
            vector.append(v[n:n+4])
            n+=4
        sv = sindrome(vector)   # Calcula el sindrome de cada vector lider
        s = sv[0]+sv[1]
        vecSin[s]= v    # Anadir al diccionario de vectores y sindromes
    
    for i in binarios:
        vector = []
        v = '000000000000'+i
        n=0
        for _ in range(4):
            vector.append(v[n:n+4])
            n+=4
        sv = sindrome(vector)   # Calcula el sindrome de cada vector lider
        s = sv[0]+sv[1]
        vecSin[s]= v    # Anadir al diccionario de vectores y sindromes
        
# Corrige las palabras codificadas        
def corregir (vector):
    i=0
    f=4
    vecLista = []
    for _ in range (4): # Pasar el string de longitud 16 a una lista formada por bloques de 4
        vecLista.append(vector[i:f])
        i +=4
        f +=4
    sindromeVector = sindrome(vecLista)  # Calcular el sindrome de la palabra
    
    sindromeV =''
    vectorCorregido=''
    
    for i in sindromeVector:    # Pasar a string el sindrome
        sindromeV += i
    
    i=0
    f=4                         # Busco por clave si hay algun valor igual que el resultado obtenido
    for key in vecSin:          # Comparo los sindromes de las palabras del diccionario con el sindrome de la palabra codificada
        if key == sindromeV:    
            lider= vecSin[key]
            for _ in range(4):
                vectorCorregido += sumar(vector[i:f],lider[i:f])
                i +=4
                f +=4
            print('Se ha corregido un error')
            return vectorCorregido  # Devuelvo el vector que es la clave
        
        elif (key != sindromeVector and sindromeV == 8*'0'):
            return vector
        
        else:   # Si no se puede corregir el error se mete un asterisco
            asterisco = '0000000000101010'
            solucion = asterisco
            
    print('No se ha podido corregir el error')        
    return solucion

# Escribir en un fichero la correcion del texto
def corregirFichero(ficheroLec, ficheroEsc):
    f = open(ficheroLec, 'r+')
    fEsc=open(ficheroEsc, 'w')
    n=0
    
    while True: # Leer mientras haya contenido en el fichero
        bit = f.read(1)
        if not bit:
            break
        
        f.seek(n)
        letra = f.read(16)
        n += 16
        correccion = corregir(letra)
        
        fEsc.write(correccion)
        
    f.close()
    fEsc.close()
    
# Diccionario de elementos en F16
alphas = {'0000': 0, '0010': 1, '0100': 2, '1000': 3, '0011': 4, '0110': 5, '1100': 6, '1011': 7, '0101': 8,
          '1010': 9, '0111': 10, '1110': 11, '1111': 12, '1101': 13, '1001': 14, '0001': 15}

# Diccionario de vectores y sindromes
vecSin = {}

# Matriz de control traspuesta
ht= [['0001', '0001'],
     ['0001', '0011'],
     ['0001', '0111'],
     ['0001', '1111']]

# Validar ficheros
while True:
    lectura = input("Escriba el nombre del fichero a corregir (con extension .txt): ")
    if(lectura[len(lectura)-4:] == '.txt'):
        break
    
while True:
    escritura = input("Escriba el nombre del fichero de escritura de la correccion (con extension .txt): ")
    if(escritura[len(escritura)-4:] == '.txt'):
        break
    
    
vectoresLideres(16)
corregirFichero(lectura, escritura)
print("Operacion finalizada")
