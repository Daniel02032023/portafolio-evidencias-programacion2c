def formato_nombre(name,lastname):
    """
    Devuelve el nombre de usuario en el formato Apellido, Nombre.
    
    Argumentos:
        name (str): Primer nombre del usuario.
        lastname (str): Apellido paterno del usuario
        
    Retorno:
        (str): El nombre completo en formato Apellido, Nombre.
    """    
    return f"{lastname},{name}"

#Funcion main para ejecución del código. 
def main():
    _name = input("Introduce tu primer nombre: ")
    _lastname = input("Introduce tu apellido paterno: ")
    print(formato_nombre(_name,_lastname))
    
if __name__ == "__main__":
    main()