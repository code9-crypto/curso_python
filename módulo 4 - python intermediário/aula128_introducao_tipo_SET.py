# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

#IMPORTANTE -> O tipo SET trabalha com iteráveis como String, lista, tuplas e dicionarios

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio OU s1 = {}
s1 = {'Luiz', 1, 2, 3}  # com dados
s2 = {'Luiz', 1, 2, 4}  # com dados
print('valores dentro do set -> ', s1, end="\n\n")

print(s1 == s2)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis; -> listas, dicionarios, tuplas e até mesmos o set
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
print(f"Verificando um valor dentro do SET usando IN (3 in s1) -> {3 in s1}", end="\n\n")

print(f"Verificando um valor dentro do SET usando NOT IN (3 in s1) -> {3 not in s1}", end="\n\n")

print('Percorrendo os dados usando o laço FOR')
for numero in s1:
    print(numero)
print() #pulando uma linha

# Métodos úteis:
# add, update, clear, discard
s1.add('william') #quando adiciona um valor do tipo string, este valor não será tratado como iterável(letra por letra), mas sim como o texto completo
print('Adicionando valor no set com o método ADD -> ', s1, end="\n\n")

#s1.update('ester') #o update atualiza o set com um novo valor. Contudo, se passar o valor assim, então será tratado como iterável(letra por letra)
s1.update(('ester','hadassa')) #agora se passar deste jeito(como uma tupla - iteravel - e com a vírgula no final) então o texto não será tratado como iterável
print('Atualizando valor no set com o método UPDATE -> ', s1, end="\n\n")

# s1.clear() #limpa totalmente o set
# print('limpando o set com o método CLEAR -> ', s1)


s1.discard('william') #aqui o set está descartando o valor em si(já que esta estrutura não trabalha com índice)
print('Descartando o valor "william" no set com o método DISCARD -> ', s1, end="\n\n")

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
se1 = {1,2,3}
se2 = {2,3,4}

se3 = se1 | se2 #UNIÃO -> une todos os valores em um
print("União de dois sets -> ", se3, end='\n\n')

se3 = se1 & se2 #INTERSEÇÃO -> retorna apenas os valores presentes em ambos os sets
print("Interseção de dois sets -> ", se3, end='\n\n')

se3 = se1 - se2 #DIFERENÇA 1 -> retorna apenas os valores contidos exclusivamente no da esquerda
print("Diferença 1 de dois sets -> ", se3, end='\n\n')

se3 = se2 - se1 #DIFERENÇA 2 -> retorna apenas os valores contidos exclusivamente no da esquerda
print("Diferença 2 de dois sets -> ", se3, end='\n\n')

se3 = se1 ^ se2 #DIFERENÇA SIMÉTRICA -> retorna apenas os valores das extremidades, ou seja, contidos exclusivamente no da esquerda e direita
print('Diferença simétrica -> ', se3)