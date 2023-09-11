# Exercício 02 - Crie uma aplicação que solicite ao usuário digitar uma palavra e imprima no console a quantidade de caracteres que a palavra possui.

def contar_caracteres(palavra):
    contar_caracteres = palavra.lower().replace(' ', '')
    return len(contar_caracteres)
print ('O texto contém ', contar_caracteres(input('Digite um texto: ')), 'caracteres.')