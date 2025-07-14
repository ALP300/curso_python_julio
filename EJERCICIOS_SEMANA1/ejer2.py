'''
Determina el mayor de tres números: 
Declara tres variables a, b y c con 
valores numéricos y utiliza condicionales  
para determinar cuál de ellos es el mayor. 

ESTRUCTURA:

if a>b:
    print("a es mayor")
else:
    print("b es mayor" )

'''
a,b,c= 40,20,10

if a>=b and a>=c:
    resultado="a es mayor"
elif b>=a and b>=c:
    resultado="b es mayor"
else:
    resultado="c es mayor"

print(resultado)
