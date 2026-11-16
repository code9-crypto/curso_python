# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MeuError(Exception):
    ...

errou = MeuError("Criei minha classe de erro")

print(errou)

#------------------------------------------------------

class NaoPodeSerNumero(Exception):
    ...

def recebeTexto(texto: str):
    if texto.isdecimal():
        # errou = NaoPodeSerNumero("Você digitou um número e não pode ser")
        # raise errou       OU
        raise NaoPodeSerNumero("Sistema não aceita número. Tente de novo")

#Este try..except está tratando o erro, por isso é exibido apenas a mensagem do erro
try:
    variavel = "123456"
    recebeTexto(variavel)
except NaoPodeSerNumero as erro:
    print(erro)