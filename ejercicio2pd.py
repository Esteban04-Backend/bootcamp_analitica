#Ejercicio 2 Tarea
import pandas as pd

'''serie=pd.Series([10,20,30], index=['A','B','C'])
print(serie)'''

data1={'Producto':['Manzana', 'Banana', 'Cereza'],
       'Precio': [2.5,1.8,3.0],
       'Cantidad':[10,15,8]
       }
acumulador=0
dataf=pd.DataFrame(data1)#Convierto el diccionario en un dataframe
print(dataf)#imprimo el dataframe
filtro=dataf[dataf['Cantidad']>=10]#realizo un filtro el cual me muestra las dos primeras filas
print(filtro)
print(f' es la columna precio {dataf['Precio']}')#accedo a la columna precio
total=(dataf['Precio'])*(dataf['Cantidad'])#multiplico la columa precio con la cantidad para obtener el precio total
print(f'el total de el precio total es {total}')
suma=total.sum()#hace la sumatoria de todo el precio total
print(suma)#se imprime la suma
dataf['Precio Total']=total#agrego una nueva columna con el precio total 
print(dataf)
dataf['Total Factura']=suma
print(dataf)