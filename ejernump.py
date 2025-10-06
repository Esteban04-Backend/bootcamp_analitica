import numpy

lista=[1,2,3]
arrai= numpy.array(lista) #convierte la lista en un arreglo
print(f'Lista {lista}')
print(f'arreglo {arrai}')
b=lista+arrai #suma de arreglos con los subindices 0 con 0 y 1 con 1 esto quiere decir que suma una lista y un arreglo
print(f'Combinar {b}')
array_lista=arrai.tolist()#to list convierte el arreglo en una lista
print(f'Convertir arreglo con to list {array_lista}')
union=array_lista+lista#concatena dos tipos de datos que sean iguales
print(f'union de las listas {union}')