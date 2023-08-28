# String Methods - Métodos de String

# Exercício 01 - Crie uma função que solicite ao usuário digitar uma palavra e substitua as vogais por "*" e a execute numa aplicação que solicite uma palavra ao usuário e imprima o resultado no console, independentemente do usuário digitar a palavra em maiúscula ou minúscula.

def replace_vogais(texto):
    return texto.replace ('a' , '*').replace ('A', '*').replace('e', '*').replace('E', '*').replace('i', '*').replace('I', '*').replace('o', '*').replace ('O', '*').replace('u','*').replace('U', '*')
print (replace_vogais(input('Digite uma palavra: ')))

# Exercício 02 - Crie uma aplicação que solicite ao usuário digitar uma palavra e imprima no console a quantidade de caracteres que a palavra possui.

def contar_caracteres(palavra):
    contar_caracteres = palavra.lower().replace(' ', '')
    return len(contar_caracteres)
print ('O texto contém ', contar_caracteres(input('Digite um texto: ')), 'caracteres.')

# Exercício 03 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console quantas vezes aparece a letra "a", independente de ser maiúscula ou minúscula.

def contador_de_a():
    texto = input('Digite seu nome completo: ')
    return f'As letras "a" e "A" aparecem {texto.count("a") , texto.count("A")} vezes no seu nome.'
print (contador_de_a())

# Exercício 04 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console o nome com todas as letras maiúsculas.

def upper():
    texto = input ('Digite seu nome completo: ')
    return texto.upper()
print (upper())
    
# Exercício 05 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console o nome com todas as letras minúsculas.

def lower():
    texto = input ('Digite seu nome completo: ')
    return texto.lower()
print (lower())

# Exercício 06 - Crie uma aplicação que solicite ao usuário digitar o seu nome e sobrenome e imprima no console o nome com todas as letras maiúsculas e o sobrenome com todas as letras minúsculas sem espaços entre o nome e o sobrenome e sem alterar a variável original.
 
def seletor_de_nome():
    nome_completo = input ('Escreva seu nome e sobrenome: ')
    nome_completo = nome_completo.title().split()
    primeiro_nome = nome_completo [0]
    ultimo_nome = nome_completo [-1]
    return f'Seu nome completo é {primeiro_nome.upper() + ultimo_nome.lower()}.'
print (seletor_de_nome())

# Exercício 07 - Crie uma aplicação em que o usuário digite o seu nome e sobrenome de uma só vez e armazene o nome em uma variável 'nome_usuário' e o sobrenome em uma variável 'sobrenome_usuario'. Em seguida, crie uma variável 'nome_completo' que armazene o nome completo do usuário com todas as letras maiúsculas e imprima no console o nome completo do usuário com todas as letras minúsculas. Além disso, crie outra variável chamada 'tamanho_nome_completo' que armazene o tamanho do nome completo do usuário e imprima no console o tamanho do nome completo do usuário.

def cadastro_usuario():
    nome_completo = input ('Digite seu nome e sobrenome: ')
    nome_usuario = nome_completo[0]
    sobrenome_usuario = nome_completo[-1]
    nome_completo = nome_completo.upper()
    tamanho_nome_completo = len(nome_completo)
    return f'Seu nome, {nome_completo.lower()}, contém {len(nome_completo)} caracteres.'
print (cadastro_usuario())
    
# Exercício 08 - Crie um programa que solicite apresenta um menu de opções no Console e solicite ao usuário que digite a opção desejada. Em seguida, crie uma função para cada opção do menu que execute a ação solicitada pelo usuário. O menu deve conter as seguintes opções:

# 1. Conte o número total de palavras digitadas.
# 2. Conte o número de vogais na palavra digitada (ignore maiúsculas/minúsculas, ou seja, "Python" e "python" devem ser contadas como iguais).
# 3. Substitua todas as ocorrências da palavra "Python" por "Java".
# 4. Converta todas as letras da string para minúsculas.
# 5. Crie uma lista com todas as palavras únicas encontradas na string (ignorando maiúsculas/minúsculas).
# 6. Imprima as palavras na string em ordem alfabética.

def menu_de_opcoes(selecionar_opcao):
    if selecionar_opcao >= 1 or selecionar_opcao <=6:
        texto = input('\nDigite uma palavra ou uma frase: ')
        
    if selecionar_opcao == 1:
        print('Opção selecionada: 1')
        print(contar_palavras(texto),'\n')
            
    elif selecionar_opcao == 2:
        print('Opção selecionada: 2')
        print(contar_vogais(texto),'\n')
    
    elif selecionar_opcao == 3:
        print('Opcão selecionada: 3')
        print(substituir_palavra(texto),'\n')
    
    elif selecionar_opcao == 4:
        print('Opção selecionada: 4')
        print(formatar_minusculo(texto),'\n')
    
    elif selecionar_opcao == 5:
        print('Opção selecionada: 5')
        print(lista_palavras_unicas(texto),'\n')
    
    elif selecionar_opcao == 6:
        print('Opção selecionada: 6')
        print(ordem_alfabetica(texto),'\n')

    else:
        print('Opção inválida. \nAcesso finalizado!')

