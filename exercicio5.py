#Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite. Se ele responder "sim", pergunte se está ventando. 
# Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", caso contrário, exiba a mensagem "Pegue um guarda-chuva".
# Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".
estachovendo=input("Está chovendo? ")
estaventando=input("Está ventando? ")
if estachovendo == ("sim"):
    print(estaventando)
else:
    if estachovendo == ("não"):
        print("Aproveite seu dia!")
    else:
        if estaventando == ("sim"):
            print("Está ventando demais para um guarda-chuva")
