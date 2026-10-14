#WHILE + CONTINUE
#continue -> pula o valor que foi alcançado na condição
#OBS.: é usado junto com uma if...else
contador = 1

while contador < 20:
    contador += 1 #IMPORTANTE: este deverá sempre ser a primeira linha da repetição

    if contador == 10:
        continue

    
    print(contador)
    