import Ordenadores
import Desempenho
import pytest

class Test_Ordenador:
    
    @pytest.fixture
    def o(self):
        return Ordenadores.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = Desempenho.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c = Desempenho.ContaTempos()
        return c.lista_aleatoria(100)
    
    def esta_ordenado(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i + 1]:
                return False
        return True

    def test_bolha_curta_aleatoria(self, o, l_aleat):
        o.improved_bubblesort(l_aleat)
        assert self.esta_ordenado(l_aleat)

    def test_selecao_direta_aleatoria(self, o, l_aleat):
        o.selecao_direta(l_aleat)
        assert self.esta_ordenado(l_aleat)

    def test_bolha_curta_quase(self, o, l_quase):
        o.improved_bubblesort(l_quase)
        assert self.esta_ordenado(l_quase)

    def test_selecao_direta_quase(self, o, l_quase):
        o.improved_bubblesort(l_quase)
        assert self.esta_ordenado(l_quase)