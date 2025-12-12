#INTRODUÇÃO A FSTRING
nome = "William"
sobrenome = "Caetano"
idade = 33
sexo = "masculino"
altura = 1.75

#A fstring permite fazer a interpolação de uma variável dentro de uma string
#usando os {}
#OBS.: para formatar números com casas decimais é {variavel:.2f} -> deste jeito vai mostrar duas casas decimais depois do ponto
texto = f"meu nome é {nome +' '+ sobrenome} eu tenho {idade} de idade e sou do sexo {sexo}, e a minha altura é {altura:.2f}"
print(texto)