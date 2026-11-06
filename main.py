print("SISTEMA DE REGISTRO DE ESTUDIANTES")
print("1. Registrar estudiante")
print("2. Consultar estudiantes")
print("3. Calcular promedio")
print("4. Salir")

estudiantes = []
calificaciones = [85, 90, 95]

def registrar_estudiante(nombre):
  estudiantes.append(nombre)
  print("Estudiante registrado:", nombre)

def  consultar_estudiantes():
  print("ESTUDIANTES REGISTRADOS")
  for estudiante in estudiantes:
  print(estudiante)

def  calcular_promedio():
  prom = sum(calificaciones) / len(calificaciones)
 print(f"El promedio de calificaciones es: {prom:.2f}")


registrar_estudiante("Juan Pérez")
registrar_estudiante("María López")
consultar_estudiantes()
calcular_promedio()
