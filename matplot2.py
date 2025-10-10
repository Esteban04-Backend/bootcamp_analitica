import matplotlib.pyplot as mplo

meses=['Enero', 'Febrero','Marzo','Abril']
ventas=[120,150,110,200]

mplo.plot(meses,ventas, color="#A52091") #color=recibe colores en ingles y colores hexadecimales( estos colores comienzan con #E)
mplo.title('Evolución de Ventas')
mplo.xlabel('Meses')
mplo.ylabel('Ventas')
mplo.grid(True)#me realiza un borde
mplo.show()