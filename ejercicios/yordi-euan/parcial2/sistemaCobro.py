# --- FUNCION 1: Pedir datos al usuario ---
def capturar_datos():
    """
    Solicita al usuario los datos del producto.

    Retorno:
        nombre (str): Nombre del producto.
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad de unidades.
    """
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    return nombre, precio, cantidad


# --- FUNCION 2: Calcular el subtotal ---
def calcular_subtotal(precio, cantidad):
    """
    Calcula el subtotal multiplicando el precio por la cantidad.
    """
    return precio * cantidad


# --- FUNCION 3: Aplicar descuento ---
def aplicar_descuento(monto):
    """
    Aplica un descuento del 10% si el monto es mayor a $1000.
    """
    if monto > 1000:
        descuento = monto * 0.10
        print(f"Se aplicó un descuento del 10%: -${descuento:.2f}")
        return descuento
    else:
        return 0


# --- FUNCION 4: Calcular IVA ---
def calcular_iva(monto):
    """
    Calcula el IVA del 16%.
    """
    return monto * 0.16


# --- FUNCION 5: Imprimir ticket ---
def mostrar_ticket(producto, sub, desc, iva, total):
    """
    Muestra el ticket de venta.
    """
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${sub:.2f}")
    print(f"Descuento: -${desc:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("------------------------")


# --- FUNCION PRINCIPAL ---
def main():
    print("--- Sistema de Cobro v1.0 ---")

    producto, precio, cantidad = capturar_datos()

    subtotal = calcular_subtotal(precio, cantidad)
    descuento = aplicar_descuento(subtotal)
    subtotal_con_desc = subtotal - descuento
    iva = calcular_iva(subtotal_con_desc)
    total_final = subtotal_con_desc + iva

    mostrar_ticket(producto, subtotal, descuento, iva, total_final)


# Ejecutar programa
main()