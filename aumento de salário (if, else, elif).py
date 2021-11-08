#  As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#alários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, 

# informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario_atual = float (input("Informe seu sálario: "))
aumento1 = (salario_atual)*(20/100)
aumento2 = (salario_atual)*(15/100)
aumento3 = (salario_atual)*(10/100)
aumento4 = (salario_atual)*(5/100)
if salario_atual <= 280:
    print (salario_atual + aumento1)
elif salario_atual >= 281 or salario_atual == 700:
    print (salario_atual + aumento2)
elif salario_atual >= 701 or salario_atual == 1500:
     print (salario_atual + aumento3)
else:
    print (salario_atual + aumento4)
    
    
