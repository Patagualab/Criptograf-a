# Programa que dados dos números te da como resultado su máximo común divisor y su identidad de Bezout
# Patricia Aguado Labrador

print ("Introduzca el primer numero porfavor")
dividendo = int(input())
a = dividendo

print ("Introduzca el segundo numero porfavor")
div = int(input())
b = div

r = [dividendo,div]
x = [1,0]
y = [0,1]

if dividendo == 0:
	print ("El mcd de %d y %d es %d" % (a, b, div))

elif div == 0:
	print ("El mcd de %d y %d es %d" % (a, b, dividendo))
	

while True:
	i1 = len(r)-2
	i2 = len(r)-1

	q = r[i1]//r[i2]
	sig_r = r[i1]%r[i2]


	if sig_r == 0:
		mcd = r[i2]
		if mcd < 0:
			mcd = -mcd
			x[i2] = -x[i2]
			y[i2] = -y[i2]

		print ("El mcd de %d y %d es %d" % (a, b, mcd))
		print ("Identidad de Bezout : %d = (%d) x (%d) + (%d) x (%d)" % (mcd, x[i2], dividendo, y[i2], div))
		break

	else:
		r.append(sig_r)
		x.append(x[i1]+(-q*x[i2]))
		y.append(y[i1]+(-q*y[i2]))