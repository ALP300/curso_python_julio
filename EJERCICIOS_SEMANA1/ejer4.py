'''
Suma condicional de múltiplos:
Pide un número N y suma solo los múltiplos de
3 o 5 hasta N. Muestra la suma y los
múltiplos encontrados.

'''
def suma_condicional():
    N= int(input("Ingresa el valor de N: "))
    suma=0
    multiplos=[]
    for i in range(1, N+1):
       if i%3==0 or i%5==0:
           multiplos.append(i)
           suma+=i
    return suma

print("La suma es: ", suma_condicional())