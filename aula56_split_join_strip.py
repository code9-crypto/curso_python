'''
split - divide uma string
join - une uma string
Há também:
rstrip(retira os espaços apenas do lado direito da string)
lstrip(retira os espaços apenas do lado esquerdo da string)

'''

frase = "estou aprendendo python novamente com um professor que ensina bem direitinho"

#dividindo a string numa lista sem passar nenhum parâmetro no método split()
lista_frase = frase.split() #este método separa uma string e cria uma lista
print(type(lista_frase),'\n',lista_frase)

#dividindo a frase, mas agora com base numa vírgula
print()
frase = "continuo, aprendendo, python, bem, em, detalhes, estou, gostando, muito"
lista_frase_com_virgula = frase.split(', ')
print(lista_frase_com_virgula)

#comando que retira espaços do lado direito e do lado da string
print()
frase ="      tem muito espaços nas extremidades      "
frase_sem_espaco = frase.strip()
print(f"Frase com espaços: {frase}\nFrase sem espaços: {frase_sem_espaco}")

#unindo uma string com o método join
#OBS.: para que o método join() funcione, ele deve receber sempre um iterável(str, lista, tuplas e range)
print()
#o método join() começa deste jeito e ali entre as aspas simples é onde será definido o separador da frase
palavras_unidas = ' '.join(lista_frase_com_virgula)
print(palavras_unidas)