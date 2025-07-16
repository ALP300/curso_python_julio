frutas= ["manzana","banana","naranja"]
numeros=[1,2,3,4,5]
mezcla=[1,"hola",4.343]
frutas[1]="pera"
frutas.append("uva")
ordenada= sorted(frutas)
frutas.insert(1,"Kiwi")
frutas.remove("naranja")
ultimo= frutas.pop()
longitud= len(numeros)
sub_lista= numeros[1:5]
primeros= numeros[:3]
ultimos= numeros[-2:]
print(ultimos)
print(primeros)
print(ordenada)
print(longitud)
print(frutas[0])
print(mezcla[2])
print(sub_lista)
print(frutas)