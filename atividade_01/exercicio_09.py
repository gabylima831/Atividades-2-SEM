# Exercício 09 - Crie uma aplicação que solicita ao usuário que digite um texto e imprima no console o texto digitado pelo usuário sem nenhuma vogal.

def sem_vogais():
    texto = input('Digite um texto: ')
    return texto.lower().replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
print(sem_vogais())