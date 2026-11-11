# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:# Esta é super classe
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__) 

#Esta é a subclasse de Pessoa
class Cliente(Pessoa):# A herança é feita deste jeito
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


#Esta é a subclasse de Pessoa
class Aluno(Pessoa):# A herança é feita deste jeito
    cpf = 'cpf aluno'
    ...


c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()
print(a1.cpf)
# help(Cliente)
# IMPORTANTE
# Segundo o MRO (Method resolution order) há uma cadeia de resolução
# OBS.: esta ordem vai depender da cadeia de classes do seu código
# 1º Classe especializada
# 2º Classe genérica
# 3º Builtins.object