import pandas as pd

#leer archivo Json
df=pd.read_json("data/personas.json")
#imprimimos la data importada
print(df)

#Normalizacion de data
df_normalizado=pd.json_normalize(df['estudios'].tolist())#toca convertirlo en lista segun la version de pyton con tolist
print(df_normalizado)
#concatenacion por filas
df_final=pd.concat([df.drop(columns='estudios'),df_normalizado], axis=1)
print(df_final)