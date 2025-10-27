'''#6. Serie Fibonacci: Crea un programa que calcule y visualice los elementos de la serie de Fibonacci. Esta serie se define de la siguiente manera:
#Fibonacci(0) = 0 
#Fibonacci(1) = 1 
#Fibonacci( n) = Fibonacci(n-1) + Fibonacci(n-2) 
#El usuario tan sólo introducirá el número de elementos que quiere visualizar.

fibonacci_series = [0,1]
n=int(input('Ingrese la cantidad:'))
for i in range(n-2):
    a=fibonacci_series[i]+fibonacci_series[i+1]
    fibonacci_series.append(a)
print(fibonacci_series)'''
#Inversión: Escribir un programa que pregunte al usuario una cantidad 
#a invertir, el interés anual y el número de años, y muestre por 
#pantalla el capital obtenido en la inversión cada año que dura la inversión.
u=float(input('Ingrese la cantidad a invertir: '))
iv=((float(input('Ingrese el interés anual (%): ')))/100)
a=int(input('Ingrese el número de años:'))
ca=u
for i in range(a):
    ca=round(ca*(1+iv),2)
    print(f'Año {i+1}: Capital acumulado = {ca}')
#print(f'La inversion para los {a} años es {inv}')