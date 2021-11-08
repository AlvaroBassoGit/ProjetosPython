#Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B. 
# A seguir (utilizando apenas atribuições entre variáveis) troque os 
# seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa. 
# Ao final,escrever os valores que ficaram armazenados nas variáveis.

A = 10
B = 20

print("o valor de A é: ",A)
print("o valor de B é: ",B)

novo_valor = A
A    = B   
B    = novo_valor

print("o valor de A é: ",A)
print("o valor de B é: ",B)