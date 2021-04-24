
import Ordenadores
import random
import time


class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)] # inteiros entre 0 e 999
        return lista
    
    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara (self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        o = Ordenadores.Ordenador()

        print("\nListas Aleatórias")
        antes = time.time()
        o.bubblesort(lista1)
        depois = time.time()
        print("Bubblesort demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Seleção Direta demorou ", depois - antes)

        antes = time.time()
        o.improved_bubblesort(lista3)
        depois = time.time()
        print("Bubblesort melhorado demorou ", depois - antes)


        print("\nListas Quase Ordenadas")
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        
        antes = time.time()
        o.bubblesort(lista1)
        depois = time.time()
        print("Bubblesort demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Seleção Direta demorou ", depois - antes)

        antes = time.time()
        o.improved_bubblesort(lista3)
        depois = time.time()
        print("Bubblesort melhorado demorou ", depois - antes)


c = ContaTempos()
c.compara(1000)
