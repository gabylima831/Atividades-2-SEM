# Exercício 05 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console o nome com todas as letras minúsculas.

def lower():
    texto = input ('Digite seu nome completo: ')
    return texto.lower()
print (lower())