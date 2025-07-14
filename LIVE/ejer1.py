'''
1. Determina el mayor de tres números:
Declara tres variables a, b y c con valores 
numéricos y utiliza condicionales
para determinar cuál de ellos es el mayor.
'''
a,b,c= 5,10,20
if a>=b and a>=c:
    mayor=a
elif b>=a and b>=c:
    mayor=b
else:
    mayor=c
print("El mayor número es: ", mayor)
    