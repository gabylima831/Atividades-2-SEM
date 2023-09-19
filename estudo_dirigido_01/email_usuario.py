# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.

import re 

email_do_usuario = input("Digite seu email: ")

def email_valido(email):
    if "@" in email:    
        return True
    else:
        return False

print(email_valido(email_do_usuario))