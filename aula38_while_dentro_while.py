#ESTRUTURA DE REPETIÇÃO WHILE DENTRO DO WHILE

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:

    coluna = 1 #é necessário colocar essa variavel aqui dentro para que possa voltar a coluna 1
    while coluna <= qtd_colunas:
        print(f"{linha=} {coluna=}")
        coluna += 1
    
    linha += 1

print("Fim do programa")
    
    