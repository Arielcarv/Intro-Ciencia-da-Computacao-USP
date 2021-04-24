def main():
    carro1 = Carro('brasília', 1968, 'amarela', 80)
    carro2 = Carro('fuscao', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, modelo, ano, cor, vmax):
        self.modelo = modelo
        self.ano    = ano
        self.cor    = cor
        self.velocidade = 0
        self.max_velocidade = vmax


    def imprima(self):
        if self.velocidade == 0:
            print(f"{self.modelo} {self.cor} {self.ano}")
        elif self.velocidade < self.max_velocidade:
            print(f"{self.modelo} {self.cor} indo a {self.velocidade}Km/h")
        else:
            print(f"{self.modelo} {self.cor} indo muito raaaaaapiiiiidooooo!")
    
    def acelere(self, v):
        self.velocidade = v
        if self.velocidade > self.max_velocidade:
            self.velocidade = self.max_velocidade
        self.imprima()

    def pare(self):
        self.velocidade = 0
        self.imprima()

main()



