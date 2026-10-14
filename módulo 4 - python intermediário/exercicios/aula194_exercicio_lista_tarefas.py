# lista_tarefas = []
# lista_desfazer = []

# #Função que irá sempre exibir os itens da lista
# def exibe_itens_lista():
#     print("TAREFAS:")
    
#     for tarefa in lista_tarefas:
#         print(tarefa)

#     print()
#     print()


# #Iniciando aplicação
# while True:

#     #Exibindo os comandos ao usuário E pedindo-lhe para digitar a tarefa ou comando
#     print("Comandos: listar, desfazer, refazer")
#     user_value = input("Digite uma tarefa ou comando: ")    
#     user_value = user_value.lower().strip() #transformando o texto em minúsculo e sem espaços nas extremidades
    
#     print()

#     #Verificando se o valor foi um dos comandos exibidos
#     match(user_value):
#         case "listar":

#             exibe_itens_lista()

#         case "desfazer":

#             if len(lista_tarefas) == 0:
#                 print("Nada a desfazer", end="\n\n")
#                 exibe_itens_lista()

#             if len(lista_desfazer) == 0:
#                 print("Nada a desfazer", end="\n\n")
#                 exibe_itens_lista()

#             if len(lista_tarefas) != 0:
#                 item_desfeito = lista_tarefas.pop()
#                 lista_desfazer.append(item_desfeito)
#                 exibe_itens_lista()

#         case "refazer":
             
#             if len(lista_tarefas) == 0:
#                 print("Nada a refazer", end="\n\n")
#                 exibe_itens_lista()

#             if len(lista_desfazer) == 0:
#                 print("Nada a refazer", end="\n\n")
#                 exibe_itens_lista()

#             if len(lista_desfazer) != 0:
#                 item_refeito = lista_desfazer.pop()
#                 lista_tarefas.append(item_refeito)
#                 exibe_itens_lista()

#         case _: #Caso o valor não seja nenhum comando, então será adicionado na lista de tarefas
#             lista_tarefas.append(user_value)


#SOLUÇÃO DO PROFESSOR
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os, json

bancoJson = './exercicios/aula194_exercicio_lista_tarefa.json'

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)

    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'clear':
    #     os.system('clear')
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     continue