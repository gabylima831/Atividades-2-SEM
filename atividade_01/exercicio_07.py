# Exercício 07 - Crie uma aplicação em que o usuário digite o seu nome e sobrenome de uma só vez e armazene o nome em uma variável 'nome_usuário' e o sobrenome em uma variável 'sobrenome_usuario'. Em seguida, crie uma variável 'nome_completo' que armazene o nome completo do usuário com todas as letras maiúsculas e imprima no console o nome completo do usuário com todas as letras minúsculas. Além disso, crie outra variável chamada 'tamanho_nome_completo' que armazene o tamanho do nome completo do usuário e imprima no console o tamanho do nome completo do usuário.

def cadastro_usuario():
    nome_completo = input ('Digite seu nome e sobrenome: ')
    nome_usuario = nome_completo[0]
    sobrenome_usuario = nome_completo[-1]
    nome_completo = nome_completo.upper()
    tamanho_nome_completo = len(nome_completo)
    return f'Seu nome, {nome_completo.lower()}, contém {len(nome_completo)} caracteres.'
print (cadastro_usuario())