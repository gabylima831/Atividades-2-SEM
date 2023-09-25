#Gerador de Senhas:
### Crie um gerador de senhas que gera senhas aleatórias com base no comprimento especificado pelo usuário.
# Dica: use a biblioteca random do Python para gerar números aleatórios.
### Bônus: permita que o usuário especifique quantas letras, números e caracteres especiais a senha deve conter.

import string 
import random 

def gerar_senha(len_senha = 8):
  letras = int(input('Digite a quantidade de letras da sua senha: '))
  numeros = int(input('Digite a quantidade de números da sua senha: '))
  caracteres_especiais = int(input('Digite a quantidade de caracteres especiais da sua senha: '))
  letras = string.ascii_letters 
  numeros = string.digits
  caracteres_especiais = string.punctuation

  senha_completa = letras + numeros + caracteres_especiais + escolha_usuario

  senha_usuario = ""

  for i in range(numeros, letras, caracteres_especiais):
    dígitos = random.choice = senha_completa
    senha_usuario = senha_usuario + dígitos
  
escolha_usuario = input('Quantos dígitos a senha possui?: ')
if escolha_usuario.isdigit():
  escolha_usuario = int(escolha_usuario)
else:
  print('Entrada inválida!')
  quit()

response = gerar_senha(len_senha = escolha_usuario)
print(f'Sua senha é: \n{response}')
