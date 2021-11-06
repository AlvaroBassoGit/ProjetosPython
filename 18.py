#Desenvolva um algoritmo que solicite o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é sempre pelo mais barato.
# < menor que > maior que

produto1 = float(input ("Produto 1, R$: "))
produto2 = float(input ("Produto 2, R$: "))
produto3 = float(input ("Produto 3, R$: "))

print("resposta")
if (produto1 <= produto2) and (produto1 <= produto3):
    print ("compre produto 1")
elif (produto2 <= produto1) and (produto2 <= produto3):
    print ("compre produto 2")
elif (produto3 <= produto1) and (produto3 <= produto2):
    print ("compre produto 3")
