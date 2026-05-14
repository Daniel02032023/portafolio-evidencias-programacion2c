import unittest
from src.operaciones import suma, resta, multiplicacion, division, potencia
#python3 -m unittest tests.testOperaciones

class TestOperaciones(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)

    def test_resta(self):
        self.assertEqual(resta(5, 2), 3)
        self.assertEqual(resta(0, 4), -4)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 4), 12)
        self.assertEqual(multiplicacion(-2, 5), -10)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        with self.assertRaises(ValueError):
            division(5, 0)

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)
        
if __name__ == '__main__':
    unittest.main()