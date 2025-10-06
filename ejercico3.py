import random;
listan=[]
par=[]
impar=[]
for n in range(15):
    gernum=random.randint(1,50)
    listan.append(gernum)
print(listan)
'''
for n in listan:
    if n%2 ==0:
        par.append(n)
    else:
        impar.append(n)
print(f'La lista de numeros pares es: {par}')
print(f'la lista de numeros impares es: {impar}')

if 32 in listan:
    print('El numero 32 se encuentra en la lista par')
else:
    print('El numero no se encuentra en la lista')'''

print(sum(listan))
print(max(listan))
print(min(listan))
prom=sum(listan)/len(listan)
print(round(prom,2))
print(listan[::-1])#reordenar la lista de atras a adelante (hacer un bucle en reversa ubicandose desde e ultimo al primero)
print(listan[-1])# imprime el ultimo numero
print(set(listan)) #elimina los numeros duplicados de la lista y los ordena de menor a mayor
numor=set(listan)
print(f'Numeros ordenados {sorted(numor)}')
print(f'ordenados 2 {sorted(listan)}')
