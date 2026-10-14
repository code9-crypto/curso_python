import random #esta biblioteca ajuda a gerar números aleatórios
import sys #esta biblioteca permite sair do programa sem que continue o script

#CPF da pessoa
cpf = ""

#gerando um novo CPF
for i in range(11):#o for..in está iterando de 0 até 11
    cpf += str(random.randint(0, 9))#aqui está sendo gerado números aleatórios entre 0 e 9
print(f"CPF gerado foi este: {cpf}", end='\n\n')

#Recortando o CPF e formatando com a pontuação correta
cpf = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
print(f"CPF formatado: {cpf}", end='\n\n')

#CÁLCULO DO SEGUNDO DÍGITO
print("FAZENDO O CÁLCULO DO PRIMEIRO DÍGITO", end='\n')

#cpf separado pelo -
lista_cpf = cpf.split('-')
print(f"Divindo a string por meio de traço a fim de tirar o último digito: {lista_cpf}", end="\n\n")

#apagando item da lista
del lista_cpf[-1]
print(f"Apagando o último digito da lista: {lista_cpf}", end="\n\n")

#pegando apenas os valores junto com o ponto
cpf_com_ponto = lista_cpf[0]
print(f"Pegando o cpf ainda com ponto: {cpf_com_ponto}", end='\n\n')

#tirando os pontos entre os números
lista_cpf_sem_ponto = cpf_com_ponto.split('.')
print(f"Aqui foi separado o cpf com base no ponto e gerado uma lista: {lista_cpf_sem_ponto}", end='\n\n')

#juntando os números em uma string
cpf_sem_ponto = ''.join(lista_cpf_sem_ponto)
print(f"Feito a junção da lista de cpf sem ponto em uma string: {cpf_sem_ponto}", end='\n\n')

#fazendo a contagem regressiva
soma_cpf = 0
contador = len(cpf_sem_ponto) + 1 #aqui o resultado é 10, pois é 9 + 1
for n in cpf_sem_ponto: #Passando cada valor do cpf e multiplicando pelo contador(este começa em 10 e vai diminuindo)
    soma_cpf += int(n) * contador#fazendo a multiplicação e já aculumando a soma
    contador -= 1
print(f"Aqui foi feito a contagem dos números e chegou neste total: {soma_cpf}", end='\n\n')

#multiplicando o valor por 10
produto_soma_cpf = soma_cpf * 10
print(f"Feito a multiplicação do resultado anterior por 10: {produto_soma_cpf}", end='\n\n')


#Obtendo o resto da divisão do resultao anterior por 11
resto_produto = round(produto_soma_cpf % 11, 1)
print(f"O resto da divisão com arredondamento foi este: {resto_produto}", end='\n\n')

#Exibindo o primiro digito do CPF
condicao_digito = resto_produto if resto_produto <= 9 else 0
print(f"O primeiro digito é: {condicao_digito}", end='\n\n')

print(80 * "=")

#CÁLCULO DO SEGUNDO DÍGITO
print("FAZENDO O CÁCULO DO SEGUNDO DÍGITO", end='\n')

#aqui os números do cpf já estão unidos e o último digito será concatenado a este
cpf_com_mais_um_digito = cpf_sem_ponto + str(resto_produto)
print(f"CPF agora com o primeiro digito incluso: {cpf_com_mais_um_digito}", end='\n\n')


#fazendo a contagem regressiva
soma_seg_cpf = 0
contador = len(cpf_com_mais_um_digito) + 1
for n2 in cpf_com_mais_um_digito:
    soma_seg_cpf += int(n2) * contador
    contador -= 1
print(f"O resultado soma foi: {soma_seg_cpf}", end='\n\n')

#multiplicando o resulto por 10
produto_seg_cpf = soma_seg_cpf * 10
print(f"Resultado referente ao segundo digíto é: {produto_seg_cpf}", end='\n\n')

#Obtendo resto da divisão do segundo digíto
resto_seg_cpf = round(produto_seg_cpf % 11, 1)
print(f"O resto da divisão com arredondamento do segundo digíto foi: {resto_seg_cpf}", end='\n\n')

#Exibindo o segundo digíto
condicao_seg_digito = resto_seg_cpf if resto_seg_cpf <= 9 else 0
print(f"O segundo digíto é: {condicao_seg_digito}", end='\n\n')

print(80 * "=")
print("VERIFICANDO SE O CPF É REALMENTE VÁLIDO")

#último dois dígitos do CPF
ultimos_cpf_original = cpf.split('-').pop() #usando métodos encadeados
print(f"Digítos do cpf original: {ultimos_cpf_original}", end='\n\n')

#dígitos unidos por meio dos cálculos
ultimos_cpf_calculo = str(resto_produto) + str(resto_seg_cpf)
print(f"Digítos do CPF obtidos pelos cálculos: {ultimos_cpf_calculo}", end='\n\n')

#verificando se o CPF é válido ou não
if ultimos_cpf_original == ultimos_cpf_calculo:
    print("CPF é válido")
else:
    print("CPF é inválido")
