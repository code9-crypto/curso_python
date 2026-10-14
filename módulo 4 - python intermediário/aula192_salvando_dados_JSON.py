import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula192.json', 'w', encoding='utf8') as arquivo:
    json.dump( #salvamos o dicionário em formato JSON num arquivo desta forma
        pessoa, #aqui vai o dicionário
        arquivo, #aqui a variável do caminho/arquivo
        ensure_ascii=False, #aqui evita que os dados salvos no arquivo não seja fique no formato ASCII
        indent=2, #por fim, os dados ficam totalmente identados no arquivo json
    )

with open('aula192.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo) #aqui pegamos o arquivo JSON e transformamos para dicionário
    # # print(pessoa)
    # # print(type(pessoa))
    # print(pessoa['nome'])
    for chave, valor in pessoa.items():
        if isinstance(valor, list):
            print(chave, "->", *valor)
        else:
            print(chave, "->", valor)
        