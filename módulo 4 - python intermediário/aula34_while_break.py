#ESTRUTURA DE REPETIÇÃO (while - enquanto, break)
condicao = True

while condicao: #ele vai executar ficar executando enquanto a condição for True. Caso contrário irá parar
    nome = input("Digite seu nome: ")
    if nome == "sair":
        print(f"Saindo do programa...")
        break
    
    print(f"Seu nome é: {nome}")