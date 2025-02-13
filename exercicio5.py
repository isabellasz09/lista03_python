#Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite. Se ele responder "sim", pergunte se está ventando. 
# Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", caso contrário, exiba a mensagem "Pegue um guarda-chuva".
# Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".
print("Isabella Carolina de Souza")
estachovendo=input("Está chovendo? ")
if estachovendo.casefold() == "sim":
    estaventando=input("Está ventando? ")
    if estachovendo.casefold() == "sim":
        print("Etá ventando muito para um guarda-chuva")
    else: 
        print("arrume um guarda-chuva")
else:
    print("Aproveite seu dia!")
