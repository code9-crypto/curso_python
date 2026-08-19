#Exemplo simples
numeros = [1,2,3,4,5,6,7,8,9]
impares = [
    impar 
    for impar in numeros
    if impar % 2 != 0
]
print(impares)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)