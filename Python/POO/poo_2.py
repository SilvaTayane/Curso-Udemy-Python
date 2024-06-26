# Atriputos de classe
# __dict__ e vars para atributos de instância 
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    
p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(p1.__dict__)