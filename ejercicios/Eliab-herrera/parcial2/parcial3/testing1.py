def calcular(*arg):
    """Devuelve el valor de la media o promedio de un conjunto de datos numericos.

    Args:
        *args (int): un numero variable de argumentos que representan los datos numericos.
    Returns:
        (float): El valor de la media o promedio de los datos numericos.
"""
    return (sum(*arg)/len(*arg))
assert(calcular([3,4,5]) ==4.0)
assert(calcular([10,20,30]) == 20.0)
assert(calcular([3,4,5]) ==2.0)
