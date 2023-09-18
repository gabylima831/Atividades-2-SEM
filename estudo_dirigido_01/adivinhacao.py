# Exercício 9: Usando o método random(), crie um programa que solicita ao usuário que adivinhe um número inteiro entre 1 e 10. Se o usuário digitar um número 
# menor que 1 ou maior que 10, solicite que ele insira um número válido. 
# Se o usuário digitar um número válido, verifique se o número que o usuário digitou é igual ao número gerado aleatoriamente pelo programa. 
# Se o número for igual, imprima "Você acertou!". Caso contrário, imprima "Você errou!".

import random
numero_adivinhado = random.randint (1,10)

acerto = False
palpites = 0
while acerto == False:
  palpite_usuario = int(input('Digite um número (entre 1 e 10): '))  
  if palpites == numero_adivinhado:
    acerto = True
    print('Você acertou!')
  else: 
    palpites += 1
    print('Você errou!')     