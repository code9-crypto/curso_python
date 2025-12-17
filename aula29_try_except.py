#INTRODUÇÃO AO TRY EXCEPT

numero = input("Digite um número: ")

try:
    print(f"O dobro do {numero} é {int(numero) * 2}")
except:
    print("O valor que você digitou não é um número")