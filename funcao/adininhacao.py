# funçoes que não são buld-in e nessessario o import,
# para fazer o importe usa a estrutura ("import LIB_A_SER_IMPORTADA")
# exmplo de importe e a lib random abaixo
import random

print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

# variaveis
# exmplo de uso do random que vai nos dar um numero de 1 ate 100
numero_secreto = random.randrange(1, 101)
numero_tentativas = 0
rodada = 1
pontos = 1000

# criando parte de nivel para o jogo
print("Escolha seu nivel de dificuldade ")
print("Quantidade de tentativas Fácil=20  Médio=10 Difícil=5 ")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Defina o nível: "))

if (nivel == 1):
    numero_tentativas = 20
elif (nivel == 2):
    numero_tentativas = 10
else:
    numero_tentativas = 5



# laço de repetiçao for e utilizado um range(valor inicial, valor final, valor incrementar)
for rodada in range(rodada, numero_tentativas + 1):

    # formatação de string interpolacao de string
    print("rodada {} de {}".format(rodada, numero_tentativas))
    # o input sempre recebe uma string
    chute_str = input("Digite um numero de (1 ate 100) : ")
    # converter de str para int
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("o chute tem que ser de 1 a 100")
        # continue serve para continuar
        continue

    # variaveies de comparação
    chute_menor = numero_secreto < chute
    chute_maior = numero_secreto > chute
    acerto_numero_secreto = numero_secreto == chute

    # condicional falando se acerto  ou não, o if e separado por ": " no python
    if (acerto_numero_secreto):
        # para o python apos o IF voce tem que dar 4 espaços para escrever a condicional, se ficar grudado no inicio do arquivo da falha
        print("Você ACERTO o numero secreto: ", numero_secreto)
        # exibe a pontuação
        print (f"Sua pontuação foi: {pontos}")
        # para o laço
        break
    else:
        # para se fazer um else if em python usa se  "ELIF"
        if (chute_maior):
            print("Você  ERROU o numero secreto: ", chute, " é  MAIOR que o numero secreto")
        elif (chute_menor):
            print("Você  ERROU o numero secreto: ", chute, " é MENOR que o numero secreto")

        # calculo de pontuação e a pontuação menos a diferença da quantidade que voce acertou
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
# apartir do pytho 3.6  o voce pode concatena a variavel dentro das aspas como conchete "{}" e adicionando o "f" no inicio do print "print(f"valor: {variavel}")
print(f"Numero secrto {numero_secreto}")
print("fim do programa")
