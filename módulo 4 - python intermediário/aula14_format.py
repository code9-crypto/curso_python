#FAZENDO FORMATAÇÃO DE TEXTOS(STRING) COM O MÉTODO format()

a="A"
b="B"
c=1.1

#Para que a função acesse cada valor das variáveis e jogar dentro de uma string
#deve ser feito como está logo abaixo, usando chaves {}
#OBS.: aqui os valores estão sendo acessados por ordem de argumento
string = "a={} b={} c={}" 
print(string.format(
    a,b,c
    )
)

#É possível também passar os argumentos como parâmetros nomeados e ficará deste jeito
string2 = "a={parA} b={parB} c={parC}"
print(string2.format(
    parA = a,
    parB = b,
    parC = c
))

#É possível também acessar os valores de acordo com seu índice
#OBS.: para que seja possível acessar os valores pelo índice, os argumentos não podem ser nomeados
string3 = "a={0} b={1} c={2}"
print(string3.format(
    a,
    b,
    c
))
