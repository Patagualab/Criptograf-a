# -*- coding: utf-8 -*-
'''
Created on 28 nov. 2018
@author: Patricia Aguado Labrador
Programa para encriptar un texto.
'''
import sys

####################################################################################

def multiplicarCuerpo(num1, num2):
    
    v1 = cuerpo.get(num1)   # Obtengo el valor del primer numero
    v2 = cuerpo.get(num2)   # Obtengo el valor del segundo numero
    
    if (v1 == 0 or v2 == 0):
        resultado = 0
    else:    
        resultado = v1 + v2     # Sumo los valores por la multiplicacion en F16 es como la suma en Z15
    
    while (resultado > 15): # Hago modulo 15 si el resultado es mayor que 15
        resultado -= 15
    
    for key in cuerpo:      # Busco por clave si hay algun valor igual que el resultado obtenido
        if cuerpo[key] == resultado:
            return key

def multiMatsCuerpo(matriz,matrizBin):
    matRes = []
    
    for x in range(len(matriz)):
        matRes.append([])
        for _ in range(len(matrizBin[0])):
            matRes[x].append('0000') 
    for i in range(len(matriz)):
        for j in range(len(matrizBin[0])):
            for k in range(len(matriz[0])):
                if(k == 0):
                    matRes[i][j] = multiplicarCuerpo(matriz[i][k],matrizBin[k][j])
                else:
                    matRes[i][j] = sumar(matRes[i][j],multiplicarCuerpo(matriz[i][k],matrizBin[k][j]))
    if(len(matRes[0]) == 1):
        temp = []
        for i in range(len(matRes)):
            temp.append(matRes[i][0])
        matRes = temp
    return matRes


def determinanteCuerpo(matriz):
    if(len(matriz) == 2):
        return sumar(multiplicarCuerpo(matriz[0][0],matriz[1][1]),multiplicarCuerpo(matriz[0][1],matriz[1][0]))
    else:
        det = '0000'
        for i in range(len(matriz)):
            det = sumar(det,multiplicarCuerpo(matriz[i][len(matriz)-1],determinanteCuerpo(matrizInferior(matriz,i))))
        return det

    
def cadenaMatrizHexa (cadena):
    matriz = [['0','0','0','0'],
              ['0','0','0','0'],
              ['0','0','0','0'],
              ['0','0','0','0']]
    inicio = 0
    fin = 4
    i=0
    j=0
    for _ in range(0,4):
        for n in cadena[inicio:fin]:
            matriz[i][j]= n
            i+=1
        j+=1
        i=0
        inicio +=4
        fin +=4  
    return matriz

def cadenaMatrizCuerpo (cadena):
    matriz = [['0','0','0','0'],
              ['0','0','0','0'],
              ['0','0','0','0'],
              ['0','0','0','0']]
    inicio = 0
    fin = 4
    i=0
    j=0
    for _ in range(0,4):
        for n in cadena[inicio:fin]:
            matriz[i][j]= hexaBin[n]
            i+=1
        j+=1
        i=0
        inicio +=4
        fin +=4  
    return matriz


####################################################################################

# Suma dos elementos del cuerpo F16
def sumar(num1, num2):
    resultado =''
    
    for i in range(len(num1)): 
        if num1[i] == num2[i]:  # Compara cada cifra del primer numero con la del segundo
            resultado += '0'    # Si las cifras son iguales la suma XOR me dara 0
        else:
            resultado += '1'    # Si las cifras son distintas me dara 1
            
    return resultado


def multiplicarBin(num1,num2):
    if(num1 == num2):
        solucion = num1
    else:
        solucion = '0'
    return solucion


def multiMatVec(matriz, vector):
    vector = list(vector)
    matRes = []
    
    for x in range(len(matriz)):
        matRes.append([])
        for _ in range(len(vector[0])):
            matRes[x].append('0')
            
    for i in range(len(matriz)):
        for j in range(len(vector[0])):
            for k in range(len(matriz[0])):
                if(k == 0):
                    matRes[i][j] = multiplicarBin(matriz[i][k],vector[k][j])
                else:
                    matRes[i][j] = sumar(matRes[i][j],multiplicarBin(matriz[i][k],vector[k][j]))
    
    if(len(matRes[0]) == 1):
        temp = []
        for i in range(len(matRes)):
            temp.append(matRes[i][0])
        matRes = temp
    return matRes


