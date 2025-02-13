#Pergunte a idade do usuário. 
# Se tiver 16 anos ou mais, exiba a mensagem "Você pode votar", 
# se tiver 18 anos, exiba a mensagem "Você pode aprender a dirigir", 
# se tiver 14 anos, exiba a mensagem "Você pode comprar um bilhete de loteria" 
# se tiver menos de 14 anos, exiba a mensagem "Você pode fazer doces ou travessuras".
print("Isabella Carolina de Souza")
idade= int(input("Digite sua idade: "))
if idade >=16 and idade != 18:
    print ("Você pode votar")
if idade == 18:
    print("Você pode dirigir")
if idade == 14:
    print("Você pode comprar um bilhete de loteria")
if idade <14:
    print("Você pode fazer doces ou travessuras")

