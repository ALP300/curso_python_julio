'''
13. Evaluación de estudiantes:
Dado un array de estudiantes (nombre, notas[]), calcula el promedio individual y
muestra los que aprobaron (promedio ≥ 11) y su 
mención (suficiente, bueno, excelente).
'''
def evaluar_estudiantes():
    estudiantes=[
        {"nombre":"Leo", "notas":[11,12,20,12]},
        {"nombre":"Gustavo", "notas":[18,13,20,17] }, 
        { "nombre":"Beckan", "notas":[17,14,20,12]}
    ]
    print("Resultados de la evalaución: ")
    for estudiante in estudiantes:
        promedio= sum(estudiante["notas"])/ len(estudiante["notas"])
        if promedio>=11:
            mensaje= "suficiente"
            if promedio>=16:
                mensaje="excelente"
            elif promedio>=14:
                mensaje="bueno"
            print(f"{estudiante["nombre"]:}: Aprobado: Promedio: {promedio}. Mención: {mensaje}")

evaluar_estudiantes()


