import os as windows #este biblioteca os é usada para que o python possa executar comandos do sistema operacional

plv_secreta = "escola"
ltr_acertadas = ""
tentativas = 0

while True:
    
    ltr_digi = input("Digite uma letra: ")
    tentativas += 1 

    if len(ltr_digi) > 1:
        print("Digite apenas uma letra")
        continue

    if ltr_digi in plv_secreta:
        ltr_acertadas += ltr_digi

    palavra_formada = ""
    for ltr_secre in plv_secreta:
        if ltr_secre in ltr_acertadas:
            palavra_formada += ltr_secre            
        else:
            palavra_formada += "*"
    
    print("Palavra formada: " + palavra_formada)

    if palavra_formada == plv_secreta:
        windows.system('cls') #o comando está sendo executado aqui
        print("VOCÊ GANHOU!! PARABÉNS")
        print("A palavra secreta era: " + plv_secreta)
        print("Número de tentativas foram: " + tentativas)
        break