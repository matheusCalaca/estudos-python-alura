# para definir uma funcao no python voce usa a palavra "def" segue o examplo encapsulando o jogo em uma função para ser
# chamado em outro arquivo
def jogar():
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************")


# variaveis
palavra_secreta = "calaca".upper()
# no python para definiçao de uma lista se usa o "[]", no exmplo abaixo e passado uma lista com a quantidade
# de caracteres da palavra_secreta
# adicionado um for dentro da gerção da palavra
letras_acertadas = ["_" for letra in palavra_secreta]

# definindo uma variavel  para ver se a forca acabou
# essa variavel e booleana pode ser "True" ou "False"
enforcou = False
acertou = False
# criando variaveis para verificar a quantidade de erros
erros = 0
quantidade_erros_para_enforca = 6


print(letras_acertadas)

# para negar se usa a palavra "not" e para a condiciona usa se a palavra "and"
while not enforcou and not acertou:
    chute = input("Qual letra? ")
    # remove os espaços da string "strip()"
    chute = chute.strip().upper()

    # verifica se palavra contem o chute
    if(chute in palavra_secreta):
        index = 0
        # for pela iterando por cada letra da palavra
        for letra in palavra_secreta:
            # verifica se a letra digitada tem no chute
            # usa o metodo upper para colocar tudo maiuscolo para fazer a comparação metodo "str.upper()"
            if (chute == letra):
                # adiciona a letra caso tenha acertado no local correto do arry
                letras_acertadas[index] = letra
            index = index + 1
    else:
        erros += 1
        print(f"Ops, você errou! Faltam {6 - erros} tentativas.")
    enforcou = erros == quantidade_erros_para_enforca
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

if acertou:
    print("Você GANHOU!")
else:
    print("Você PERDEU!")
print("fim de jogo ")

# esse codigop so vai executar quando o este arquivo for executado como arquivo principal
#     ou seja não sera executado caso ele estaja como um importe ,
# sendo assim quando cahmarmos somente este arquivo o jogo ira iniciar, agora se ele
# tiver sido importado o jogo so inicia se agente chamar explicitamente o metodo jogar
if (__name__ == "__main__"):
    jogar()
