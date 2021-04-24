import bhaskara
import pytest

class Test_bhaskara:

    @pytest.fixture()
    def b(self):
        return bhaskara.Bhaskara()

    @pytest.mark.parametrize("entrada, saida",[
        ((1,0,0), (1,0)),
        ((1, -5, 6), (2, 3, 2)),
        ((10, 10, 10), 0),
        ((10, 20, 10), (1, -1))
    ])

    def teste_raiz(self, b, entrada, saida): 
        assert b.calcula_raizes(entrada[0], entrada[1], entrada[2]) == saida

 
"""     def test_uma_raiz(self, b):
        assert b.calcula_raizes(1, 0, 0) == (1, 0)
        
    def test_duas_raiz(self, b):
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)
       
    def test_zero_raiz(self, b):
        assert b.calcula_raizes(10, 10, 10) == 0
    
    def test_uma_raiz_negative(self, b):
        assert b.calcula_raizes(10, 20, 10) == (1, -1) """
