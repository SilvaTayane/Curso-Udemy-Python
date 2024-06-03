# class  Classes são moldes para criar novos objetos
# Métodos em instâncias de classes Python
# Classe  - Molde (sem dados)
#Instâncias da class(objeto) - Tem os dados
# Uma classe pode gerar várias instâncias
#Na classe o self é a própria instância
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro()
fusca.acelerar()
Carro.acelerar(fusca)
