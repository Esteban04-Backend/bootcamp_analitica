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