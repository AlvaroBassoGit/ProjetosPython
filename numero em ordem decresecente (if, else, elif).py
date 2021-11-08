#Faça um Programa que leia três números e mostre-os em ordem decrescente.
numero1 = float(input("Digite o número: "))
numero2 = float(input("Digite o número: "))
numero3 = float(input("Digite o número: "))
print ("Numero: ", numero1)
print ("Numero: ", numero2)
print ("Numero: ", numero3)

if numero1 > numero2 > numero3:
    print (numero1,numero2,numero3)
if numero1 > numero3 > numero2:
    print (numero1,numero3,numero2)

if numero2 > numero1 > numero3:
    print (numero2,numero1,numero3)
if numero2 > numero3 > numero1:
    print (numero2,numero3,numero1)

if numero3 > numero1 > numero2:
    print (numero3,numero1,numero2)

if numero3 > numero2 > numero1:
    print (numero3,numero2,numero1)
if numero1 > numero2 > numero3:
    print (numero1,numero2,numero3)
else:
    numero1 == numero2 == numero3
    print ("Invalido")