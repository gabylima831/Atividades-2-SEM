"""
Exercício: Gerenciamento de Lista de Nomes e Tipos Sanguíneos
Objetivo: Criar um programa Python que permita aos alunos gerenciar uma lista de nomes de pessoas e seus tipos sanguíneos. 
Os alunos serão instruídos a adicionar, visualizar e salvar os dados em um arquivo de texto.

Instruções:
Crie um programa Python que ofereça as seguintes funcionalidades:
a. Adicionar um novo nome e tipo sanguíneo à lista.
b. Visualizar a lista atual de nomes e tipos sanguíneos.
c. Salvar a lista em um arquivo de texto chamado "lista_tipos_sanguineos.txt".

O programa deve começar com uma lista vazia e dar ao usuário a opção de adicionar nomes e tipos sanguíneos. 
Eles devem ser capazes de adicionar quantas entradas desejarem.

O programa também deve permitir ao usuário visualizar a lista de nomes e tipos sanguíneos.

Após adicionar nomes e tipos sanguíneos, o programa deve fornecer a opção de salvar os dados em um arquivo de texto. 
Os dados devem ser formatados de forma legível.

Ao iniciar o programa, ele deve verificar se o arquivo "lista_tipos_sanguineos.txt" existe. 
Se o arquivo existir, o programa deve carregar os dados do arquivo no início da execução.

Dica: Você pode usar uma estrutura de dados como uma lista de dicionários para armazenar os nomes e tipos sanguíneos, 
e a função open() para criar ou carregar o arquivo. Certifique-se de lidar com exceções, como erros de abertura ou leitura de arquivo.
"""
lista_pessoas = []

nome_arquivo = 'lista_tipos_sanguineos.txt'

def adicionar_nome_e_tipo_sanguineo():
    nome = input('Digite o nome do paciente: ')
    tipo_sanguineo = input('Digite o tipo sanguíneo: ')
    pessoa = {
        'Nome': nome,
        'Tipo sangúineo': tipo_sanguineo
    }
    lista_pessoas.append(pessoa)
    print(f'Dados de{pessoa} armazenados com sucesso!')

def ver_lista():
    if not lista_pessoas:
        print('A lista está vazia.')
    else:
        print('Lista de nomes e de tipos sanguíneos: ')
        for pessoa in lista_pessoas:
            print(
                f'Nome: {pessoa["Nome"]}, Tipo sanguíneo: {pessoa["Tipo sanguíneo"]}'
            )

def salvar_dados():
    with open(nome_arquivo, 'w') as arquivo:
        for pessoa in lista_pessoas:
            arquivo.write(
                f'Nome: {pessoa["Nome"]}, Tipo sanguíneo: {pessoa["Tipo sanguíneo"]}'
            )
        print('Arquivo gerado com sucesso!')

def carregar_dados():
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                nome = dados[0].split(': ')[1]
                tipo_sanguineo = dados[1].split(': ')[2]
                pessoa = {
                    'Nome': nome,
                    'Tipo sangúineo': tipo_sanguineo
                }
                lista_pessoas.append(pessoa)
        print('Dados carregados com sucesso!')
    except FileNotFoundError:
        print(f'{nome_arquivo} não encontrado. Contate o administrador do sistema.')

carregar_dados()
while True:
    print('\n Opções: ')
    print(
        '1) Adicionar paciente e tipo sanguíneo;\n 2) Ver pacientes;\n 3) Salvar dados em arquivo;\n 4) Sair do sistema;'
    )
    opcao = input('Selecione uma opção: ')
    if opcao == '1':
        adicionar_nome_e_tipo_sanguineo()
    elif opcao == '2':
        ver_lista()
    elif opcao == '3':
        salvar_dados()
    elif opcao == '4':
        print('Sistema encerrado com sucesso.')
        break
    else:
        print('Opção inválida, tente novamente!')

'''
with open(novo_nome) as arquivo: 
    arquivo.append('')

print(f'Digite um nome: ')

tipo_sanguineo = 'lista_tipos_sanguineos.txt'
'''