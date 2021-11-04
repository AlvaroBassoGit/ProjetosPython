#A cancela de um estabelecimento, neste momento de pandemia funciona dependendo da temperatura aferida e registrada pelo recepcionista do local. 
# É preciso criar um algoritmo para liberar ou não cancela dependendo da temperatura corporal. 
# Com um medidor o recepcionista irá aferir e registrar no sistema e o algoritmo deverá liberar caso a temperatura seja <= 37 e não liberar caso a temperatura seja maior que 37º.
#A cancela só recebe True ou False (True para liberar e False para bloquear)

# (como fazer para imprimir o valor tru e false?)
# porque eu preciso tem uma variavel com valor bool?
temp = False
temperatura = float(input("temperatura: "))
if temperatura <= 37:
    print (not temp)
if temperatura >37:
    print (temp)