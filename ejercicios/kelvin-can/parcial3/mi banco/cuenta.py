
class cuenta:
    # Atributos: cliente, cuenta, saldo
    """Inicializa una nueva instancia de la clase cuenta.

    Args:
        cliente (str): El nombre del dueño de la cuenta.
        cuenta (str): El número de cuenta bancaria.
        saldo (float): El saldo inicial de la cuenta.
    """
    def __init__(self, cliente, cuenta, saldo = 0):
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo

    def deposito(self, cantidad):
        """Una cantidad de dinero al saldo actual si la cantidad es positiva.
        Args:
            cantidad (float): Monto a depositar. 
        Returns:
            bool: True si el depósito fue exitoso, False en caso contrario.
        """
        if cantidad>0:
            self.saldo += cantidad  
            return True
        return False
   
    def retirar(self,cantidad):
        """Resta una cantidad de dinero al saldo actual si hay fondos suficientes.
        Args:
            cantidad (float): Monto a retirar.
        Returns:
            bool: True si el retiro se pudo realizar, False si hay saldo o es insuficiente.
        """
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False
    