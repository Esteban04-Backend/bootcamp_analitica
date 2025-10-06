'''def suma(a,b):#comenzamos definiendo def el nombre de la funcion y dentro del parentesis colocamos parametros y arbumentos
    sum=a+b #colocamos lo que va a hacer la funcion
    return sum # siempre nos va a retornar un valor, no es aconsejable que me retorne una funcion, es recomendabe que me retorne un valor.
print(suma(8,10))
print(suma(2,4))
print(suma(6,5))

def saluda(nom):
    return print(f'Hola Buenos Dias {nom}')

saluda('Miguel')
saluda('Juan')
saluda('Paola')

def cuadrado (n):
    return n**2

numero=cuadrado(2)
print(f'El resultado es: {numero}')

#Arreglo de datos con datos vacios, y lo complementamos con un set

#SIEMPRE DEFINIR LAS FUNCIONES DE PRIMREAS PARA PODER INVOCARLAS
def cambia (d,o):
    r=[]
    for i in d:
        if i is None:
            r.append(o)
        else:
            r.append(i)
    return r

datos=[1, None,2,None,3]
print(f'la funcion es cambia normal {cambia(datos,0)}')#datos lo toma como d y 0 lo toma como o. 

#funciones lambda son aquellas funciones que se ejecutan en una sola linea no necesita un return, los dos puntos se consideran el return 
suma2=lambda x,y: x+y
print(f'la suma de 4 + 1 es igual {suma2(4,1)}')

cambia2=lambda datos, p: [p if i is None else i for i in datos]

print(f'La funcion se llama cambia con lambda {cambia2(datos, 0)}')'''

#ejercicio
#el arreglo de 
numero=[10,8,45,26,7]
def ejemplo(numero):
    may=max(numero)
    mi=min(numero)
    su=sum(numero)
    orden=sorted(numero)
    return print(f'El mayor es {may}, el menor es {mi} y la suma es {su}, la lista ordenada es {orden}')

ejemplo(numero)

def ejem (n):
    return max(n),min(n),sum(n), sorted(n) 

numero_1=ejem(numero)
print(f'el resultado es {numero_1}')

