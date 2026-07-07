"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

#A variável representa à segunda função e o valor que ela está recebendo é a primeira função
falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome)) #para atrelar o valor à segunda função é chamando a função por meio da variável
    print(falar_boa_noite(nome))
