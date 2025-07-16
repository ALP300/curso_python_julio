
estudiante={
    "nombre":["Leonardo","Juan","Luis"],
    "edad": 21,
    "carrera": "Sistemas"
}
print(estudiante["nombre"])
estudiante["edad"]= 23
valor = estudiante["nombre"][1]
estudiante["semestre"]=5
valor= estudiante.get("direccion", "No especificado")
items= estudiante.items()
print(estudiante["semestre"])
print(estudiante["edad"])
claves= estudiante.keys()
edad= estudiante.pop("edad")
valores= estudiante.values()
estudiante.clear()
print(edad)
print(estudiante)
print(items)
print(valores)
print(claves)

universidad={
    "estudiante":{
        "001":{"nombre":"Ana", "edad":20},
        "002":{"nombre":"Leo", "edad":21}
    },
    "cursos":["Matemática","Historia"]
}