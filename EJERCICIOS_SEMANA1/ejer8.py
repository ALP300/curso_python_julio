'''
13. Evaluación de estudiantes:
Dado un array de estudiantes (nombre, notas[]), 
calcula el promedio individual y
muestra los que aprobaron (promedio ≥ 11) y su 
mención (suficiente, bueno, excelente).
'''

def evaluar_estudiantes():
    estudiantes=[
        {"nombre": "Leo", "notas":[16,14,17,13]},
        {"nombre": "Nicolás", "notas":[17,12,16,13]},
        {"nombre": "Ramon","notas":[12,15,16,17]},
        {"nombre": "Juan","notas":[14,17,12,13]},
    ]
    print("Resultados de la evaluación")
    for estudiante in estudiantes:
        promedio= sum(estudiante["notas"])/len(estudiante["notas"])
        if promedio>=11:
            mensaje="Suficiente"
            if promedio>=16:
                mensaje="Excelente"
            elif promedio>=14:
                mensaje="Bueno"
            
            print(f"{estudiante["nombre"]}.APROBADO: Promedio: {promedio}.Mensaje {mensaje}")

evaluar_estudiantes()

