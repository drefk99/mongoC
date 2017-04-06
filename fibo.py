a=int(input('Ingresa el numero de unos: '))
b=int(input('Ingresa el numero de iteraciones: '))

fibo=[]
x=0
y=1
aux=1

while aux<a:
	aux=x+y
	x=y
	y=aux

	

for i in range(b):
		
	print(aux)
	aux=x+y
	x=y
	y=aux

#print(fibo)
