# Exercício 7: Faça um programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo (divisível entre 0 e ele mesmo).

def numero_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    else:
        for num in range(2, numero):
            if numero % num == 0:
                return False
        return True
    
numero = int(input("Digite um número inteiro: ")) 
print(numero_primo(numero))
