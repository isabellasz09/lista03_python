#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
#Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. (usar ELIF)
print("Isabella Carolina de Souza")
numero1= int(input("Digite o primeiro numero: "))
numero2= int(input("Digite o segundo numero: "))
opera=input("Digite a operção: ")
if opera == "+":
    print("resultado",(numero1+numero2))
if opera == "-":
    print("resultado",(numero1-numero2))
if opera == "*":
    print("resultado",(numero1*numero2))
if opera == "/":
    print("resultado",(numero1/numero2))
if opera != "+" and opera != "-" and opera != "*" and opera != "/":
    print("operação invalida")