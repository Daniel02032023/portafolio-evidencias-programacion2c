def formato_nombre(name, lastName):
    """
    Debuelve el nombrede usuario en el formato Apellido, Nombre

    Argumentos:
        name (str): Primer nombre de usuario.
        astName (str): Apellido paterno del usuario.
     
    Retorno:
       (str): El nombre completo en formato Apellido, Nombre.
    """
    return f"{lastName}, {name}"

#funcion main para ejecución del código.
def main():
    _name = input("introduce tu primer nombre: ")
    _lastName = input("introduce tu apellido paterno: ")
    print(formato_nombre(_name,_lastName))
    
if __name__== "__main__":
 main()
    