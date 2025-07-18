'''
LISTAS
'''
frutas= ["manzana","banana","naranja"]
numeros=[1,2,43,4,24]
mezcla= [1,"hola",4,5.345]

frutas[1]="pera"
frutas.insert(1,"Kiwi")
frutas.remove("naranja")
a= numeros[1:5]
b= numeros[:4]
c= numeros[4:]
d= numeros[-2:]
frutas.append("uva")
ultimo= frutas.pop()

print(a)
print(b)
print(frutas)
print(ultimo)
print(frutas)