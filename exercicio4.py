#Peça ao usuário para inserir sua cor favorita. Se ele digitar "vermelho", "VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho",
#caso contrário, exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".
print("Isabella Carolina de Souza")
corfav=input("Digite sua cor favorita: ")
if corfav == "Vermelho" or corfav == "vermelho" or corfav == "VERMELHO":
    print("Eu também gosto de vermelho")
else:
    print("Eu não gosto de,",corfav," eu prefiro vermelho")