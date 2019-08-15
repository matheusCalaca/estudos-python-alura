# importando os jogos de adivinhação e de forca
import adininhacao
import forca

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

