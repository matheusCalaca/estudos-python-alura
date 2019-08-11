print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

# declarando numero para comparaçao
numero_secreto = 42

# o input sempre recebe uma string
chute_str =  input("Digite um numero: ")

# converter de str para int
chute = int(chute_str)


# condicional falando se acerto  ou não, o if e separado por ": " no python
if(numero_secreto == chute):
    # para o python apos o IF voce tem que dar 4 espaços para escrever a condicional, se ficar grudado no inicio do arquivo da falha
    print("Você ACERTO o numero secreto: ", numero_secreto)
else:
    print("Você  ERROU o numero secreto: ", numero_secreto)

print("fim do programa")