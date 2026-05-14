def formato_nombre(name, lastName):
    """
    Devuelve el nombre de usuario en el formato Apellido, Nombre.

    Argumentos:
        name (str): Primer nombre del usuario.    
        lastaName (str): Apellido paterno del usuario.

    Retorno:
       (str): El nombre completo en formato Apellido, Nombre:
    """
    return f"{lastName}, {name}"

#Funcion main para ejecucion del codigo.
def main():
    _name = input("Introduce tu primer nombre: ")
    _lastName = input("introduce tu apellido paterno: ")
    print(formato_nombre(_name,_lastName))
    
if __name__== "__main__":
    main()
