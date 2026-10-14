#EXERCICIO QUE MOSTRA QUAL LETRA MAIS REPETE NA FRASE
#usando o método count()

frase = "O python é uma linguagem de programação, multiparadigma. Python foi criado por Guido van Rossum"

frase_sem_espaco = frase.replace(" ","") #aqui retirei os espaços da frase com o método replace
i = 0
qtd_repetida_mais_vezes = 0
letra = ""

while i < len(frase_sem_espaco):    
    letra_atual = frase_sem_espaco[i]
    qtd_vezes_apareceu_atual = frase_sem_espaco.count(letra_atual)

    if qtd_repetida_mais_vezes < qtd_vezes_apareceu_atual:
        qtd_repetida_mais_vezes = qtd_vezes_apareceu_atual
        letra = letra_atual
    
    i += 1

print(f"A letra mais repetida foi a letra '{letra}' com '{qtd_repetida_mais_vezes}' vezes")