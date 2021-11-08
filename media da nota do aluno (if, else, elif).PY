#Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = int (input("Nota 1: "))
nota2 = int (input("Nota 2: "))
resultado = (nota1 + nota2)/2
print ("A média é: ", resultado)

if resultado == 10:
    print ("Aprovado com Distinção")
elif resultado >= 7 and resultado < 10:
    print ("Aprovado")
else:
    print ("Reprovado")
