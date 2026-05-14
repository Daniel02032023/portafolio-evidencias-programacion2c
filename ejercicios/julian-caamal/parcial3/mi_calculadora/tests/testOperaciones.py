import unittest
from mi_calculadora.src.operaciones import suma,resta,multi,div,poten

class TestOperaciones(unittest.TestCase):
    
    def test_suma_positivo (self):
        self.assertEqual(suma(300,3),303)
        
    def test_resta_positivo (self):
        self.assertEqual(resta(4,6), 2)
        
    def test_multi_positivo(self):
        self.assertEqual(multi(10,5), 50)
        
    def test_div_positivo(self):
        self.assertEqual(div(100,2), 50)
        
    def test_poten_positivo(self):
        self.assertEqual(poten(4,2),8)
        
if __name__ == '__main__':
    unittest.main()