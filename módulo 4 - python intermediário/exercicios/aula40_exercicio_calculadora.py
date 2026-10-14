#EXERCÍCIO CALCULADORA

print("C A L C U L A D O R A", end="\n\n")

while True:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    operacao = input("Escolha uma das operações: \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nopção: ")
    
    try:
        n1 = float(num1)
        n2 = float(num2)
        conta = int(operacao)
        if conta == 1:
            print(f"{n1} + {n2} = {n1 + n2}")
        elif conta == 2:
            print(f"{n1} - {n2} = {n1 - n2}")
        elif conta == 3:
            print(f"{n1} * {n2} = {n1 * n2}")
        elif conta == 4:
            print(f"{n1} / {n2} = {n1 / n2}")
        else:
            print("Operação inválida")
    except:
        print("Não foi possível calcular com esses números")
    
    resp = input("Deseja fazer outra operação ( S[sim], N[não] ): ").lower().startswith('n')
    if( resp is True):
        break

print()
print("Obrigado por usar nossa calculadora :)")
    
    


    
