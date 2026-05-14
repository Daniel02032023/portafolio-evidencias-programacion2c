class perro:
    #Atributos de la clase perro
    especie = "Canis Lups Familiaris"
    #Constructor de la clase perro
    def __init__(self,nombre,raza = "caramelo", edad=0):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    #Metodo para imprimir los datos del perro
    def imprimirDatos(self):
        print("Nombre: ",self.nombre)
        print("Raza: ",self.raza)
        print("Edad: ",self.edad)
        print("Especie: ",self.especie)
def main():
     #Crear un objeto de la clase perro
    perro1 = perro("Firulais","Labrador", 5)
    perro1.imprimirDatos()
    perro2 = perro("Rex", "Pastor Aleman", 3) 
    perro2.imprimirDatos
    print("informacion del perro 2:",perro2.nombre,perro2.raza,perro2.edad)
    perro3 = perro("max", "Bulldog", 2)
    perro3.imprimirDatos()
    perro4 = perro("Dante",)
    perro4.edad = 4
    perro4.imprimirDatos()
    perro2.raza = "Pastor Belga"
    perro2.imprimirDatos()
    perro5 = perro("Raya", "siames", 1)
    perro5.especie = "Feliz catus"
    perro5.imprimirDatos()

    if __name__ == "__main__":
       main()