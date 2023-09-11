# Exercício 03 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console quantas vezes aparece a letra "a", independente de ser maiúscula ou minúscula.

def contador_de_a():
    texto = input('Digite seu nome completo: ')
    return f'As letras "a" e "A" aparecem {texto.count("a") , texto.count("A")} vezes no seu nome.'
print (contador_de_a())