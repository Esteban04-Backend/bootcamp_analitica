productos=[
    {'nombre':'manzana', 'categoria': 'fruta', 'valor': 500},
    {'nombre':'pan rollo', 'categoria': 'pan', 'valor': 600},
    {'nombre':'pera', 'categoria': 'fruta', 'valor': 200},
    {'nombre':'espinaca', 'categoria': 'verdura', 'valor': 500},
    {'nombre':'guineo', 'categoria': 'fruta', 'valor': 300},
    {'nombre':'zanahoria', 'categoria': 'verdura', 'valor': 500}
]
#agrupar productos por categoria
agrupados={}
for producto in productos:
    cat=producto['categoria']
    if cat not in agrupados:
        agrupados[cat]=[]
    agrupados[cat].append([producto['nombre'],producto ['valor']])#agregamos el valor del prodcto a nuestro archivo final, mediante un agrupamiento de datos
    agrupados[cat].append([producto['nombre']])
    agrupados[cat].append([producto['valor']]) #agregar datos pero sin agruparlos. 
print(agrupados)