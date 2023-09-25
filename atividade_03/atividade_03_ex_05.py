#Lista de Tarefas:
### Desenvolva um aplicativo de lista de tarefas que permita ao usuário adicionar, marcar como concluída e remover tarefas.
### Bônus: armazene a lista de tarefas em um arquivo e carregue-a quando o aplicativo for iniciado.

tarefas = {}
def adicionar_tarefa():
  tarefa = input('Digite a tarefa que deseja adicionar: ')
  tarefas[tarefa] = False 
def marcar_como_concluida():
  tarefa = input('Digite a tarefa que deseja marcar como concluída: ')
  if tarefa in tarefas:
    tarefas[tarefa] = True
    print(f'{tarefa} foi marcada como concluída.')
  else:
    print('Tarefa não encontrada na lista.')

def remover_tarefa():
  tarefa = input('Digite a tarefa que desej remover: ')
  if tarefa in tarefas:
    del tarefas[tarefa]
    print(f'{tarefa} foi removida da lista de tarefas.')
  else: 
    print('Tarefa não encontrada na lista.')

def listar_tarefas():
  print('Lista de Tarefas:')
  for tarefa, concluida in tarefas.items():
    status = 'Concluída' if concluida else 'Pendente'
    print(f'{tarefa} - Status: {status}')

while True:
  print('\nOpções:')
  print('1 - Adicionar tarefa')
  print('2 - Marcar tarefa como concluída')
  print('3 - Remover tarefa')
  print('4 - Listar tarefas')
  print('5 - Sair')

  opcao = input('Escolha uma opção: ')

  if opcao == '1':
    adicionar_tarefa()
  elif opcao == '2':
    marcar_como_concluida()
  elif opcao == '3':
    remover_tarefa()
  elif opcao == '4':
    listar_tarefas()
  elif opcao == '5':
    break
  else:
    print('Opção inválida! Tente novamente.')
  (quit)