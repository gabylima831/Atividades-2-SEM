# Exercício 08 - Crie um programa que apresenta um menu de opções no Console e solicite ao usuário que digite a opção desejada. Em seguida, crie uma função para cada opção do menu que execute a ação solicitada pelo usuário. O menu deve conter as seguintes opções:

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