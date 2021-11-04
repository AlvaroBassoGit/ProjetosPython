#Desenvolva um algoritmo que solicite o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é sempre pelo mais barato.
# < menor que > maior que

produto1 = float(input ("Produto 1, R$: "))
produto2 = float(input ("Produto 2, R$: "))
produto3 = float(input ("Produto 3, R$: "))

if produto1 < produto2:
    print ("compre o produto 1 pois é mais barato")
elif produto1 < produto3:
    print ("compre o produto 1 pois é mais barato")
    
elif produto2 < produto3:
    print ("compre o produto 2 pois é mais barato")
elif produto2 < produto1:
    print ("compre o produto 2 pois é mais barato")
 
else:
    print ("compre o produto 3 pois é mais barato")