def formato_nombre(name,lasname):
    """
    devuelve el nombre de usuario en el formato Apellido,nobre.

    argumento:
        name (str): Primer nombre del usuario.
        lasname (str): Apellido paterno del usuario.

    retorno:
        (str): El nombre completo en formato Apellido, Nombre.
    """
    return f"{lasname},{name}"

#funcion main para ejecutar del codigo.

def main():
    ()
    _name= input("Introduce tu primer nombre: ")
    _lasname= input("Introduce tu apellidopaterno: ")

    print(formato_nombre(_name,_lasname))

if __name__ == "__main__":
    main()