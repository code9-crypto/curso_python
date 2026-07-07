#MINHA SOLUÇÃO
print('MINHA SOLUÇÃO')
print("*" * 50)

numero = int(input('Digite um número para ser o multiplicador: '))
numero_multiplicador = [] #esta lista irá receber os multiplicadores
for x in range(2, numero+1): #aqui está inserindo os multiplicadores na lista a fim de multiplicar de forma dinâmica
    numero_multiplicador.append(x) #adicionando o número multiplicador à lista

numero_a_ser_multiplicado = input("Digite um número que será multiplicado: ")#recebendo do usuário o número a ser multiplicado
print()

#verificando se o que foi digitado é um número
if numero_a_ser_multiplicado.isdigit():
    try:
        numero_a_ser_multiplicado = int(numero_a_ser_multiplicado) #converte o valor recebido do usuário em inteiro
        
        #A lógica da multiplicação está acontecendo aqui
        def multiplicador(multiplicador):
            def multiplicado(multiplicado):
                return f"{multiplicador} * {multiplicado} = {multiplicador * multiplicado}"
            return multiplicado

    except:
        print("Não foi possível converter um dos valores em inteiro")
else:
    print("Um dos valores é inválido")

#percorrendo pela lista a fim de imprimir o resultado dos multiplicadores
for x in numero_multiplicador:
    funcs_multiplicacoes = multiplicador(x) #aqui instâncio a função com o parâmetro individual da lista
    print(funcs_multiplicacoes(numero_a_ser_multiplicado)) # aqui printa o resultado da multiplicação: dobro, tripo e quadruplo
print()
###################################################################################################################

print("SOLUÇÃO DO PROFESSOR")
print("*" * 50)
#SOLUÇÃO DO PROFESSOR
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))    