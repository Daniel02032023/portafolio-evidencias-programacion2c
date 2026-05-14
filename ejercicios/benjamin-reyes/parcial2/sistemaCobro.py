# SISTEMA DE COBRO v1.0

def capturar_datos():
    """
    Solicita al usuario los datos de un producto.

    Returns:
        tuple:
            nombre (str): Nombre del producto.
            precio (float): Precio unitario del producto.
            cantidad (int): Cantidad de productos.
    """
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    return nombre, precio, cantidad


def calcular_subtotal(precio, cantidad):
    """
    Calcula el subtotal de la compra.

    Args:
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad comprada.

    Returns:
        float: Resultado de multiplicar precio por cantidad.
    """
    return precio * cantidad


def aplicar_descuento(monto):
    """
    Aplica un descuento del 10% si el monto es mayor a 1000.

    Args:
        monto (float): Subtotal de la compra.

    Returns:
        float: Monto del descuento aplicado. Retorna 0 si no aplica.
    """
    if monto > 1000:
        descuento = monto * 0.10
        print(f"Se aplicó un descuento del 10%: -${descuento:.2f}")
        return descuento
    return 0


def calcular_iva(monto):
    """
    Calcula el IVA del 16% sobre un monto.

    Args:
        monto (float): Monto al que se le aplicará el IVA.

    Returns:
        float: IVA calculado.
    """
    return monto * 0.16


def mostrar_ticket(producto, subtotal, descuento, iva, total):
    """
    Muestra el resumen de la compra en formato de ticket.

    Args:
        producto (str): Nombre del producto.
        subtotal (float): Subtotal de la compra.
        descuento (float): Descuento aplicado.
        iva (float): IVA calculado.
        total (float): Total final a pagar.
    """
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: -${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("------------------------")


def main():
    """
    Función principal del programa.

    Flujo del sistema:
    1. Solicita los datos del producto al usuario.
    2. Calcula el subtotal.
    3. Aplica descuento si corresponde.
    4. Calcula el IVA sobre el subtotal con descuento.
    5. Calcula el total final.
    6. Muestra el ticket de compra.

    Returns:
        None
    """
    print("--- Sistema de Cobro v1.0 ---")

    # Captura de datos
    producto, precio, cantidad = capturar_datos()

    # Cálculos principales
    subtotal = calcular_subtotal(precio, cantidad)
    descuento = aplicar_descuento(subtotal)
    subtotal_con_desc = subtotal - descuento

    # Impuestos y total
    iva = calcular_iva(subtotal_con_desc)
    total_final = subtotal_con_desc + iva

    # Mostrar ticket
    mostrar_ticket(producto, subtotal, descuento, iva, total_final
# EJECUCIÓN DEL PROGRAMA

if __name__ == "__main__":
    main()
