#Exercicio 1
print("1º Exercício", end="\n\n")
numero = input("Digite um numero inteiro: ")

try:
    #Tentando fazer a conversão valor recebido do usuário para inteiro e depois verificar se é par ou impar
    num_int = int(numero)    
    if num_int % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é impar")
except:
    #Se não for número inteiro, cairá nesta exceção
    print("Não é um número inteiro")

print(60 * "-")

#Exercício 2
print("2º Exercício", end="\n\n")
hora = input("Por favor, digite a hora: ")
hora_int = int(hora)

dia = hora_int >= 0 and hora_int <= 11
tarde = hora_int >= 12 and hora_int <= 17
noite = hora_int >= 18 and hora_int <= 23

if dia:
    print("Bom dia")
elif tarde:
    print("Boa tarde")
elif noite:
    print("Boa noite")
else:
    print("Este é um horário inválido")

print(60 * "-")

#Exercício 3
print("3º Exercício", end="\n\n")

nome = input("Digite o seu nome: ")

curto = len(nome) <= 4 and nome.isdigit() == False and nome != ""
normal = len(nome) >= 5 and len(nome) <= 6 and nome.isdigit() == False and nome != ""
grande = len(nome) > 6 and nome.isdigit() == False and nome != ""

if curto:
    print("Seu nome é curto")
elif normal:
    print("Seu nome é normal")
elif grande:
    print("Seu nome é muito grande")
elif nome.isdigit():
    print("Você digitou um número")
else:
    print("Este não um nome válido")