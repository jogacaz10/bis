import unittest
import math
from t_biseccion.biseccion import bi

class TestBiseccion(unittest.TestCase):

    def test_t1(self):
        def getFun(n):return math.exp(-n) - math.log(n)
        res=0.01
        Ni=100
        a=1
        b=1.5
        resultado=bi(Ni,a,b,res,getFun) 
        self.assertEqual(resultado[0], 1.3046875)
        self.assertEqual(resultado[1], 0.005988023952095809)
    def test_t2(self):
        def getFun(n):return n**2 - 4
        a = 0
        b = 3
        res = 0.01
        Ni = 100
        resultado = bi(Ni, a, b, res, getFun)
        self.assertEqual(resultado[0], 2.00390625)
        self.assertEqual(resultado[1], 0.005847953216374269)
