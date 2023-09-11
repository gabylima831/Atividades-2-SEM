# String Methods - Métodos de String

# Exercício 01 - Crie uma função que solicite ao usuário digitar uma palavra e substitua as vogais por "*" e a execute numa aplicação que solicite uma palavra ao usuário e imprima o resultado no console, independentemente do usuário digitar a palavra em maiúscula ou minúscula.

def replace_vogais(texto):
    return texto.replace ('a' , '*').replace ('A', '*').replace('e', '*').replace('E', '*').replace('i', '*').replace('I', '*').replace('o', '*').replace ('O', '*').replace('u','*').replace('U', '*')
print (replace_vogais(input('Digite uma palavra: ')))