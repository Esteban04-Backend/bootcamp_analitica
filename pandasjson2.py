import pandas as pd

#Cargar archivo json
df=pd.read_json('data/json2.json')
print('data frame original')
print(df)

#seleccionar o dividir grupos por data frame separados para luego unirlos
df1=pd.json_normalize(df['grupo1']) #para versiones anteriores de python 3.13 usar el dataframe y el tolist, el resto se puede hacer con json normalizar
df2=pd.json_normalize(df['grupo2'])

print('datos1')
print(df1)
print('datos2')
print(df2)

#se unifica la data para que se muestre en un solo conjunto de datos
df_final=pd.concat([df1,df2],axis=0,ignore_index=True)
print(df_final)
#para validar que informacion de que fila se encuentra duplicada
print('Validacion data duplicada')
print(df_final.duplicated())
#para realizar una sumatoria de duplicados
print('total de datos duplicados')
print(df_final.duplicated().sum())

#verficar duplicados por columna se usa el subset=['Nombre columna']
print(df_final)
print(df_final.duplicated(subset=["Id"]))
#validar dos campos a la vez
print(df_final)
print(df_final.duplicated(subset=["Id",'Nombre']))

#siempre dejar el data frame original y crear versiones con las modificaciones
#dataframe sin duplicados
df_limpio=df_final.drop_duplicates(keep="last")#con keep=last elimina las primerass y amntiene las ultimas
print(df_final)
print("Dataset sin duplicados: ")
print(df_limpio)

#Suma edades
print(df_final)
#Convertir Texxto en Numero
df_final['Edad']=pd.to_numeric(df_final['Edad'], errors='raise')#utilizamos el errors course(coerencia) para no tomar el valor, como que le vale verga, y el raise es para saber en que linea es y uno puede mirar para corregir ese dato
print(f'Suma edades {df_final['Edad'].sum()}')

