#Ler o nome de 2 time e o número de gols marcados na partida (para cada time).
#Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = (input("Escreva o nome do time 1: "))
time2 = (input("Escreva o nome do time 2: "))
gol_time1 = float(input("Escreva o placar do time 1: "))
gol_time2 = float(input("Escreva o placar do time 2: "))

if gol_time1 > gol_time2:
    print (" o vencedor é: ", time1)
if gol_time2 > gol_time1:
    print (" o vencedor é: ", time2)

if gol_time1 == gol_time2:
        print ("EMPATE")
