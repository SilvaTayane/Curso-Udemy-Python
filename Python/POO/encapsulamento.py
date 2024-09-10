# Encapsulamento (modificadores de acesso: public, protected)
# Pyhton não tem modificadores de acesso
# Mas podemos seguir as seguintes convenções:
#  (sem underline) = public
#   pode ser usado em qualquer lugar
# _ (um underline) = protected
#    não DEVE ser usado fora da classe
#    ou suas subclasses.
# __ (dois underlines) = private
#   "name mangling" (desfiguração em nomes) em Python
#   só DEVE ser usado na classe em que foi declarado.

class Foo:
    def __init__(self):
        self.public = 'isso não é público'
        self._protected = 'isso é protegido'