def matrizInferior(matriz,fila):
    inferior = []
    for i in range(len(matriz)):
        if(i != fila):
            filaInferior = []
            for j in range(len(matriz[i]) - 1):
                filaInferior.append(matriz[i][j])
            inferior.append(filaInferior)
    return inferior


def determinanteBin(matriz):
    if(len(matriz) == 2):
        return sumar(multiplicarBin(matriz[0][0],matriz[1][1]),multiplicarBin(matriz[0][1],matriz[1][0]))
    else:
        det = '0'
        for i in range(len(matriz)):
            det = sumar(det,multiplicarBin(matriz[i][len(matriz)-1],determinanteBin(matrizInferior(matriz,i))))
        return det

   
def binario(letra):
    binario = bin(hexa[letra])[2:6]
    b = binario
    if (len(binario) != 4):
        c= 4-len(binario)
        b= c*'0'+binario
    return b


def cadenaMatriz (inicio, fin):
    matriz = [['0','0','0','0'],
              ['0','0','0','0'],
              ['0','0','0','0'],
              ['0','0','0','0']]
    j=0
    for n in clave[inicio:fin]:
        i=3
        b = bin(hexa[n])[2:6]
        if (len(b) != 4):
            c= 4-len(b)
            b= c*'0'+b
        for m in b:
            if m == '1':
                matriz[i][j]= '1'
            else:
                matriz[i][j]= '0'
            i-=1
        j+=1
        
    return matriz


####################################################################################

def encriptar (ficheroEntrada, ficheroSalida):
    f = open(ficheroEntrada, 'r+')
    texto = f.read()
    f.close()
    
    if (len(texto)%16 != 0):
        print('El fichero no es válido.')
        sys.exit()
        
    else:
        fr = open(ficheroEntrada, 'r+')
        fw = open(ficheroSalida, 'w')
        while True:
            bloque = fr.read(16)
            if not bloque:
                break
            
            fw.write(encriptarBloque(bloque))
        fr.close()
        fw.close()
        print('Fin')

def encriptarBloque (bloque):
    
    resultadoSubBytes = subBytes(bloque, 0)
    resultadoShiftRows = shiftRows(resultadoSubBytes)
    resultadoMixColumns = mixColumns(resultadoShiftRows,0)
    resultadoAppendKey = appendKey(resultadoMixColumns)
    
    resultadoSubBytes = subBytes(resultadoAppendKey, 1)
    resultadoShiftRows = shiftRows(resultadoSubBytes)
    resultadoMixColumns = mixColumns(resultadoShiftRows,1)

    return resultadoMixColumns
   
   
####################################################################################
   
def subBytes(bloque, ronda):
    resultado =''
    if (ronda == 0):
        for i in bloque:
            resultado += biyec0[i]
    else:
        for i in bloque:
            resultado += biyec1[i]
    
    return resultado


def shiftRows(bloque):
    m = [['0','0','0','0'],
         ['0','0','0','0'],
         ['0','0','0','0'],
         ['0','0','0','0']]
    matriz = cadenaMatrizHexa (bloque)
    for i in range (0,4):
        for j in range (0,4):
            m[i][j-i] = matriz[i][j]
            
    
    resultado = ''
    i=0
    j=0
    for _ in range(0,4):
        for _ in range(0,4):
            resultado = resultado + m[i][j]
            i+=1
        j+=1
        i=0
              
    return (resultado) 


def mixColumns(bloque,ronda):
    resultado = ''
    if(ronda==0):
        matriz = [[hexaBin[clave[12]],'0001',hexaBin[clave[10]],hexaBin[clave[11]]],
                  [hexaBin[clave[11]],hexaBin[clave[12]],'0001',hexaBin[clave[10]]],
                  [hexaBin[clave[10]],hexaBin[clave[11]],hexaBin[clave[12]],'0001'],
                  ['0001',hexaBin[clave[10]],hexaBin[clave[11]],hexaBin[clave[12]]]]
    else:
        matriz = [[hexaBin[clave[15]],'0001',hexaBin[clave[13]],hexaBin[clave[14]]],
                  [hexaBin[clave[14]],hexaBin[clave[15]],'0001',hexaBin[clave[13]]],
                  [hexaBin[clave[13]],hexaBin[clave[14]],hexaBin[clave[15]],'0001'],
                  ['0001',hexaBin[clave[13]],hexaBin[clave[14]],hexaBin[clave[15]]]]
        
    matrizBin = cadenaMatrizCuerpo(bloque)
    matrizRes = multiMatsCuerpo(matriz,matrizBin)

    for i in range(4):
        for j in range(4):
            resultado = resultado + binHexa[matrizRes[j][i]]

        
    return resultado

