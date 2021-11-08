salario_atual = input ("Informe seu sálario: ")
salario_atual = float (salario_atual)

if (salario_atual<500):
    salario_novo = salario_atual + (salario_atual*0.15)
    print ("salario com reajuste é: ", salario_novo)
    
if ((salario_atual>=500) and (salario_atual<=1000)):
    salario_novo = salario_atual + (salario_atual*0.10)
    print ("salario com reajuste é: ", salario_novo)
    
if (salario_atual>1000):
    salario_novo = salario_atual + (salario_atual*0.05)
    print ("salario com reajuste é: ", salario_novo)