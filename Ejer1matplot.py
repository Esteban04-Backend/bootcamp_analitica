import matplotlib.pyplot as mplo

meses=['Enero','Febrero','Marzo','Abril']
ventas=[1500,1800,1200,2000]
gasto_publicitario=[500,700,400,800]

#Crear un Grafico de barras que muestre las ventas por cada mes
colores=['Red','Blue','Green','Yellow']
mplo.bar(meses,ventas,color=colores, edgecolor='black')#bar es para barras
mplo.title('Ventas Por Mes')
mplo.xlabel('Meses')
mplo.ylabel('Cantidad de Ventas')
mplo.show()

#Crear un grafico de lineas que muestre la tendencia de las ventas durante los meses
mplo.plot(meses, ventas, color='Blue',linewidth=3, marker='o', mec='black',mfc='black' )#plot es usado para grafico de lineas, mec color de borde del marker, mfc es el color total del marker
mplo.title('Tendencia de Ventas Por Mes')
mplo.xlabel('Meses')
mplo.ylabel('Cantidad de Ventas')
mplo.show()
#Crear un grafico de dispersion para analizar la relacion entre el gasto publicitario y las ventas
mplo.scatter(gasto_publicitario,ventas)#scatter es para dispersion
mplo.title('Gasto Publicitario Vs Ventas')
mplo.xlabel('Gasto Publicitario')
mplo.ylabel('Cantidad de Ventas')
mplo.show() #revisar este ejercicio con doble eje
