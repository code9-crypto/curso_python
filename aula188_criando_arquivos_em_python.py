# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

#Caso o caminho do arquivo seja em outra pasta, então deve ser escrito assim: C:\\pasta1\\pasta2....
caminho_arquivo = 'aula188.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

#O comando with faz a abertura e fechamento do arquivo, igual ao comando acima
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo: #OBS.: este "as arquivo" é semelhante ao atrelamento do comando acima
    arquivo.write("Atenção")
    arquivo.seek(0,0)
    print(arquivo.readline())
    print('Olá mundo')
    print('Arquivo vai ser fechado')    