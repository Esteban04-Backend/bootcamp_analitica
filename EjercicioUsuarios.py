import pandas as pd

df=pd.read_csv("data/Usuarios.csv", nrows=5, usecols=['Nombres','Apellidos','Año_Nacimiento'])
print(df)
df['Edad']=2025-df['Año_Nacimiento']
print(df)
#defino columnas a seleccionar
fr3=['Nombres','Apellidos','Edad']
#creo la nueva serie con las columnas seleccionadas
fr4=df[fr3]
print(fr4)
#importar el archivo en excel
df.to_excel('usuarios.xlsx', index=False)
print('Se creo el archivo Excel Correctamente')