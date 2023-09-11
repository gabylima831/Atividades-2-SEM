# Exercício 06 - Crie uma aplicação que solicite ao usuário digitar o seu nome e sobrenome e imprima no console o nome com todas as letras maiúsculas e o sobrenome com todas as letras minúsculas sem espaços entre o nome e o sobrenome e sem alterar a variável original.
 
def seletor_de_nome():
    nome_completo = input ('Escreva seu nome e sobrenome: ')
    nome_completo = nome_completo.title().split()
    primeiro_nome = nome_completo [0]
    ultimo_nome = nome_completo [-1]
    return f'Seu nome completo é {primeiro_nome.upper() + ultimo_nome.lower()}.'
print (seletor_de_nome())