notas = []
prom = 0.0

numeroNotas=int(input("Ingrese el numero de notas que ingresara: "))

print("Hola, como estas?, ingresa las notas en un rango del 0 al 5")

#rango donde pido las notas
for i in range(numeroNotas):
    
    nota=float(input(f"Ingrese la nota {i+1}: "))
    
    #Para cuando la nota esta fuera del rango
    while nota>5 or nota<0:
        print("La nota debe estar entre 0 y 5")
        nota=float(input(f"Ingrese la nota {i+1}: "))
        
    #Agrego a la lista de notas    
    notas.append(nota)
    
#sumo las notas    
for nota in range(numeroNotas):
    prom += notas[nota]

prom = prom/numeroNotas

#Valido aprobado o no
if prom >= 3 :
    print("Aprobado c:") 
else:
    print("Reprobado :c") 

print(f"Promedio: {round(prom,2)}")   
    

