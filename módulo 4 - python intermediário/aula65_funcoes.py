#Definindo uma função em python
#def nomeFuncao():
#   ...
#IMPORTANTE:
#Parâmetros são "variáveis" dentro dos parênteses da função
#Argumentos são os valores dos respectivos parêmetros da função
#Ex.:

def imprimiSaudacao(nome, sobrenome):
    print(f"Boa tarde... {nome} {sobrenome}")

imprimiSaudacao("william","Caetano")

#Passando valor padrão ao parâmetro na construção das funções
def exibeNome(nome="Sem nome"):
    print(f"Olá, {nome}")

exibeNome("felpis")