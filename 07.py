#O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). 
# Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

custo_fabrica_carro = input ("Escreva o custo total do carro: R$ ")
custo_fabrica_carro = float (custo_fabrica_carro)

distribuidor = (custo_fabrica_carro*28)/100

imposto = (custo_fabrica_carro*45)/100

total = (custo_fabrica_carro+distribuidor+imposto)

valor_total = print ("o valor total é: R$ ",total)