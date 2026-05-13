class cuenta:
    # Atributos: cliente, cuenta, saldo

    def __init__(self, cliente, cuenta, saldo = 0):
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo
        """Inicializa una nueva cuenta bancaria con el cliente, número de cuenta y saldo inicial.
        Args:
            cliente (str): El nombre del cliente.
            cuenta (str): El número de cuenta.
            saldo (float): El saldo inicial de la cuenta.POr efecto, el saldo inicial es 0.
        """
    #Metodo para realizar un deposito en la cuenta bancaria
    def deposito(self, cantidad):
        if cantidad>0:
            self.saldo += cantidad  
            return True
        return False
    """
    Realiza un depósito en la cuenta.
    Args:cantidad (float): La cantidad a depositar. Debe ser un valor positivo.
    Returns:True si el depósito fue exitoso, False si la cantidad es negativa o cero.

    """
    #Metodo para realizar un retiro en la cuenta bancaria
    def retirar(self,cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad 
            return True 
        return False
    """Realiza un retiro de la cuenta.
    Args:cantidad (float): La cantidad a retirar. Debe ser un valor positivo y no puede exceder el saldo disponible.
    Returns:True si el retiro fue exitoso, False si la cantidad es negativa, cero o mayor que el saldo disponible.
    """
    
    def main():
        pass

    if __name__ == '__main__':
        main()