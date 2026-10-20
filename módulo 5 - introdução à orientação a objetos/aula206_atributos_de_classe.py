# Atributos de classe
class Pessoa:
    ano_atual = 2022 #atributo da classe. Esta ficará disponível em todas as instâncias

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #Para acessar o atributo da classe é deste jeito


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

for p in vars(p1).items:
    print(p)