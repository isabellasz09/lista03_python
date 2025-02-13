#Escreva um programa que pergunte a velocidade do carro de um usuário.
#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
#Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
vel= int(input("Qual a velocidade: "))
if vel > 80:
    multa=(vel-80)*5
    print ("A sua multa é de: ",multa)