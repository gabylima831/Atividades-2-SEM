'''
import sqlite3
def criar_tabela():
  #Conectar ao banco
  connection = sqlite3.connect('dados_usuarios.db')
  cursor = connection.cursor()

  #Criar a tabela se não existir:
  cursor.execute('''
    #CREATE TABLE IF NOT EXISTS usuarios(
      #id INTEGER PRIMARY KEY AUTOINCREMENT,
      #nome TEXT NOT NULL,
      #email TEXT NOT NULL,
      #idade INTEGER NOT NULL
    #)             
''')

  connection.commit()
  connection.close()
criar_tabela()

def visualizar_lista():
  connection = sqlite3.connect('dados_usuarios.db')
  cursor = connection.cursor()

  #Selecionar registros da tabela:
  cursor.execute('SELECT * FROM usuarios')
  rows = cursor.fetchall()

  print("\n Lista de usuários:")
  for row in rows:
    print(row)

  connection.close()
def adicionar_membro():
  nome = input('Digite seu nome: ')
  email = input('Digite o email: ')
  idade = int(input('Digite sua idade: '))

  connection = sqlite3.connect('dados_usuarios.db')
  cursor = connection.cursor()

  #Inserir novo registro:
  cursor.execute('INSERT INTO usuarios (nome, email, idade) VALUES (?,?,?)', (nome, email, idade))

  connection.commit()
  connection.close()

  print(f'\n Usuário: {nome} adicionado com sucesso!')

def remover_membro():
  id_remover = int(input('Digite o ID do usuário a ser removido: '))

  connection = sqlite3.connect('dados_usuarios.db')
  cursor = connection.cursor()

  #Remover o registro com base no ID:
  cursor.execute('DELETE FROM usuarios WHERE id = ?', ({id_remover}))

  connection.conmit()
  connection.close()

  print(f'\n Usuários com ID ({id_remover}) foi removido com sucesso!')

if __name__ == "__main__":
  criar_tabela()

  while True:
    print("\n ESCOLHA UMA OPÇÃO:")
    print("1. Visualizar lista")
    print("2. Adicionar membro")
    print("3. Remover membro")
    print("4. Sair")

    escolha = input('Opção: ')

    if escolha == "1":
      visualizar_lista()
    elif escolha == "2":
      adicionar_membro()
    elif escolha == "3":
      remover_membro()
    elif escolha == "4":
      print("Saindo do sistema...")               
      break
    else:
      print("Opção inválida, tente novamente.")

def buscar_usuario():
  cursor.execute("SELECT * FROM usuarios"
)
rows = cursor.fetchall()
for row in rows: #linhas.
  print(row) #imprimir linhas da tabela.

connection.commit() #fechar a conexão.
connection.close()
'''