# file handling (gestão de arquivos)
# Quais são as funções básicas para a gestão de arquivos?
# Funções básicas: Ler (read); Criar (create); Acrescentar (append); Escrever (write).

#abrir_arquivo = open('lista.txt')
'''
lista_nomes = open(lista, 'r')
for x in lista_nomes:
    print(x)
'''
#Exercício: Criação de um arquivo de texto via Terminal.

#Objetivo: Criar um arquivo de texto chamado 'meuarquivo.txt' usando o console.

nome_arquivo = 'meuarquivo.txt'

with open(nome_arquivo, 'w') as arquivo: #w = write
    arquivo.write('Este é o conteúdo do arquivo')

print(f'O arquivo {nome_arquivo} foi criado com sucesso!')
'''    
lista = 'lista.txt'

f = open(lista)
print(f.readline())
f.close() #fecha o comando da função.
'''
#with open(lista, 'r') as lista: r = repeat; rt = repetir texto.
#with open(lista) as lista:  
    #conteudo = lista.readline() # ler a linha.

#print(conteudo)


