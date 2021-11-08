#Faça um Programa que leia três números inteiros e mostre o maior deles.
numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))
numero3 = float(input("Número 3: "))
print ("Numero 1: ", numero1)
print ("Numero 2: ", numero2)
print ("Numero 3: ", numero3)

if numero1 > numero2 and numero3:
    print ("O número 1 é maior: ", numero1)
elif numero2 > numero3 and numero1:
    print ("O número 2 é maior: ", numero2)
else:
    print ("O número 3 é maior: ", numero3)
