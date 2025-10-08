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
filtro2=dataf.iloc[0:2]# otra forma de imprimir las dos primeras filas del data frame
print(filtro2)
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
#sort_values me realiza ordenamiento alfabetico como numerico
df_ordenado=dataf.sort_values(by='Producto') # ordena el data frame de forma ascendente
print('El data frame ordenado es: ')
print(df_ordenado)
df_ordenadod=dataf.sort_values(by='Producto', ascending=False)# ordena el data frame de forma descendente
print(df_ordenadod)
f_ordenadod=dataf.sort_values(by='Producto', key=lambda x: x.str.lower()) #convierte toda las palabras del producto en minusculas, las consultas adicionales siempre se separan con comas. 
print(f_ordenadod)


''' Solución del Docente
data2={'Producto':['Manzana', 'Banana', 'Cereza'],
       'Precio': [2.5,1.8,3.0],
       'Cantidad':[10,15,8]
       }
df=pd.DataFrame(data2)
print(df.iloc[0], df.iloc[1])
print(df.head[2])#para imprimir las primeras filas decididas por mi
print(df.tail[2])#imprimir las filas desde el final la cantidad de veces que necesite

df['P_total']=df.['Precio']*df['Cantidad']#agrega una nueva columna de en la fila
print('la nueva serie es: ')
print(df)
print(f'la suma total de los productos es: {df['P_total'].sum()}')'''