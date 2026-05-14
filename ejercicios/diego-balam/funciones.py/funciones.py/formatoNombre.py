def formato_nombre(name, lastName):
 """
devuelve el nombre de usuario en foamato Apellido,Nombre

Argumentos:
  name(str):Primer nombre del usuario
  lastName(str): Apellido paterno del usuario

Retorn:
   (str): EL nombre completo en formato Apellido,Nombre.
"""
 return f"{lastName},{name}"

#funcion main para ejecucuion del codigo.
def main():
    _name = input("introduce el primer nombre: ")
    _lastName = input("introduce el primer apellido paterno: ")
    print(formato_nombre(_name,_lastName))
 
if__name__=="_main_":
main()
