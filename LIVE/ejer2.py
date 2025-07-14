'''
Determina el rango de un número:
Declara una variable número con un valor 
numérico y utiliza condicionales para
determinar en qué rango se encuentra.
'''
numero=20
if numero<0:
    rango="El número es negativo"
elif 0<=numero<=10:
    rango="El número está entre 0 y 10"
elif 11<=numero<=20:
    rango="El número está entre 11 y 20"
else:
    rango="El número es mayor a 20"

print("El rango del número es: ", rango)
