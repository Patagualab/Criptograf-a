'''
@author: Patricia Aguado Labrador
'''

# Suma dos elementos del cuerpo F16
def sumar (num1, num2):
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
    

# Diccionario de elementos en F16
alphas = {'0000': 0, '0010': 1, '0100': 2, '1000': 3, '0011': 4, '0110': 5, '1100': 6, '1011': 7, '0101': 8,
          '1010': 9, '0111': 10, '1110': 11, '1111': 12, '1101': 13, '1001': 14, '0001': 15}

# Seleciona entre sumar o multiplicar
operacion = int(input('Seleccione la operacion que quiera realizar:\n 0: sumar\n 1: multiplicar\n'))

if operacion == 0 or operacion == 1:
    
    # Obtencion de numeros como strings con los que se va a operar
    num1 = (input('Introduzca el primer numero (ejemplo: 0010): '))
    num2 = (input('Introduzca el segundo numero (ejemplo: 1100): '))
    
    if operacion == 0:
        print (sumar(num1, num2))
    
    else:
        print (multiplicar (num1, num2))
        
else:
    print('Eleccion incorrecta')




