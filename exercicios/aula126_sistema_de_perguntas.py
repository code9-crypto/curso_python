#SISTEMA DE PERGUNTAS

certas = [] #respostas certas ficaram aqui
erradas = [] #respostas erradas ficaram aqui

#Aqui onde ficam as perguntas
perguntas = [
    {
        'Número':'1',
        'Pergunta':'Quanto é 2 * 2?',
        'Opções':['1','3','4','5'],
        'Resposta':'4'
    },
    {
        'Número':'2',
        'Pergunta':'Quanto é 8 * 2?',
        'Opções':['16','9','45','59'],
        'Resposta':'16'
    },
    {
        'Número':'3',
        'Pergunta':'Quanto é 10/2?',
        'Opções':['7','9','4','5'],
        'Resposta':'5'
    }
]

#função que irá converter o número em letra
def numeroParaLetra(numero):
    match numero:
        case 0:
            return 'a'
        case 1:
            return 'b'
        case 2:
            return 'c'
        case 3:
            return 'd'

#função que irá converter letra para número
def letraParaNumero(letra):
    match letra:
        case 'a':
            return 0
        case 'b':
            return 1
        case 'c':
            return 2
        case 'd':
            return 3

#Este for está percorrendo todos os dicionários dentro da lista
for indice in perguntas:
    print(indice['Pergunta']) #aqui está exibindo a pergunta de cada pergunta/dicionario
    
    #Este laço está sendo usado exclusivamente para percorrer itens da chave Opções e exibir as perguntas
    for ind, opcao in enumerate(indice['Opções']): #aqui está percorrendo os indices da lista de opções usando o método enumerate     
        opc = numeroParaLetra(ind)#aqui está recebendo a letra referente ao índice que vem da função numeroParaLetra()
        print(f"{opc}) {opcao}")#exibindo os indíces(em forma de letra) e as opções de cada pergunta/dicionario
    
    #aqui está fazendo a pergunta ao usuário e a variável irá armazenar a resposta
    #OBS.: como a opção escolhida é uma letra, então a função letraParaNumero() está convertendo a letra em número
    #a fim de conseguir pegar o valor a lista Opções
    try:
        resp = letraParaNumero(input("Escolha uma opção(letra): ")) #aqui a está sendo feito a pergunta e ao mesmo tempo sendo enviada como paramêtro ao função letraParaNumero()
        resp = indice['Opções'][resp] #aqui a mesma variável está pegando o valor da lista Opções mediante a escolher feita acima
    except TypeError:
        print("Opção escolhida inválida")
    
    #Verificando se a resposta está correta ou não
    if resp == indice['Resposta']:
        print("Acertou 👏")
        certas.append(indice['Número']) #se a resposta estiver correta, o número da pergunta será armazenada aqui
    else:
        print('Errou ❌')
        erradas.append(indice['Número']) #se a resposta estiver errada, o número da pergunta será armazenada aqui
        
    print()#pulando uma linha


#EXIBINDO O RELATÓRIO FINAL
    
#Verificando se a lista de certas é igual a 0
if len(certas) == 0:
    print('Não acertou nenhuma pergunta 😞')

#Verificando se acertou alguma pergunta
if len(certas) != 0:
    print("Questão(ões) certa(as): ", end="")
    for certa in certas:
        print(certa, end=" ")
    print()

#Verificando se errou alguma pergunta
if len(erradas) != 0:
    print("Questão(ões) errada(as): ", end="")
    for errada in erradas:
        print(errada, end=" ")
    print()
else:
    print("Você não errou nenhuma pergunta")