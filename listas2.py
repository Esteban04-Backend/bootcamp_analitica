import random;#importamos la libreria random al principio esto se hace con todas las librerias

frutas=['Pera','Uva','Manzana','Banano','Fresa']
print(frutas[0]) #accede al primer elemento de la lista
print(frutas[-1]) #acceder a la parte o ultimo elemento de mi lista con la posicion -1
print('__________________')
for elemento in frutas:
    print(elemento)#recorrer toda l lista elemento por elemento

print('__________________')
#del frutas[2] #vamos a eleminar manzana
print(frutas)
print('__________________')
if 'Manzana' in frutas:
    print('Manzana se encuentra en la lista')
else:
    print('Manzana No se encuentra en la lista')
print('__________________')
#Contar elemento de la lista
print(f'la lista de frutas contiene {len(frutas)} elementos')
#Contar elementos de la lista con un nombre menor a 5 letras
f_corta=[f for f in frutas if len(f)<=4] #forma 1

f_corta2=[] #Forma2 
for f in frutas:
    if len(f)<=4:
        f_corta2.append(f)
print(f_corta2)
''' F es la iteracion del recorrido que va a hacer por cada elemento 
de la lista frutas y hace el conteno de cada caracter que contiene cada fruta'''
print(f'La lista cuenta con {len(f_corta)} frutas con nombres cortos')
print(f'Las frutas con nombres cortos son: {f_corta}')

print('__________________')
n=random.randint(1,10)
print(f'El numero aleatorio es: {n}')


