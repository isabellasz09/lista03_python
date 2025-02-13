#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
print("Isabella Carolina de Souza")
distancia=int(input("Qual a distância que um passageiro deseja percorrer em km: "))
if distancia > 200:
    print("valor cobrado: ",distancia*0.45,"reais")
else:
    print("valor cobrado: ",distancia*0.50,"reais")