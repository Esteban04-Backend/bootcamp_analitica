import matplotlib.pyplot as mplo

edades=[20,21,22,25,25,26,27,30,35,40,42]
mplo.hist(edades,bins=5, color='red',edgecolor='black')#bins me da el rango del salto de 5 en 5 en el eje x
mplo.title('Rango Edades')
mplo.xlabel('Edades  Rangos')
mplo.ylabel('Distribucion de Edades')
mplo.show()