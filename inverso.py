# Programa que dado un número y un módulo calcula el inverso de dicho número si lo tuviera
# Patricia Aguado Labrador

print ("Introduzca el numero porfavor")
num = int(input())
a = num

print ("Introduzca el modulo porfavor")
mod = int(input())
b = mod

r = [num,mod]
x = [1,0]
y = [0,1]


while True:
	i1 = len(r)-2
	i2 = len(r)-1

	q = r[i1]//r[i2]
	sig_r = r[i1]%r[i2]


	if sig_r == 0:
		mcd = r[i2]

		if mcd == 1:

			if 0 < x[i2] < mod:
				print ("El inverso de %d en modulo %d es %d" % (a, b, x[i2]))

			else:
				x[i2] = x[i2]+mod
				print ("El inverso de %d en modulo %d es %d" % (a, b, x[i2]))

		else:
			print ("%d no tiene inverso en modulo %d " % (a, b))

		break

	else:
		r.append(sig_r)
		x.append(x[i1]+(-q*x[i2]))
		y.append(y[i1]+(-q*y[i2]))