#A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3 grupos de indústrias que são altamente poluentes do meio ambiente. 
# O índice de poluição aceitável varia de 0,05 até 0,25. 
# Se o índice sobe para 0,3 as indústrias do 1º grupo são intimadas a suspenderem suas atividades, 
# se o índice crescer para 0,4 as indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades, se o índice atingir 0,5 
# todos os grupos devem ser notificados a paralisarem suas atividades. 
# Faça um algoritmo que leia o índice de poluição medido e emita a notificação adequada aos diferentes grupos de empresas
 
 # não intendi as identações

industrias1 =  ("GBOM, PLANTOS, AVON, AMBEV")
industrias2 =  ("TRAMONTINA, GOOGLE, CARREFUR")
industrias3 =  ("SONHO, TURBOTECH, ENGENHARIAB")

indice = float(input("Escreva o índice de poluição: "))

if indice >= 0.5:
    print ("Intimar as empresas",industrias1, ",", industrias2, "e", industrias3, "a paralizar as atividas.")
else:
    if indice >= 0.4:
        print ("Intimar as empresas",industrias1, "e", industrias2, "a suspenderem as atividades.")
    else:
        if indice >= 0.3:
            print ("Intimar as empresas",industrias1, "a suspenderem as atividas.")
        else:  
            if indice < 0.3:
                print ("Nenhuma empresa precisa paralizar as atividas")
    
    