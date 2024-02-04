#carlo Sosa 0901-22-1106

class estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def verificar(self):
      return self.calificacion >=60

nombre_estudiante = input("Ingrese el nombre del estudiante: ")
edad_estudiante = int(input("Ingrese la edad del estudiante: ")) #Int se usa para numero enteros
calificacion_estudiante = float(input("Ingrese la calificacion: ")) #float se usa para numeros con decimales

estudiante1 = estudiante(nombre_estudiante, edad_estudiante, calificacion_estudiante)

if estudiante1.verificar():
    print(f"{nombre_estudiante} ha aprobado")

else:
    print(f"{nombre_estudiante} no ha aprobado")




    