#Instalar Matplotlib
#pip install matplotlib o python -m pip install matplotlib
import matplotlib.pyplot as mplo
#Matploit
#Nos permite hacer graficas 
productos=['Manzanas','Peras','Naranjas']
ventas=[50,80,30]

mplo.bar(productos,ventas)# bar es la informacion donde este se va a alimentar con ejes x y y
mplo.title('Ventas por Producto') #agregar un titulo
mplo.xlabel('Productos')
mplo.ylabel('Ventas')#colocar titulo en el eje y
mplo.show() #.show es usado pafra ver la grafica