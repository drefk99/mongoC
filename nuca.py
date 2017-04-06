a=[]
a=input('Cadenas: ')
b=int(input('cantidad: '))
print('Tu cadena es:\n  ')

aux=0
auxb=b
time=1+int(len(a)/b)
for i in range(time): 
	print(a[aux:auxb])
	aux=auxb
	auxb=auxb+b

