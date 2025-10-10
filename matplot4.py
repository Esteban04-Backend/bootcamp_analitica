import matplotlib.pyplot as mplo

ingresos=[100,200,300,500,550]
gastos=[80,120,250,400,520]

mplo.scatter(gastos, ingresos, color='Chocolate')#me compara una variable respecto a  otra x vs y
mplo.title('Gastos VS Ingresos')
mplo.xlabel('Gastos')
mplo.ylabel('Ingresos')
mplo.show()