#Analisador de String:
### Faça um programa que analise uma string inserida pelo usuário e conte quantas letras maiúsculas, minúsculas, dígitos e caracteres especiais ela contém.
### Bônus: faça o programa retornar quantas palavras há na string.

def lower():
    texto = input ('Digite seu nome completo: ')
    return texto.lower()
print (lower())

def upper():
    texto = input ('Digite seu nome completo: ')
    return texto.upper()
print (upper())
def contar_caracteres(palavra):
    contar_caracteres = palavra.lower().replace(' ', '')
    return len(contar_caracteres)
print ('O texto contém ', contar_caracteres(input('Digite um texto: ')), 'caracteres.')
