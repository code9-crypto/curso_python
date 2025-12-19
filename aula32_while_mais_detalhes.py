#ESTRUTURA WHILE(CONTINUAÇÃO)

tabuada = input("Digite um número para fazer a tabuada: ")
contador = 1

try:
    tabuada_int = int(tabuada)
    print(f"TABUADA DO {tabuada}")    
    while contador <= 10:
        print(f"{tabuada} * {contador} = {tabuada_int * contador}")
        contador += 1
except:
    print("Desculpe, valor inválido")