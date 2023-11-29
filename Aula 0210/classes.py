""""
class MinhaClasse:
    nome ='Romes'

p1 = MinhaClasse()
print(p1.nome)
"""
class Pessoa:
    def __init__ (self, nome, idade, habilitacao): #init = início da função. (autoreferência) / self = si mesmo - dentro do objeto.
        self.nome = nome
        self.idade = idade
        self.habilitacao = habilitacao
    
    def __str__(self): #srt = string.
        return f'O seu nome é {self.nome} e sua idade é {self.idade}.'

    def maioridade(self): #maioridade = método(ação).
        if self.idade > 17:
            print (f'Você é maior de idade, tem {self.idade} anos nas costas.')
        else: 
            print(f'Você é menor de idade.')
    
    def checagem_habilitacao(self):
        return self.habilitacao 

usuario1 = Pessoa('João', 18, True)
usuario2 = Pessoa('Maria', 33, False) #instância = armazena elementos dentro de uma classe.

print(usuario1.checagem_habilitacao())
print(usuario2.checagem_habilitacao())

usuario2.habilitacao = True
print(usuario2.checagem_habilitacao())

#Pessoa('Enzo', 13).maioridade()
#print(usuario1)
#print(usuario2)
#print(usuario1.idade)
#print(f'O seu nome é {usuario1.nome} e sua idade é {usuario1.idade}.')
#print(Pessoa)