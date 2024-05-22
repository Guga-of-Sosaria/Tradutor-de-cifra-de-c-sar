import os

#Função para codificar
def codificar(string, num, lista):
    nascii = int
    for i in range(0, len(string)):
        #Verifica se o caractére é uma letra
        if string[i].isalpha():
            #Decodifica a letra
            nascii = ord(string[i]) + num
            #Volta pro início do alfabeto se o resultado ultrapassar o Z
            if nascii > 90:
                nascii = 65 + (nascii - 90 - 1)
            lista.append(chr(nascii))
        else:
            lista.append(string[i])
#Função para decodificar
def decodificar(string, num, lista):
    nascii = int
    for i in range(0, len(string)):
        #Verifica se o caractére é uma letra
        if string[i].isalpha():
            #Decodifica a letra
            nascii = ord(string[i]) - num 
            #Volta pro fim do alfabeto se o resultado for menor que A  
            if nascii < 65:
                nascii = 90 - (65 - nascii - 1)
            lista.append(chr(nascii))
        else:
            lista.append(string[i])
print("|||TRADUTOR E DECODIFICADOR DE CIFRA DE CÉSAR|||", end="\n\n")
while True:
    print("Bem vindo! Por favor, Escolha uma opreação:")
    print("1) Codificar\n2) Decodificar")
    opcao = input()
    if opcao == "1":
        #Codifica a palavra
        codigo = []
        palavra = input("Digite algo para codificar: ")
        chave = int(input("Agora digite a chave: "))
        palavra = palavra.upper()
        codificar(palavra, chave, codigo)
        #Exibe o código
        print("")
        for i in codigo:
            print(i, end="")
        print("\n")
    elif opcao == "2":
        #Traduz o código
        traducao = []
        codigo = input("Digite o codigo a ser decodificado: ")
        chave = int(input("Agora digite a chave: "))
        codigo = codigo.upper()
        decodificar(codigo, chave, traducao)
        #Exibe a tradução
        print("")
        for i in traducao:
            print(i, end="")
        print("\n")
    else:
        os.system('cls')
        continue
    continuar = input("Aperte 1 para realizar outra operação ou aperte qualquer outra tecla para fechar o programa: ")
    if continuar == "1":
        os.system('cls')
    else:
        break
