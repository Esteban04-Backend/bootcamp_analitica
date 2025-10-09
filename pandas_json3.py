import pandas as pd

#Leer el json
df=pd.read_json('data/data.json')
print('Data Frame Original')
print(df)

#filtro por fecha
df['fecha_Nac']=pd.to_datetime(df['fecha_Nac'], format=('%d/%m/%Y'))
df_filtrado=df[df['fecha_Nac'].between('2000-01-01', '2001-01-01')]
print('Nuevo data frame por filtrado por fecha')
print(df_filtrado)