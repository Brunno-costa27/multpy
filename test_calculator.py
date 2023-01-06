
from unittest import TestCase

from calculator import invert, is_number, mul, soma, sum_


class CalculatorTest(TestCase):

    def test_mul(self):
        self.assertEqual(mul(2,3), 8) # 2 * 2 = 4 e 2 ** 2 = 4, por isso, temos que melhorar o teste.
        
class InvertTests(TestCase):
    def test_invert(self):
        self.assertEqual(invert(5), -5)
        
class SumTests(TestCase):
    def test_sum(self):
        self.assertEqual(sum_(1,2,3,4), 10)
        
class Is_numberTests(TestCase):
    def test_is_number(self):
        self.assertEqual(is_number(1), True)
        

class SomaTest(TestCase):
    def test_soma(self):
        self.assertEqual(soma(10, 10), 20)