# Exercício 10: Faça um programa que solicita ao usuário escrever um texto e conta quantas vezes a letra "a" aparece no texto.

def contador_a():
    texto = input('Digite um texto: ')
    return texto.count('a')
print(f"O texto contém a letra 'a' {contador_a()} vezes.")