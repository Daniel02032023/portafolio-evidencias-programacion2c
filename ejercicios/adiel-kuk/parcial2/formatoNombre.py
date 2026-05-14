def formato_nombre(name, lastName):
    """
    Devuelve el nombre del usuario en el formato Apellido, Nombre.

    Argumentos:
        name (str): Primer nombre del usuario.
        lastName (str): Apellido paterno del usuario.

    Retorno:
        (str): El nombre completo en formato Apellido, Nombre.ß
    """
    return f"{lastName}, {name}"

#Funcion main para ejecución del código.
def main():
    _name = input("Introduce tu primer nombre: ")
    _lastName = input("Introduce tu apellido paterno: ")
    print(formato_nombre(_name,_lastName))

if __name__ == "__main__":
    main()