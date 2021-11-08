numero_inteiro = input ("Escreva o número inteiro: ")
numero_inteiro = int (numero_inteiro)

numero_taboada = print ("A tubuada do", numero_inteiro, "é:")

for i in range(1, 11):
    print(numero_inteiro, "X", i, "=", (numero_inteiro * i))