"""
import tkinter as tk 

def mostrar_mensagem():
    label.config(text="Olá, IESGO!")

#Criar uma janela:
janela = tk.Tk() #busca na biblioteca
janela.title("Exemplo de Interface Gráfica de Usuário (GUI) em Python") #título

#Criar um rótulo:
label = tk.Label(janela, text="Bem-vindo à Interface Gráfica de Usuário (GUI)") #label = legenda; Label = classe.
label.pack(padx=10, pady=10) #tamanho da janela

#Criar um botão tipo CTA (Call to action/Chamada para ação):
botao = tk.Button(janela, text="Clique aqui!", command= mostrar_mensagem) 
botao.pack(padx=10, pady=10) #tamanho do botão


#Iniciar a Interface Gráfica do Usuário em loop:
janela.mainloop()
"""

import tkinter as tk
from tkinter import messagebox
#import pesquisar_produto



def abrir_janela(mensagem):
    nova_janela = tk.Toplevel()
    nova_janela.title("Ação qualquer...")

    label = tk.Label(nova_janela, text=mensagem, padx=20, pady=20)
    label.pack()

    botao_fechar = tk.Button(nova_janela, text="Sair", command=nova_janela.destroy)
    botao_fechar.pack(padx=20, pady=10)

#Funções para as diferentes funcionalidades do sistema ERP:

def pesquisar_produto():
    abrir_janela("Pesquisar produto")

def checar_estoque():
    abrir_janela("Checar estoque")

def acrescentar_estoque():
    abrir_janela("Acrescentar estoque")

def remover_estoque():
    abrir_janela("Remover estoque")

def cadastrar_produto():
    abrir_janela("Cadastrar produto")

#Criar a janela principal:

janela_principal = tk.Tk()
janela_principal.title("SISTEMA ERP IESGO")
janela_principal.attributes("-fullscreen", True)
#janela_principal.attributes("-topmost", True)
#janela_principal.attributes("-disabled", False)
#janela_principal.attributes("-zoomed", True)


#Configurar ícones no menu:
icon_pesquisar = tk.PhotoImage(file="/media/lab03/66D8-6C9A/Python/Aula 0611/pesquisar_produto.png")
icon_acrescentar_estoque = tk.PhotoImage(file="/media/lab03/66D8-6C9A/Python/Aula 0611/acrescentar_estoque.png")
icon_checar_estoque = tk.PhotoImage(file="/media/lab03/66D8-6C9A/Python/Aula 0611/checar_estoque.png")
icon_cadastrar_produto = tk.PhotoImage(file="/media/lab03/66D8-6C9A/Python/Aula 0611/cadastrar_produto.png")
icon_remover_estoque = tk.PhotoImage(file="/media/lab03/66D8-6C9A/Python/Aula 0611/remover_estoque.png")

#Criar os botões com ícones:
botao_pesquisar = tk.Button(janela_principal, image=icon_pesquisar, command=pesquisar_produto)
botao_acrescentar_estoque = tk.Button(janela_principal, image=icon_acrescentar_estoque, command=acrescentar_estoque)
botao_checar_estoque = tk.Button(janela_principal, image=icon_checar_estoque, command=checar_estoque)
botao_cadastrar_produto = tk.Button(janela_principal, image=icon_cadastrar_produto, command=cadastrar_produto)
botao_remover_estoque= tk.Button(janela_principal, image=icon_remover_estoque, command=remover_estoque)

#Exibir os botões na janela:
botao_pesquisar.pack()
botao_acrescentar_estoque.pack()
botao_checar_estoque.pack()
botao_cadastrar_produto.pack()
botao_remover_estoque.pack()

#Loop na janela principal:
janela_principal.mainloop()
