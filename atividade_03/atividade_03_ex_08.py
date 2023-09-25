# Jogo de Adivinhação:
###Implemente um jogo simples em que o computador escolhe um número aleatório e o usuário tenta adivinhar o número.
### Bônus: faça o computador informar se o número inserido pelo usuário é maior ou menor que o número escolhido pelo computador.

import random
numero_sorteado = random.choices

acertou = False
palpites = 0
while acertou == False:
    palpite_jogador = int(input('Qual é o seu palpite (nº aleatório)?: '))
    if palpite_jogador == numero_sorteado:
        acertou = True
        print('Parabéns, você acertou!')
    else:
        palpites += 1 
        print('Você errou, tente novamente.')
print(f'Você precisou de {palpites} palpites para acertar.')