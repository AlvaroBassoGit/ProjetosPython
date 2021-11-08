
salario_atual = float(input("informe o salario atual: "))

if (salario_atual>500):
    salario_novo=salario_atual+(salario_atual*0.15)
    print("salario com reajuste" "=",salario_novo)
    
if ((salario_atual>=500) and (salario_atual<=1000)):
    salario_novo=salario_atual+(salario_atual*0.10)
    print("salario com reajuste" "=",salario_novo)
    
    
if (salario_atual >1000):
    salario_novo=salario_atual+(salario_atual*0.05)
    print("salario com reajuste" "=", salario_novo) 