#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. 
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.


totalVotos = input ("Informe o numero total de votos: ")
totalVotos = float (totalVotos)

total_votos_nulos = input ("Escreva o numero total de votos nulos: ")
total_votos_nulos = float (total_votos_nulos)

total_votos_brancos = input ("Escreva o numero total de votos brancos: ")
total_votos_brancos = float (total_votos_brancos)

total_votos_validos = input ("Escreva o numero total de votos validos: ")
total_votos_validos = float (total_votos_validos)

percentual_votos_nulos = (total_votos_nulos/totalVotos)*100
print("o percentual de votos nulos em relação ao total de eleitores é: ", percentual_votos_nulos, "%")

percentual_votos_brancos = (total_votos_brancos/totalVotos)*100
print("o percentual de votos brancos em relação ao total de eleitores é: ", percentual_votos_brancos, "%")

percentual_votos_validos = (total_votos_validos/totalVotos)*100
print("o percentual de votos validos em relação ao total de eleitores é: ", percentual_votos_validos, "%")