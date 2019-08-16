# para definir uma funcao no python voce usa a palavra "def" segue o examplo encapsulando o jogo em uma função para ser
# chamado em outro arquivo
def jogar():
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************")

#variaveis
palavra_secrta = "banana"
# definindo uma variavel  para ver se a forca acabou
# essa variavel e booleana pode ser "True" ou "False"
enforcou = False
acertou = False

# para negar se usa a palavra "not" e para a condiciona usa se a palavra "and"
while(not enforcou and not acertou):
    print("Jogando")



# esse codigop so vai executar quando o este arquivo for executado como arquivo principal
#     ou seja não sera executado caso ele estaja como um importe ,
# sendo assim quando cahmarmos somente este arquivo o jogo ira iniciar, agora se ele
# tiver sido importado o jogo so inicia se agente chamar explicitamente o metodo jogar
if(__name__ == "__main__"):
    jogar()