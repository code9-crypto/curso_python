import json

#Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

#Instância da classe Pessoa
p1 = Pessoa('Ester',26,'Feminino')
p2 = Pessoa('William',34,'Masculino')
p3 = Pessoa('Hadassa',3,'Feminino')
bd = [vars(p1),vars(p2),vars(p3)]

#Banco de dados em JSON
banco_de_dados = './módulo 5 - introdução à orientação a objetos/exercicios/salvar classe em jSON/dados.json'

with open(banco_de_dados, 'w', encoding='utf8') as arquivo:
    json.dump(
        bd,
        arquivo,
        ensure_ascii=False,
        indent=2        
    )