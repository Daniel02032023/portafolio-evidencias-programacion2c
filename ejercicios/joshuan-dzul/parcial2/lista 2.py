#joshuan david dzul cohuo
"""""
estas programando el sistema de una pequeña tienda debes manipular el inventario de productos disponibles
1.-Te ha llegado un camión con muevos productos"arroz","frijol","aceite".Agregalos todos a la lista usando un solo metodo.
2.-Te ha dedo cuenta que el "pan" esta vencido .Encuentra el indice del "pan" usando index()y lluegp eliminalo de la lista.
3.-
"""""
# Inicialización del inventario base
productos = ["leche", "pan", "huevos", "manzanas"]

# 1. Registro de nuevos suministros
# Usamos extend() para agregar múltiples elementos de una lista a otra en una sola operación
productos.extend(["arroz", "frijol", "aceite"])

# 2. Gestión de productos vencidos
# Localizamos la posición del "pan" y lo eliminamos usando pop()
# Nota: pop() extrae el elemento; si no necesitas el valor, podrías usar productos.remove("pan")
indice_vencido = productos.index("pan")
productos.pop(indice_vencido)

# 3. Organización del inventario
# Ordenamos la lista alfabéticamente para facilitar la búsqueda visual o reportes
productos.sort()

# Visualización del estado actual de la tienda
print("Inventario actualizado:", productos)

# Verificación de disponibilidad (Control de Stock)
if "leche" in productos:
    print("Estado: Contamos con leche en existencia.")
else:
    print("Estado: La leche no está disponible.")
