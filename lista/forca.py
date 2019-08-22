# para definir uma funcao no python voce usa a palavra "def" segue o examplo encapsulando o jogo em uma função para ser
# chamado em outro arquivo
def jogar():
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************")


# variaveis
palavra_secreta = "banana"
# no python para definiçao de uma lista se usa o "[]", no exmplo abaixo e passado uma lista com a quantidade
# de caracteres da palavra_secreta
letras_acertadas = ["_", "_", "_", "_", "_", "_"]

# definindo uma variavel  para ver se a forca acabou
# essa variavel e booleana pode ser "True" ou "False"
enforcou = False
acertou = False


print(letras_acertadas)

# para negar se usa a palavra "not" e para a condiciona usa se a palavra "and"
while (not enforcou and not acertou):
    chute = input("Qual letra? ")
    # remove os espaços da string "strip()"
    chute = chute.strip()

    index = 0
    # for pela iterando por cada letra da palavra
    for letra in palavra_secreta:
        # verifica se a letra digitada tem no chute
        # usa o metodo upper para colocar tudo maiuscolo para fazer a comparação metodo "str.upper()"
        if (chute.upper() == letra.upper()):
            # adiciona a letra caso tenha acertado no local correto do arry
            letras_acertadas[index] = letra
        index = index + 1

    print(letras_acertadas)
print("fim de jogo ")

# esse codigop so vai executar quando o este arquivo for executado como arquivo principal
#     ou seja não sera executado caso ele estaja como um importe ,
# sendo assim quando cahmarmos somente este arquivo o jogo ira iniciar, agora se ele
# tiver sido importado o jogo so inicia se agente chamar explicitamente o metodo jogar
if (__name__ == "__main__"):
    jogar()
