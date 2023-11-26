#Dicionário (coleções)
#Lista
#Tupla
#String
"""
import array as ar

obj = ar.array('i',[1,2,3])
print(type(obj),obj)
print(obj[0])
print(obj[1:]) #slice = "fatia" o número selecionado.

obj2 = ar.array('u','YESGO')
print(type(obj2), obj2)
obj2[0] = 'I' #se a string estiver errada, substitui a letra certa.
print (obj2)

obj3 = ar.array('d', [1.233, 1.2334, 3.3])
print(type(obj3), obj3)
"""

import array as arr

#Criar um array de inteiros vazio:
meu_array = arr.array ('i')

#Adicionar cinco ao array:
for i in range(5): #range = gera 5 números aleatórios.
    num = int(input("Insira um número inteiro: "))
    meu_array.append(num)

print("Array resultante: ", meu_array)

#Somar os números do array:
print(sum(meu_array)) #sum = soma os número da lista.

nome = "Estevan"
sobrenome = "Ferreira"
print(nome, sobrenome) #vírgula separa; "+" une as palavras.

#Encontrar o mínimo e o máximo:
min_valor = min(meu_array)
max_valor = max(meu_array)
print(f'O menor valor é: {min_valor}\nO maior valor é: {max_valor}')    

#Remover o último elemento:
print(meu_array)
meu_array.pop() #pop = remove um elemento.
print("Removido o último elemento", meu_array)

#Inverter a ordem:
meu_array.reverse() #reverse = inverte a ordem da lista.
print("lista invertida: ", meu_array)