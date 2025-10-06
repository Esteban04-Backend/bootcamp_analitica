def bruh():
    numero=int(input("escriba un numero: "))
    return numero

n=0
value=True

while value:
    try:
        n=bruh()
    except:
        print("escribe un numero gil c:")
    else:
        value=False   
        
if n >0:
    print("el numero es positivo")
elif n ==0:
    print("el numero es cero")
else:
    print("el numero es negativo")
    
