import unittest
from parcial2.calculadoraBasica import Suma, resta, multi, division

class testOperaciones(unittest.TestCase):

    def test_suma_positivos(self):
        self.assertEqual(Suma(300,3),303)

    def test_suma_negativos(self):
        self.assertEqual(Suma(-4,-6), -10)

    def test_resta_basica(self):
        self.assertEqual(resta(10,5), 5)

    def test_resta_negativos(self):
        self.assertEqual(resta(10,30), -20)

    def test_resta_valoresNegativos(self):
        self.assertEqual(resta(-5,-5), 0)

    if __name__ == '__main__':
        unittest.main()




