import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

#Criar o banco de dados SQLite e a tabela de usuários:
conn = sqlite3.connect('banco_usuario.db')
cursor = conn.cursor()
cursor.execute( #c
    '''
    CREATE TABLE IF NOT EXISTS users( 
        id INTERGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, email TEXT NOT NULL
    )
    '''
)
conn.commit() #fecha dados do banco.

#Aplicação de gestão dos usuários:
class AppGestaodeUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Gestão de Usuários - Versão 0.0.1")
        self.tree = ttk.Treeview(root, columns=('ID', 'Nome de usuário', 'Email'), show='headings') #cria a tabela onde pode inserir colunas.
        self.tree.heading('ID', text='ID')
        self.tree.heading('username', text='Usuário')
        self.tree.heading('email', text='Email')
        self.tree.pack(padx=10, pady=10) #margem da janela.

        self.load_data() #carrega todos os dados que estiverem no banco.

        adicionar_botao = tk.Button(root, text='Adicionar', command=self.show_add_user_window) #mostrar janela do usuário.
        adicionar_botao.pack(pady=10)

        deletar_botao = tk.Button(root, text='Remover', command=self.delete_user) #deletar usuário.
    
    def carregar_dados(self):
        #Carregar os dados do banco e exibir no Treeview (janela)
        cursor.execute('SELECT * FROM USERS') #executa o comando SQL./*varre os dados do banco inteiro.
        rows = cursor.fetchall
        for row in rows:
            self.tree.insert('', 'end', values=row) #busca os valores da coluna.

    def mostrar_janela_usuario(self):
        mostrar_janela_usuario = tk.Toplevel(self.root)
        mostrar_janela_usuario.title('Adicionar novo usuário')

        #Criar campos da nova janela:
        username_label = tk.Label(mostrar_janela_usuario, text='Nome do usuário:')
        username_label.grid(row=0, column=0, padx=10, pady=10)
        username_entry = tk.Entry(mostrar_janela_usuario) #entrada de dados do usuário.
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        email_label = tk.Label(mostrar_janela_usuario, text="Email:")
        email_label.grid(row=1, column=0, padx=10, pady=10)
        email_entry = tk.Entry(mostrar_janela_usuario)
        email_entry.grid(row=1, column=1, padx=10, pady=10)

        botao_salvar = tk.Button(mostrar_janela_usuario, text='Salvar', command=lambda: self.botao_salvar(username_entry.get(), email_entry.get(), mostrar_janela_usuario)) #get = buscar elemento.
        botao_salvar.grid(row=2, columnspan=2, pady=10) #columnspan = dá destaque ao botão.

    def salvar_usuario(self, username, email, window):
        #Salvar no banco de dados:
        cursor.execute('INSERT INTO users (username, email) VALUES (?,?)', (username, email)) 
        conn.commit() #Salvar.

        #Update na tabela do aplicativo:
        self.tree.insert('', 'end', values=(cursor.lastrowid, username, email)) #busca no cursor o elemento que é a chave primária.

        #Fecha a janela:
        window.destroy()
    
    #Deletar usuário:
    def deletar_usuario(self):
        item_selecionado = self.tree.selection()
        if item_selecionado:
            id_usuario = self.tree.item(item_selecionado)['values'][0]
            cursor.execute('DELETE FROM users, WHERE id=?', (id_usuario))
            conn.commit()

            #Apagar da janela (treeview)
            self.tree.delete(item_selecionado)
        else:
            messagebox.showerror('Erro', 'Selecione um usuário para remover da lista')

if __name__=='__main__':
        root = tk.Tk()
        app = AppGestaodeUsuario(root)
        root.mainloop()

        #Fechar o banco:
        conn.close()



