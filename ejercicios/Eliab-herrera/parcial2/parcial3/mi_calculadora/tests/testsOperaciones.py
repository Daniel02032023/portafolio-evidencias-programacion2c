import unittest
from mi_calculadora.src import suma, resta, multi, division

class testOperaciones(unittest.TestCase):

    def test_suma_(self):
        self.assertEqual(suma(50,5),55)

    def test_resta_(self):
        self.assertEqual(resta(20,-2), 18)

    def test_multi_(self):
        self.assertEqual(multi(6,6), 36)

    def test_division_(self):
        self.assertEqual(division(50,2), 25)

if __name__ == "__main__":
    unittest.main     

