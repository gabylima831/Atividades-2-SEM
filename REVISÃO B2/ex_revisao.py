"""
Exercício Revisão I: Sistema de Gerenciamento de Livros
Considere um sistema de gerenciamento de livros com uma tabela livros que tem os seguintes campos:

id (Chave Primária, Integer)
titulo (Texto)
autor (Texto)
ano_publicacao (Integer)

Você deve criar uma aplicação via terminal para gerenciar essa biblioteca.  Você deve atentar para o seguinte:
@@@ Criar o banco de dados:

Nome do banco de dados: biblioteca.db

@@@ Criar a tabela livros:

Campos: id (autoincremento), titulo (texto), autor (texto), ano_publicacao (inteiro)

@@@ Inserir alguns livros na tabela:

Inserir pelo menos 3 livros diferentes com informações fictícias.
Permitir que o usuário insira novos títulos

@@@ Consultar todos os livros:

Selecionar e exibir todos os livros presentes na tabela.

@@@ Remover livro

O usuário poderá remover um livro da lista

Seu sistema deverá ser operado no terminal e deverá conter um menu em loop

"""
import sqlite3
def criar_tabela():
  #Conectar ao banco:
  connection = sqlite3.connect('biblioteca.db')
  cursor = connection.cursor()

  #Criar tabela de livros:
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros(
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      titulo TEXT NOT NULL, 
      autor TEXT NOT NULL,
      ano_publicacao INTEGER NOT NULL
    )  
  ''')

  connection.commit()
  connection.close()


#Inserir dados na tabela:
def inserir_livros(titulo, autor, ano_publicacao):
  titulo = input('Digite o nome do livro: ')
  autor = input('Digite o nome do autor: ')
  ano_publicacao = int(input('Digite o ano de publicação: '))

  connection = sqlite3.connect('biblioteca.db')
  cursor = connection.cursor()

  #Inserir novos livros:
  cursor.execute('INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?,?,?)', (titulo, autor, ano_publicacao))
  
  connection.commit()
  connection.close()
  
  print(f'\n Livro {titulo} de {autor} de {ano_publicacao} adicionado com sucesso!')
inserir_livros('A canção de Aquiles', 'Madeline Miller', 2015) 

#Fazer consulta:
def consultar_livros():
  connection = sqlite3.connect('biblioteca.db')
  cursor = connection.cursor()
  #Consultar todos os livros:
  cursor.execute("SELECT * FROM livros")
  rows = cursor.fetchall()

  print('\n Lista de livros: ')
  for row in rows:
    print(row)

  connection.close()

#Remover livros:
def remover_livro():
  id_remover = int(input('Digite o ID do livro a ser removido: '))

  connection = sqlite3.connect('biblioteca.db')
  cursor = connection.cursor()

  cursor.execute('DELETE FROM livros WHERE id = ?', 
  ({id_remover}))

  connection.commit()
  connection.close()

  print(f'\n Livro com ID ({id_remover}) foi removido com sucesso!')

#Menu:
if __name__ == '__main__':
  criar_tabela()

  while True:
    print('\n ESCOLHA UMA OPÇÃO:')
    print('1. Inserir livro')
    print('2. Consultar livros')
    print('3. Remover livro')
    print('4. Sair da biblioteca')

    escolha = input('Opção: ')

    if escolha == '1':
      inserir_livros()
    elif escolha =='2':
      consultar_livros()
    elif escolha == '3':
      remover_livro()
    elif escolha == '4':
      print('Saindo do sistema...')
      break
    else:
      print('Opção inválida, tente novamente.')


