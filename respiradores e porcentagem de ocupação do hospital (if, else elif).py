#Receber do usuário a quantidade de respiradores e a porcentagem de ocupação de 5 hospitais em Salvador, 
# caso algum desses hospitais tenham menos que 50 respiradores e a taxa ocupacional esteja maior que 60%, 
# serão adicionados mais 5. 

print ("Caso o numero de respiradores for menor que 50 e a taxa ocupacional esteja maior que 60%, adicionar 5 respiradores ao final")
print ("INFORME O NÚMERO DE RESPIRADORES DOS CINCO HOSPITAIS")
h1respiradores = float(input("Informe a quantidade de respiradires hospital 1: "))
h2respiradores = float(input("Informe a quantidade de respiradires hospital 2: ")) 
h3respiradores = float(input("Informe a quantidade de respiradires hospital 3: ")) 
h4respiradores = float(input("Informe a quantidade de respiradires hospital 4: ")) 
h5respiradores = float(input("Informe a quantidade de respiradires hospital 5: "))

print ("INFORME O NÚMERO DE OCUPAÇÃO CINCO HOSPITAIS")
h1porcentagem_ocupacao = float(input("Informe a porcentagem de ocupação hospital 1: "))
h2porcentagem_ocupacao = float(input("Informe a porcentagem de ocupação hospital 2: "))
h3porcentagem_ocupacao = float(input("Informe a porcentagem de ocupação hospital 3: "))
h4porcentagem_ocupacao = float(input("Informe a porcentagem de ocupação hospital 4: "))
h5porcentagem_ocupacao = float(input("Informe a porcentagem de ocupação hospital 5: "))


if h1respiradores < 50 and h1porcentagem_ocupacao > 60:
    print (" O numero dos respiradores é de: ",h1respiradores + 5, "no hospital 1")
else:
    print ("respiradores:",h1respiradores, "porcentagem de ocupação:",h1porcentagem_ocupacao,"%, no hospital 1")
    
if h2respiradores < 50 and h2porcentagem_ocupacao > 60:
    print (" O numero dos respiradores é de: ",h2respiradores + 5, "no hospital 2")
else:
    print ("respiradores:",h2respiradores, "porcentagem de ocupação:",h2porcentagem_ocupacao,"%, no hospital 2")
    
if h3respiradores < 50 and h3porcentagem_ocupacao > 60:
    print (" O numero dos respiradores é de: ",h3respiradores + 5, "no hospital 3")
else:
    print ("respiradores:",h3respiradores, "porcentagem de ocupação:",h3porcentagem_ocupacao,"%, no hospital 3")
    
if h4respiradores < 50 and h4porcentagem_ocupacao > 60:
    print (" O numero dos respiradores é de: ",h4respiradores + 5, "no hospital 4")
else:
    print ("respiradores:",h4respiradores, "porcentagem de ocupação:",h4porcentagem_ocupacao,"%, no hospital 4")
    
if h5respiradores < 50 and h5porcentagem_ocupacao > 60:
    print (" O numero dos respiradores é de: ",h5respiradores + 5, "no hospital 5")
else:
    print ("respiradores:",h5respiradores, "porcentagem de ocupação:",h5porcentagem_ocupacao,"%, no hospital 5")

