"""
Exercício 1.1: Sistema de Biblioteca

Contexto:
Você foi contratado para criar um simples sistema de gerenciamento para uma pequena biblioteca. Os requisitos iniciais são criar um programa que permita ao 
usuário gerenciar livros e membros da biblioteca.

Requisitos:

A biblioteca deve ser capaz de armazenar informações sobre os livros, como título, autor e status (emprestado ou disponível).
A biblioteca deve também ser capaz de armazenar informações sobre os membros, como nome e os livros que eles emprestaram.
Implemente funcionalidades para adicionar livros, emprestar livros a membros e retornar livros.

Instruções:

Crie uma classe chamada Livro que tenha os seguintes atributos: titulo, autor e status. Por padrão, todos os livros devem ter o status "disponível".

Crie uma classe chamada Membro que tenha os seguintes atributos: nome e livros_emprestados (uma lista).

Crie uma classe chamada Biblioteca que tenha os seguintes atributos: livros (um dicionário com o título do livro como chave e a instância do livro como valor) 
e membros (um dicionário com o nome do membro como chave e a instância do membro como valor).

Na classe Biblioteca, crie os seguintes métodos:

adicionar_livro(self, livro): Adiciona um livro ao dicionário de livros.
registrar_membro(self, membro): Adiciona um membro ao dicionário de membros.
emprestar_livro(self, titulo_livro, nome_membro): Empresta um livro para um membro se o livro estiver disponível.
retornar_livro(self, titulo_livro, nome_membro): Retorna um livro que estava emprestado.


Desafio:

Adicione funcionalidades para remover livros ou membros.
Implemente uma busca para encontrar um livro ou membro por nome.
Dicas:

Use dicionários para armazenar livros e membros na classe Biblioteca para fácil acesso.
Ao emprestar um livro, atualize o status do livro e a lista de livros emprestados do membro.
Ao retornar um livro, faça o processo inverso do empréstimo.
"""
class Livro:
    def __init__ (self, titulo, autor): #init = início da função. (autoreferência) / self = si mesmo - dentro do objeto.
        self.titulo = titulo
        self.autor = autor
        self.status = 'Disponível'      

    def __str__(self):
        return f'Título: {self.titulo}\n Autor: {self.autor}\n Status: {self.status}\n.'
    
class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:

    titulo_livro = {
        'A canção de Aquiles': 'Madeline Miller',
        'O sinal dos quatro': 'Arthur Conan Doyle', 'Um estudo em vermelho': 'Arthur Conan Doyle','Tudo é rio': 'Mariana Rios',
        'O silêncio dos inocentes': 'Thomas Harris', 'O pequeno príncipe': 'Antoine Saint Èxupery'
    }

    nome_membros = {
        'Fulano',
        'Ciclano',
        'Beltrano',
        'Irineu',
        'Zumira',
    }

    def __init__(self):         
        self.livros = titulo_livro
        titulo_livro = {}    
        self.membros = nome_membros
        nome_membros = {}

    def adicionar_livro(self): #exibir_informacoes = método(ação).
        self.titulo_livro = {}.append('Belas Maldições')
           
    def registrar_membro(self):
        self.nome_membros = {}.append('Muriel')
                           
    def emprestar_livro(self):
        if self.titulo_livro == 'Disponível':
            return f'Título: {self.titulo_livro}\n Membro: {self.nome_membros}\n Este livro está disponível.'

    def retornar_livro(self): 
        self.titulo_livro = {}
        self.nome_membro = {}
        return f'Título: {self.titulo_livro}\n Membro: {self.nome_membros}\n.'
        
membro1 = Livro ('A canção de Aquiles', 'Madeline Miller') #instância = armazena elementos dentro de uma classe.

#print(membro1)
#print(resultado)
#print(membro1.adicionar_livro())
#resultado = Biblioteca(dict(titulo_livro))
#resultado = Biblioteca.titulo_livro[0]
