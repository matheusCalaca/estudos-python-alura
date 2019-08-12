print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

# variaveis
numero_secreto = 42
numero_tentativas = 3
rodada = 1

# laço de repetiçao while
while (rodada <= numero_tentativas):

    # formatação de string interpolacao de string
    print("rodada {} de {}".format(rodada, numero_tentativas))
    # o input sempre recebe uma string
    chute_str = input("Digite um numero: ")
    # converter de str para int
    chute = int(chute_str)

    # variaveies de comparação
    chute_menor = numero_secreto < chute
    chute_maior = numero_secreto > chute
    acerto_numero_secreto = numero_secreto == chute

    # condicional falando se acerto  ou não, o if e separado por ": " no python
    if (acerto_numero_secreto):
        # para o python apos o IF voce tem que dar 4 espaços para escrever a condicional, se ficar grudado no inicio do arquivo da falha
        print("Você ACERTO o numero secreto: ", numero_secreto)
    else:
        # para se fazer um else if em python usa se  "ELIF"
        if (chute_maior):
            print("Você  ERROU o numero secreto: ", chute, " é  MAIOR que o numero secreto")
        elif (chute_menor):
            print("Você  ERROU o numero secreto: ", chute, " é MENOR que o numero secreto")

    rodada = rodada + 1

print("fim do programa")
