# como getter
# p/ evitar quebrar código cliente
# p/ executar ações ao obter um atributo
# p/ habilitar setter
# métodos executa ações
#Atributos que começar com um ou dois underlines
#não devem ser usados fora da classe.

#Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self,cor):
        # private protected
        self._cor = cor
        self._cor_tampa = None
    
    @property
    def cor(self):
        print('PROPERTY')
        return self._cor
    
    @cor.setter #restringir determinadas funções
    def cor(self,valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self,valor):
        self._cor_tampa = valor
    
def mostrar(caneta):
    return caneta.cor
    
    
caneta = Caneta('Azul')
caneta.cor = 'Pink'

#getter -> é obter valor
print(caneta.cor)


