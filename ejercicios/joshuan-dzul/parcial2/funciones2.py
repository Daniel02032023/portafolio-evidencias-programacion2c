# Definimos una variable global llamada 'puntos' con un valor inicial de 10
puntos = 10

def calcular_puntos(puntos, bono):
    """
    Suma un bono al valor de puntos actual.
    
    Argumentos:
    puntos (int): El valor base (parámetro local).
    bono (int): La cantidad a sumar.
    
    Retorna:
    int: La suma de puntos y bono.
    """
    # Se realiza la suma. 'puntos' aquí es una variable local 
    # que solo existe dentro de esta función.
    puntos = puntos + bono
    return puntos

# Llamamos a la función pasando la variable global 'puntos' (10) y el bono (5).
# El resultado devuelto (15) se asigna nuevamente a la variable global 'puntos'.
puntos = calcular_puntos(puntos, 5)

# Muestra el resultado final en la consola: 15
print(puntos)
