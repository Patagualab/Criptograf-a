# Programa que dada una lista de numeros te da como resultado su máximo común divisor y su identidad de Bezout
# Patricia Aguado Labrador

def mcd (a, b):

	dividendo = a
	div = b
	mcd = 0

	r = [dividendo,div]
	x = [1,0]
	y = [0,1]

	if dividendo == 0:
		return [div,0,0]
	

	elif div == 0:
		return [dividendo,0,0]
	

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
				return [mcd,x[i2],y[i2]]

			return [mcd,x[i2],y[i2]]
			break

		else:
			r.append(sig_r)
			x.append(x[i1]+(-q*x[i2]))
			y.append(y[i1]+(-q*y[i2]))


list = [int(x) for x in input("Escribe una lista de ńúmeros(Ejemplo:1 2 3 4 ): ").split()]
lx_bezout = []
ly_bezout = []



mcd1 = mcd (int(list[0]), int(list[1]))

i = 2
lx_bezout.append(mcd1[1])
ly_bezout.append(mcd1[2])
sig_mcd = int(mcd1[0])

while i<len(list):
	sig_mcd = mcd (sig_mcd, int(list[i]))
	i+=1

	lx_bezout.append(sig_mcd[1])
	ly_bezout.append(sig_mcd[2])
	sig_mcd = sig_mcd[0]

print ("El mcd es %d" % sig_mcd)

cont = len(lx_bezout)-2

for i in range(cont+1):
	lx_bezout[cont-i] = lx_bezout[cont-i]*lx_bezout[cont-i+1]
	ly_bezout[cont-i] = ly_bezout[cont-i]*lx_bezout[cont-i+1]

print ("La identidad de bezout para los números dados es la siguiente: ")

print (sig_mcd,"=(",lx_bezout[0],") x (",list[0],")", end="")
j = 1
for i in range(len(ly_bezout)):
	print ("+(",ly_bezout[i],") x (",list[j],")", end="")
	j +=1