import unittest
from calculadoraBasica import suma, resta, multi, div

class testOperaciones(unittest.TestCase):

    def test_suma_positivos(self):
        self.assertEqual(suma(300,3),303)

    def test_suma_negativos(self):
        self.assertEqual(suma(-4,-6),-10)

    def test_suma_basica(self):
        self.assertEqual(resta(10,5), 5)

    def test_suma_negativa(self):
        self.assertEqual(resta(10,30), -20)

    def test_suma_valoresNegativos(self):
        self(self.assertEqual(-5,-5), 0)

if __name__ == "__main__":
    unittest.main   
