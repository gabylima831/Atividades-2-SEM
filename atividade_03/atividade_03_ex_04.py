# Contador de Palavras:
### Faça um programa que conte quantas palavras há em uma frase inserida pelo usuário.
### Bônus: faça o programa retornar a frase com todas as letras maiúsculas e sem espaços em branco.

def contador_palavras():
  frase = input('Digite uma frase: ')
  palavras = frase.upper().split()
  qnt_de_palavras = len(palavras)
  return f'A quantidade de palavras na frase {palavras} é {qnt_de_palavras}.'
print(contador_palavras())