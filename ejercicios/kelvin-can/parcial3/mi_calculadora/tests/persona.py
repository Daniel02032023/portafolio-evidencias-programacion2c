"""
Crea una clase persona con las siguientes atributos : nombre, edad, genero y nacionalidad
 Agreaga un metodo para imprimir los datos de la persona y otro metodo para calcular el año
 de nacimiento de la persona.
 Crea un objeto de la clase persona y utiliza los metodos para mostrar su informacion y 
 calcula su año de nacimiento
 """

import datetime

class persona:
    
    def __init__(self, nombre, edad, genero, nacionalidad="Mexico"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Genero: {self.genero}")
        print(f"Nacionalidad: {self.nacionalidad}") 

    def calcular_año_nacimiento(self):
        año_actual = datetime.datetime.now().year
        año_nacimiento = año_actual - self.edad
        return año_nacimiento
    
    def main():
        persona1 = persona("Juan Perez", 30, "Masculino")
        persona1.imprimir_datos()
        año_nacimiento = persona1.calcular_año_nacimiento()
        print(f"Año de nacimiento: {año_nacimiento}")

    if __name__ == "__main__":
        main()
        