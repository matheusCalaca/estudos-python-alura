# importando os jogos de adivinhação e de forca
import adininhacao
import forca

def jogar():
    print("********************************")
    print("* Bem vindo a central de jogos *")
    print("********************************")

    print("Escolha seu Jogo")
    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Defina o JOGO: "))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adininhacao.jogar()


# esse codigop so vai executar quando o este arquivo for executado como arquivo principal
#     ou seja não sera executado caso ele estaja como um importe ,
# sendo assim quando cahmarmos somente este arquivo o jogo ira iniciar, agora se ele
# tiver sido importado o jogo so inicia se agente chamar explicitamente o metodo jogar
if(__name__ == "__main__"):
    jogar()
