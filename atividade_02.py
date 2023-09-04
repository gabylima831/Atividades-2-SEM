# JOKENPÔ
def jokenpo():
    import random
    opcoes_jogo = ['pedra', 'papel', 'tesoura']
    computador = random.choice(opcoes_jogo)
    usuario = opcoes_jogo [int(input('Escolha entre pedra, papel ou tesoura: \n 1. pedra \n 2. papel \n 3. tesoura \n'))-1]
    print(f'O computador escolheu {computador}.')
    print(f'O usuário escolheu {usuario}.')

    if usuario == computador:
        print('Parabéns, você acertou!')
    elif usuario == 'pedra' and computador == 'tesoura':
        print('Você ganhou!')
    elif usuario == 'papel' and computador == 'pedra':
        print('Você ganhou!')
    elif usuario == 'tesoura' and computador == 'papel':
        print('Você ganhou!')
    else:
        print('Você perdeu!')
        input('Pressione ENTER para continuar: ')
    jokenpo()
jokenpo()

# JOGO DE ADIVINHAÇÃO
import random
numero_sorteado = random.randint (0,10)

acertou = False
palpites = 0
while acertou == False:
    palpite_jogador = int(input('Qual é o seu palpite (nº entre 0 e 10)?'))
    if palpite_jogador == numero_sorteado:
        acertou = True
        print('Parabéns, você acertou!')
    else:
        palpites += 1
        print('Você errou, tente novamente.')
print(f'Você precisou de {palpites} palpites para acertar.')
