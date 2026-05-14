"""
Sistema de cobro básico en Python
Este modulo permite realizar el calculo del subtotal, iva, descuento y total
de un producto aplicando los conceptos de modularidad.
"""
#PROGRAMA DE GESTION DE VENTAS (SIN MODULARIZACION)
print("--- Sistema de Cobro v1.0 ---")

opc = 0
while(opc != 2):
    print("\n--- Menu de Opciones ---")
    print("1. Realizar venta | 2. Salir")
    opc = input("Selecciona una opción para continuar: ")
    if opc == 1:
        producto = input("Nombre del producto: ")
        precio = float(input("Precio unitario: $"))
        cantidad = int(input("Cantidad: "))

        #Cálculo del subtotal
        subtotal =precio * cantidad

        #Aplicar descuento si la compra es mayor a 1000
        if subtotal > 1000:
            descuento = subtotal * 0.10
            print(f"Se aplicó un descuento del 10%: -{descuento}")
        else:
            descuento = 0
            
        subtotal_con_descuento = subtotal - descuento

        #Calculo del IVA(16%)
        iva = subtotal_con_descuento * 0.16
        total_final = subtotal_con_descuento + iva

        #Impresión del ticket
        print("\n--- TICKET DE VENTA ---")
        print(f"Producto: {producto}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"IVA: ${iva:.2}")
        print(f"TOTAL A PAGAR: ${total_final:.2f}")
        print("-------------------------")
    elif opc == 2:
        print("Programa terminado\n")