def appendKey(bloque):
    resultado = ''
    for i in range(len(bloque)):
        b = hexaBin[bloque[i]]
        k = hexaBin[clave[i]]
        
        suma = sumar(b,k)
        resultado = resultado + binHexa[suma]
    
    return resultado


####################################################################################
                   
def claveValida(clave):
    if (len(clave) != 16):
        print('La clave no es válida.')
        sys.exit()
    
    suma1 = '0001'
    for n in range(10,13):
        letra = clave[n]
        b = binario(letra)
        suma1 = sumar(suma1,b)
    
    suma2 = '0001'
    for n in range(13,16):
        letra = clave[n]
        b = binario(letra)
        suma2 = sumar(suma2,b)
        
    if (suma1 != '0000' and suma2 != '0000'):
        matriz= cadenaMatriz (0, 4)
        
        if (determinanteBin(matriz) == '1'):
            matriz= cadenaMatriz (5, 9)
            
            if (determinanteBin(matriz) == '1'):
                return True
            else:
                return False
        else:
            return False

    else:
        return False


####################################################################################
    
def biyeccion0(cadena):
    matriz= cadenaMatriz (0, 4)
    s = binario(clave[4])
    resultado = []
    imagen = ''
    biy0 = ''
    
    for i in cadena:
        b = binario(i)
        v = multiMatVec(matriz,reversed(b))
        for i in range(0,4):
            resultado.append(sumar(v[i],s[3-i]))
        resultado = reversed(resultado)
        for n in resultado:
            imagen += n
        
        biy0 += binHexa[imagen]
        resultado = []
        imagen = ''
    return biy0

    
def biyeccion1(cadena):
    matriz= cadenaMatriz (5, 9)
    s = binario(clave[9])
    
    resultado = []
    imagen = ''
    biy1 = ''
    
    for i in cadena:
        b = binario(i)
        v = multiMatVec(matriz,reversed(b))
        for i in range(0,4):
            resultado.append(sumar(v[i],s[3-i]))
        resultado = reversed(resultado)
        for n in resultado:
            imagen += n
        
        biy1 += binHexa[imagen]
        resultado = []
        imagen = ''
        
    return biy1

####################################################################################    
    
hexa = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
       'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

cuerpo = {'0000':0, '0001':15, '0010':1, '0011':4, '0100':2, '0101':8, '0110':5,
        '0111':10, '1000':3, '1001':14, '1010':9, '1011':7, '1100':6, '1101':13,
        '1110':11, '1111':12}

hexaBin = {'0':'0000','1':'0001','2':'0010','3':'0011',
            '4':'0100','5':'0101','6':'0110','7':'0111',
            '8':'1000','9':'1001','a':'1010','b':'1011',
            'c':'1100','d':'1101','e':'1110','f':'1111'}

binHexa = {'0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6',
        '0111':'7', '1000':'8', '1001':'9', '1010':'a', '1011':'b', '1100':'c', '1101':'d',
        '1110':'e', '1111':'f'}



clave = str(input('Introduzca la clave: '))

if (claveValida(clave) == True):
    cadena = '0123456789abcdef' 
    biyec0 = dict(zip(cadena,biyeccion0(cadena)))
    biyec1 = dict(zip(cadena,biyeccion1(cadena)))
    
    # Validar ficheros
    while True:
        lectura = input("Escriba el nombre del fichero a encriptar (con extension .txt): ")
        if(lectura[len(lectura)-4:] == '.txt'):
            break
        
    while True:
        escritura = input("Escriba el nombre del fichero de escritura de la encriptación (con extension .txt): ")
        if(escritura[len(escritura)-4:] == '.txt'):
            break
    
    encriptar(lectura, escritura)

else:
    print('La clave no es válida.')
    sys.exit()
    
