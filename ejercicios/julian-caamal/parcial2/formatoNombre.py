def formato_nombre(name, lastName):
    """
    Debuelbe el nombre de usuario en el fomato Apellido, Nombre.
    
    Argumentos:
        name (str): Primer nombre de usuario
        lasName (str): Apellido paterno del usuario.
        
    Retorno:
    (str): El nombre completo en formato Apellido, Nombre.
    """
    return f"{lastName}, {name}"

# Funcion main para ejecucion del codigo.
def main():
    _name = input ("introduce tu primer nombre: ")
    _lasName = input ("introduce tu apellido paterno: ")
    print(formato_nombre(_name,_lasName))
    
    if __name__=="__main__":
        main()
    