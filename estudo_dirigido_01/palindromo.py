# Exercício 3: Crie um programa em que o usuário insira uma palavra e o programa retorna se a palavra é palíndromo ou não.

def palindromo():

    palavra = input("Digite uma palavra: ")
    inverso = palavra[::-1]
    if palavra == inverso:
        return "A palavra é um palíndromo."
    else:
        return "A palavra não é um palíndromo."
    
print(palindromo())
