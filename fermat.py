# Programa que realiza el pequeño teorema de fermat
# Patricia Aguado Labrador

print ("Introduzca la base porfavor")
base = int(input())
a = base

print ("Introduzca la exponente porfavor")
exponente = int(input())
p = exponente

print ("Introduzca el modulo porfavor")
modulo = int(input())
mod = modulo

def es_primo(numero):

    for i in range(2,numero):
        if (numero%i)==0:
            return False

    return True


if es_primo (modulo) == True:

	base_red = base%modulo
	exp_red = exponente%(modulo-1)

	num = 1

	for i in range(exp_red):

		num = num*(base%modulo)

		if num > modulo:
			num = num%modulo


	print ("El resultado es:",num)

else:
	print ("El exponente no es un numero primo")