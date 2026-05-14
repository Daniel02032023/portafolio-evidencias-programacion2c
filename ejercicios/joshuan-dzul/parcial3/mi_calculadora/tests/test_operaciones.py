import unittest
from mi_calculadora.src.operaciones import suma,resta,multiplicacion,divicion

class testOperaciones(unittest.TestCase):

    def test_suma_positivo (self):
        self.assertEqual(suma(30,30),60)

    def test_suma_negativo (self):
        self.assertEqual(suma(-9,-6),-15)

    def test_resta_basica (self):
        self.assertEqual (resta(15,5),10)

    def test_resta_negativa(self):
        self.assertEqual (resta(10,40),-30)

    def test_resta_valoresNegativos(self):
        self.assertEqual (resta(-5,-9),4)

if __name__ =='__main__':
    unittest.main()