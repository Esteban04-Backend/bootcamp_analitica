persona={
    'nombre':'Mauricio',
    'edad': 42,
    'ciudad':'chiquinquira'
}
print(persona)
print(persona['edad'])
persona['nombre']='Juanito'
print(persona)
persona['profesion']='Ingeniero'
print(persona)
print(persona.keys())#.keys me da todas las llaves y/o keys del diccionario
data2={
    'estrato':2,
    'eps':'Sanitas',
    'comidas':['pastas','mexicana'],
    'profesion':'carnicero',
    'direccion':{
        'calle': 'carrera',
        'numero':'75-26',
        'complemento':'apto 602'
    }
}
persona.update(data2)#para actualizar valores del diccionario
print(persona)
print(f'Nombre:{persona['nombre']} apartamento: {persona['direccion']['complemento']}') #para acceder a los objetos tipo diccionario
print(f'segunda comida {persona['comidas'][1]}') #para acceder datos tipo lista segun subindice