#EXERCÍCIO MULTIPLICADOR

print("EXERCÍCIO 1 - TOTAL DA MULTIPLICAÇÃO")
#pedindo ao usuário inserir valores
def usuario():    
    valores = [] # os valores serão acumalados aqui dentro para depois serem passados à função
    while True:
        num = input("Digite um número: ")
        try:
            num = int(num)
            valores.append(num)
        except:
            print("Houve um erro")
        
        #perguntando se o usuário quer continuar ou parar
        resp = input("1(Continuar) ou 0(Sair): ")        
        if resp == "0" or resp == 0:
            break
        else:            
            continue
    
    return valores


#função que recebe os valores ilimitadamente
def mult(*nums):
    total = 1
    for n in nums:
        total *= n
    return total


#CHAMANDO A FUNÇÃO QUE PEDE OS NUMÉROS AO USUÁIO COMO PARÂMETRO PARA FUNÇÃO DE MULTIPILCAÇÃO

#apresentando valores multiplicados
totalMult = mult(*usuario())
print()
print(f"O produto é {totalMult}")

################################################################################
print(50 * "-")
################################################################################

print("EXERCÍCIO 2 - VERIFICAR SE PAR OU ÍMPAR")

results = [] #aqui ficaram os número junto com suas classifcações
cont = 0 #este será o índice de cada iteração
while True:
    results.append([])
    perg = input("Digite um número qualquer: ")
    try:
        resp = int(perg)        
        if resp % 2 == 0:
            results[cont] = f"{resp} -> par"
        else:
            results[cont] = f"{resp} -> impar"
        
        rp = input("1(Continuar) ou 0(Sair): ")
        if rp == "0" or rp == 0:
            break
        else:
            cont += 1
            continue           

    except:
        print("Valor inválido")

for nums, classes in enumerate(results):
    print(classes)