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