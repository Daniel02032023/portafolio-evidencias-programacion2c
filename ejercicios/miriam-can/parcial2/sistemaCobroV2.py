"""
Sistema de cobro básico en Python
Este modulo permite realizar el calculo del subtotal, iva, descuento y total
de un producto aplicando los conceptos de modularidad.
"""
def calcular_iva(monto):
    """
    Devuelve el impuesto de la venta.
    
    Args:
        monto (float): Subtotal de la venta
    
    Returns:
        (float): Impuesto aplicado a la venta.
    """
    return monto * 0.16

def cacular_descuento(monto):
    """
    Devuelve el descuento aplicado a ventas mayores a $1000.
    
    Args:
        monto (float): Subtotal de la venta
        
    Returns:
        (float): Descuento aplicable a la venta.
    """
    if monto > 1000:
        return monto * 0.10
    return 0

def imprimir_ticket(prod, sub, desc, impuesto, total):
    """
    Imprime en pantalla el ticket de venta con la información detallada.
    
    Args:
        prod (str): Nombre del producto.
        sub (float): Subtotal de la venta.
        desc (float): Descuento aplicable a la venta.
        impuesto (float): Impuesto aplicado a la venta.
        total (float): Total final de la venta.
    """
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {prod}")
    print(f"Subtotal: ${sub:.2f}")
    print(f"Descuento: ${desc}")
    print(f"IVA: ${impuesto:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("-------------------------")
    
def main():
    """
    Funcion principal de inicia el programa.
    Procesa los datos de entrada y general los datos de salida.   
    """
    #PROGRAMA DE GESTION DE VENTAS (SIN MODULARIZACION)
    print("--- Sistema de Cobro v1.0 ---")

    opc = 0
    while(opc != 2):
        print("\n--- Menu de Opciones ---")
        print("1. Realizar venta | 2. Salir")
        opc = int(input("Selecciona una opción para continuar: "))
        if opc == 1:
            #Solicitar datos del producto al usuario
            producto = input("Nombre del producto: ")
            precio = float(input("Precio unitario: $"))
            cantidad = int(input("Cantidad: "))
            
            #Calcular subtotal
            subtotal = precio * cantidad
            
            #Calcular descuento
            descuento = cacular_descuento(subtotal)
            
            #Calcular iva
            impuesto = calcular_iva(subtotal)
            
            #Calcular total de venta
            total = (subtotal - descuento) + impuesto
            
            imprimir_ticket(producto, subtotal, descuento, impuesto, total)
            
        elif opc == 2:
            print("Programa terminado\n")
        else:
            print("Opción seleccionada no valida")
            
if __name__ == "__main__":
    main()