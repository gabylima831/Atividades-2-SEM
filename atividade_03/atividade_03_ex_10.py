# Agenda Telefônica:
### Desenvolva um aplicativo de agenda telefônica que permita ao usuário adicionar, pesquisar, editar e excluir contatos.
### Bônus: armazene a agenda telefônica em um arquivo e carregue-a quando o aplicativo for iniciado.

def adicionar(lista):
 pass
def pesquisar():
  pass
def editar():
  pass
def excluir():
  pass
def principal():
  while True:
    print('=== Agenda Telefônica ===')
    print('1 - Adicionar contato')
    print('2 - Pesquisar contato')
    print('3 - Editar contato')
    print('4 - Excluir contato')
    opção = int(input('Selecione uma opção: '))
  
    if opção == 1:
      adicionar()
    elif opção == 2:
      pesquisar()
    elif opção == 3:
      editar()
    elif opção == 4:
      excluir()
      break
    else:
      print('Opção inválida. Por favor, tente novamente.')
principal()

