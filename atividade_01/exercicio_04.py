# Exercício 04 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console o nome com todas as letras maiúsculas.

def upper():
    texto = input ('Digite seu nome completo: ')
    return texto.upper()
print (upper())