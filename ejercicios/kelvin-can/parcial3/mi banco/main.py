from banco import Banco
from cuenta import cuenta

banco = Banco()


def mostrar_menu():
    print("\n===== MENU DEL PROGRAMA MI BANCO =====")
    print("1. Aperturar nueva Cuenta")
    print("2. Ver Clientes")
    print("3. Depositar a Cuenta")
    print("4. Retirar de una Cuenta")
    print("5. Transferencia entre Cuentas")
    print("6. Buscar Cuenta")
    print("7. Eliminar una Cuenta")
    print("8. Salir del programa")


def main():

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        # 1. Crear cuenta
        if opcion == "1":
            numero = input("Número de cuenta: ")
            nombre = input("Nombre del cliente: ")
            saldo = float(input("Saldo inicial: "))

            cuenta = cuenta(numero, nombre, saldo)
            banco.agregar_cuenta(cuenta)

            print("Cuenta creada correctamente")

        # 2. Ver clientes
        elif opcion == "2":
            banco.ver_clientes()

        # 3. Depositar
        elif opcion == "3":
            numero = input("Número de cuenta: ")
            monto = float(input("Monto a depositar: "))

            banco.depositar(numero, monto)

        # 4. Retirar
        elif opcion == "4":
            numero = input("Número de cuenta: ")
            monto = float(input("Monto a retirar: "))

            banco.retirar(numero, monto)

        # 5. Transferencia
        elif opcion == "5":
            origen = input("Cuenta origen: ")
            destino = input("Cuenta destino: ")
            monto = float(input("Monto a transferir: "))

            banco.transferir(origen, destino, monto)

        # 6. Buscar cuenta
        elif opcion == "6":
            numero = input("Número de cuenta: ")

            cuenta = banco.buscar_cuenta(numero)

            if cuenta:
                print(cuenta)
            else:
                print("Cuenta no encontrada")

        # 7. Eliminar cuenta
        elif opcion == "7":
            numero = input("Número de cuenta a eliminar: ")

            banco.eliminar_cuenta(numero)

        # 8. Salir
        elif opcion == "8":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
