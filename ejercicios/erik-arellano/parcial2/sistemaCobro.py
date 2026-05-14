# Función para calcular el subtotal
def calcular_subtotal(precio, cantidad):
    """Calcula el subtotal multiplicando precio por cantidad"""
    return precio * cantidad


# Función para calcular el descuento
def calcular_descuento(subtotal):
    """Aplica un 10% de descuento si el subtotal es mayor a 1000"""
    if subtotal > 1000:
        return subtotal * 0.10
    return 0


# Función para calcular el IVA
def calcular_iva(subtotal_con_descuento):
    """Calcula el IVA del 16%"""
    return subtotal_con_descuento * 0.16


# Función para calcular el total final
def calcular_total(subtotal_con_descuento, iva):
    """Suma subtotal con descuento más IVA"""
    return subtotal_con_descuento + iva


# Función para imprimir el ticket
def imprimir_ticket(producto, subtotal, descuento, iva, total):
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: -${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("----------------------")


# Función principal
def main():
    print("--- Sistema de Cobro v1.0 ---")

    try:
        producto = input("Nombre del producto: ")
        precio = float(input("Precio unitario: "))
        cantidad = int(input("Cantidad: "))

        if precio < 0 or cantidad < 0:
            print("Error: precio y cantidad deben ser positivos.")
            return

        subtotal = calcular_subtotal(precio, cantidad)
        descuento = calcular_descuento(subtotal)
        subtotal_con_descuento = subtotal - descuento
        iva = calcular_iva(subtotal_con_descuento)
        total = calcular_total(subtotal_con_descuento, iva)

        imprimir_ticket(producto, subtotal, descuento, iva, total)

    except ValueError:
        print("Error: Debes ingresar valores numéricos válidos.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
