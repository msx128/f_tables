import pytest
from f_tables import A, B, Calculate 

class Test:
    def test_A_calculation(self):
        a = A()
        a.u = 0.68
        a.i = 0.066
        a.calculate()
        assert a.usi == 10.30
        assert a.r == 10.1
        assert a.teto == 0.9
    
    def test_B_calculation(self):
        b = B()
        b.u = 0.67
        b.i = 0.066
        b.calculate()
        assert b.usi == 10.15
        assert b.r == 10.2
        assert b.teto == 0.9
