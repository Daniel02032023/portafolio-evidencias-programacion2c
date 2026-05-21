import unittest

from cuenta import cuenta
from banco import Banco

class TesttIntegracionBanco(unittest.TestCase):

    def setUp(self):
        self.cuenta1 = cuenta ("Fulanito Perez", "001", 1000)
        self.cuenta2 = cuenta("Perecilla Sanchez", "002")

        self.banco = Banco()

    def test_transfencia_exitosa(self):
        resultado = self.banco.transferir(self.cuenta1, self.cuenta2, 350)
        self.assertTrue(resultado, "Deberia realizarce de manera correcta la transferencia")
        self.assertEqual(self.cuenta1.saldo, 650, "El saldo de la cuenta 1 deberia ser 650")
        self.assertEqual(self.cuenta2.saldo, 350, "El saldo de la cuenta 2 destino deberia ser 350")

    def test_transferencia_saldo_insuficiente(self):
        resultado = self.banco.transferir(self.cuenta1, self.cuenta2, 1200)
        self.assertFalse(resultado, "La transferencia no se deberia realizar al no disponer del saldo suficiente")
        self.assertEqual(self.cuenta1.saldo, 1000, "El saldo deberia mantenerse sin cambios")
        self.assertEqual(self.cuenta2.saldo, 0, "El saldo de la cuenta 2 deberia ser 0")