def contar_palavras(texto): 
    quantidade_de_palavras = texto.split();
    if len(quantidade_de_palavras)>1:
        return f"O texto acima possui {len(quantidade_de_palavras)} palavras."
    else:
        return f'{len(quantidade_de_palavras)} palavras inseridas.'

def contar_vogais(texto):
    qnt_de_vogais = texto.count('a') + texto.count ('e') + texto.count('i') + texto.count('o') + texto.count('u')
    if qnt_de_vogais > 1:
        return f'O texto acima possui {qnt_de_vogais} vogais.'
    else:
        return f'O texto acima possui {qnt_de_vogais} vogais.'

def substituir_palavra(texto):
    troca_de_texto = texto.capitalize().replace('Python', 'Java')
    return f'Novo texto: \n {troca_de_texto}'

def formatar_minusculo(texto):
    return texto.lower()

def lista_palavras_unicas(texto):
    texto = texto.lower().split()
    palavras_unicas = list(set(texto))
    return f'Lista de palavras únicas: \n {palavras_unicas}'

def ordem_alfabetica(texto):
    lista_de_palavras = texto.split()
    lista_de_palavras = sorted(lista_de_palavras)
    return f'Palavras em ordem alfabética: \n {lista_de_palavras}'

def opcoes_menu():
    opcao_1 = '1. Conte o número total de palavras digitadas.'
    opcao_2 = '2. Conte o número de vogais na palavra digitada (ignore maiúsculas/minúsculas, ou seja, "Python" e "python" devem ser contadas como iguais).'
    opcao_3 = '3. Substitua todas as ocorrências da palavra "Python" por "Java".'
    opcao_4 = '4. Converta todas as letras da string para minúsculas.'
    opcao_5 = '5. Crie uma lista com todas as palavras únicas encontradas na string (ignorando maiúsculas/minúsculas).'
    opcao_6 = '6. Imprima as palavras na string em ordem alfabética.'
    print("---- Menu de Opções: ---- ")
    print(f' {opcao_1}\n {opcao_2}\n {opcao_3}\n {opcao_4}\n {opcao_5}\n {opcao_6}')
    selecionar_opcao = input('Digite a opção desejada: ')
    menu_de_opcoes(int(selecionar_opcao))

opcoes_menu()

# Exercício 09 - Crie uma aplicação que solicita ao usuário que digite um texto e imprima no console o texto digitado pelo usuário sem nenhuma vogal.

def sem_vogais():
    texto = input('Digite um texto: ')
    return texto.lower().replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
print(sem_vogais())

# Exercício 10 - Crie uma aplicação que solicita ao usuário que digite um texto e retorne a quantidade de caracteres que o texto possui.

def qnt_de_caracteres(texto):
    contar_caracteres = texto.lower().replace(' ', '')
    return len(contar_caracteres)
print('O texto contém ', qnt_de_caracteres(input('Digite um texto: ')), 'caracteres.')

####################################################################################
#------------------------------------------------------------------------------------
#-----------------------------DESAFIO DE ARTE ASCII----------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
####################################################################################


# Crie um programa Python que permita ao usuário criar sua própria arte ASCII no console. Siga as instruções abaixo:

# Solicite ao usuário que insira um caractere (por exemplo, "*", "@", "#", etc.) que será usado para criar o padrão de arte. Solicite ao usuário que insira um número inteiro positivo que represente a altura do padrão de arte. Use o caractere fornecido pelo usuário e crie um padrão de arte que tenha a forma de um triângulo retângulo. O triângulo deve ter a altura especificada pelo usuário. Imprima o padrão de arte no console. Cada linha do triângulo deve conter um número crescente de caracteres, começando com 1 na primeira linha e aumentando em 1 em cada linha subsequente.

# DICA: Use métodos de string para criar e formatar o padrão de arte e lembre-se de que podemos fazer operações matemáticas com strings em Python, como multiplicação e adição.

inserir_caractere = input('Insira um caractere (como -, ., / e entre outros.): ')
altura_da_arte = input('Digite um número inteiro positivo: ')
if int(altura_da_arte)>0:
    print(f'Triângulo retângulo com {inserir_caractere} e {altura_da_arte} de altura. \n')

    for linhas in range(1, int(altura_da_arte)+1):
        print(inserir_caractere*linhas)
    print('\n Sua arte está pronta! \n')
else:
    print('\n Caractere inserido inválido! \n')