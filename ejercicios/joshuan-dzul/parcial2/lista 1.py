#joshuan david dzul cohuo
"""
Trabajas en la organización de un evento de premios.
Tienes una lista de celebridades que entrarán por la alfombra roja. El orden es vital!
1. Crea una lista llamada invitados con los nombres: "Robert Downey Jr.", "Emma Stone" y "Cillian Murphy".
2. Llegada de último minuto. Agrega a "Zendaya" al final de la lista.
3. Invitado VIP: "Steven Spielberg" acaba de llegar y debe ir al principio de la lista.
4. Cancelación: "Emma Stone" avisa que no asistir.
5. seguridad El último de la lista se porta mal y debe ser retirado.
6. Imprime la lista final y cuántos quedan en total.
"""
"""
SISTEMA DE GESTIÓN DE INVITADOS
Este script realiza operaciones básicas de manipulación de listas:
creación, inserción, eliminación y conteo.
"""

# punto no1: Inicialización de la lista con los primeros invitados
invitados = ["robert dawny jr", "emma stone", "cillian murphy"]

# punto no2: Agregar un elemento al final de la lista usando append()
# Zendaya entra en la última posición disponible.
invitados.append("zendaya")

# punto no3: Insertar un elemento en una posición específica usando insert(índice, valor)
# Agregamos a Steven Spielberg al inicio de la lista (índice 0).
invitados.insert(0, "steven spielberg")

# punto no4: Eliminar un elemento buscando por su nombre exacto usando remove()
# Se busca "emma stone" y se retira de la lista.
invitados.remove("emma stone")

# punto no5: Eliminar un elemento por su índice (posición) usando pop()
# El índice 3 corresponde al cuarto elemento de la lista actual.
invitados.pop(3)

# punto no6: Salida de datos
# Imprime la lista resultante y utiliza len() para mostrar la cantidad de elementos.
print(invitados, "no.total invitados: ", len(invitados))
