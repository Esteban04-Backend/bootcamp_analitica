a =["pera", 4, 3, 2.4]
print(a[0])

lista = [1,2,3]
lista.append(4) #ingresa un dato al final / [1,2,3,4]
print(lista)
lista.extend([5,6]) #agrega los datos de una lista / [1,2,3,4,5,6]
print(lista)
lista.insert(2,10) #Inserta un dato en la posicion dada / [1,2,10,3,4,5,6]
print(lista)
lista.remove(3) #elimina la primera aparicion del dato / [1,2,10,4,5,6]
print(lista)
elemento = lista.pop(1) #elimina el dato del index dato y retorna el dato / elemento = 2, [1,10,4,5,6]
print(elemento)
print(lista)
print(lista[::-1]) #Recorre la lista de atras para adelante pero no la edita
lista.reverse() #Invierte la lista
print(lista)

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]