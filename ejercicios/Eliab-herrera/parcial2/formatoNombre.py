def formato_nombre(name, lastName):
    """
    Devuelve el nombre de usuario en el formato Apellido, Nombre.

    Argumentos:
        name (str): Primer nombre del usuario.
        lastName (str): Apellido paterno del usuario.

    Rrtorno:
        (str): El nombre completo en formato Apellido, Nombre.    
    """
    return f"{lastName}, {name}"

# Funcion main para ejecutar del codigo.
def main():
    ()
    _name = input("introduce tu primer apellido")
    _lastName = input("introduce tu apellido materno: ")

    print(formato_nombre (_name, _lastName))

if __name__ == "__main__":
    main()
    
