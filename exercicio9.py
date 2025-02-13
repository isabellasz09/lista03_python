#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.
print("Isabella Carolina de Souza")
salario=float(input("Digite seu salario: "))
if salario <= 2259.20:
    print("Você está isento")
else: 
    if salario >= 2259.20 and salario <=2828.65:
        alicota=salario*7.5/100
        print("Você tera que pagar: ",alicota)
    else: 
        if salario >= 2826.66 and salario <=3751.05:
            alicota=salario*15/100
            print("Você tera que pagar: ",alicota)
        else: 
            if salario >= 3751.06 and salario <=4664.68:
                    alicota=salario*22.5/100
                    print("Você tera que pagar: ",alicota)
            else: 
                if salario >= 4664.68 and salario :
                    alicota=salario*27.5/100
                    print("Você tera que pagar: ",alicota)
            
