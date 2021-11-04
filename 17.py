

codEmp = int(input('Informe o código do empregado: '))
anoNasc = int(input('Informe o ano de nascimento do empregado: '))
anoIngresso = int(input('Informe o ano de ingresso do empregado na empresa: '))
anoAtual = 2021  
idade = (anoAtual - anoNasc)
tempServ = (anoAtual - anoIngresso)
print (' Idade do Empregado:', idade,'Tempo de serviço:', tempServ)
if (idade >= 65): 
    print (' Requerer aposentadoria')
elif (tempServ >= 30): 
    print (' Requerer aposentadoria')
elif (idade >= 60) and (tempServ >= 25):
    print (' Requerer aposentadoria')
    
    #porque ele não continua o if e else depois da impressão?
            
            

