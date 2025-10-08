import pandas as pd

#Cargar el archivo .csv

df=pd.read_csv("data/archivo.csv", sep=';')# dentro del parentesis siempre va la ubicacion y el nombre del archivo siempre en string
#para definir el separador usamos sep=
#Si no tenemos encabezado usamos la funcion header=None, ademas es un valor verdadero y falso
#usamos el names= para agregar encabezados a los archivos , names=['Producto','Precio','Cantidad']
#mostrar la data del csv
print(df)
print(df.head(2))
df['P_total']=df['Precio']*df['Cantidad']
print('La nueva serie es: ')
print(df)

#importar columnas especificas del csv los nombres deben de ser iguales a los encabezados
fr2=pd.read_csv("data/archivo.csv", usecols=['Producto','Precio'], sep=';')
print('Nuevo data frame solo con dos columnas')
print(fr2)

#Imprtar numero de filas que necesito
fr3=pd.read_csv("data/archivo.csv",sep=';', nrows=2, encoding='utf-8')#se reaiza especificacion del lenguaje para caracteres especiales
print('Nuevo data frame solo con dos filas')
print(fr3)

#exportar el archivo a csv
#df.to_csv('nuevo_archivo.csv', index=False)
#exportar el archivo a excel
df.to_excel('archivo_excel.xlsx', index=False)#libreria necesaria pip install openpyxl el index true me exporta directamente la indexacion