# Exercício 10 - Crie uma aplicação que solicita ao usuário que digite um texto e retorne a quantidade de caracteres que o texto possui.

def qnt_de_caracteres(texto):
    contar_caracteres = texto.lower().replace(' ', '')
    return len(contar_caracteres)
print('O texto contém ', qnt_de_caracteres(input('Digite um texto: ')), 'caracteres.')