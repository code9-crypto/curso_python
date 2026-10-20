import json

#Recuperando instancia no arquivo JSON
dados = './módulo 5 - introdução à orientação a objetos/exercicios/salvar classe em jSON/dados.json'

# #Abrindo json e recriando instancia

with open(dados, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = pessoas[0]
    p2 = pessoas[1]
    p3 = pessoas[2]


print(p1)
print(p2)
print(p3)