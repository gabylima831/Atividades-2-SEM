# Calculadora de Idade:
### Crie um programa que recebe o ano de nascimento do usuário e calcula a idade atual.
### Bônus: faça o programa retornar o signo do usuário de acordo com o mês e dia do seu nascimento.

def ano_nasc_usuario():
  ano_nasc = int(input('Digite o ano de seu nascimento: '))
  ano_atual = int(2023)
  idade = ano_atual - ano_nasc
  return f'Sua idade atual é {idade} anos.'
print(ano_nasc_usuario())

def signo_usuario():
  mes_nasc = int(input('Digite o mês do seu nascimento: '))
  dia_nasc = int(input('Digite o dia do seu nascimento: '))
  if (mes_nasc == 3 and 21 <= dia_nasc <= 31) or (mes_nasc == 4 and 1 <= dia_nasc <= 19):
    signo = 'Áries'
    print('Seu signo é Áries.')
  elif (mes_nasc == 4 and 20 <= dia_nasc <= 30) or (mes_nasc == 5 and 1 <= dia_nasc <= 20):
    signo = 'Touro'
    print('Seu signo é Touro.')
  elif (mes_nasc == 5 and 21 <= dia_nasc <= 31) or (mes_nasc == 6 and 1 <= dia_nasc <= 20):
    signo = 'Gêmeos'
    print('Seu signo é Gêmeos.')
  elif (mes_nasc == 6 and 21 <= dia_nasc <= 30) or (mes_nasc == 7 and 1 <= dia_nasc <= 22):
    signo = 'Câncer'
    print('Seu signo é Câncer.')
  elif (mes_nasc == 7 and 23 <= dia_nasc <= 31) or (mes_nasc == 8 and 1 <= dia_nasc <= 22):
    signo = 'Leão'
    print('Seu signo é Leão.')
  elif (8 and 23 <= dia_nasc <= 31) or (mes_nasc == 9 and 1 <= dia_nasc <= 22):
    signo = 'Virgem'
    print('Seu signo é Virgem.')
  elif (mes_nasc == 9 and 23 <= dia_nasc <= 31) or (mes_nasc == 10 and 1 <= dia_nasc <= 22):
    signo = 'Libra'
    print('Seu signo é Libra.')
  elif (mes_nasc == 10 and 23 <= dia_nasc <= 31) or (mes_nasc == 11 and 1 <= dia_nasc <= 21):
    signo = 'Escorpião'
    print('Seu signo é Escorpião.')
  elif (mes_nasc == 11 and 22 <= dia_nasc <= 30) or (mes_nasc == 12 and 1 <= dia_nasc <= 21):
    signo = 'Sagitário'
    print('Seu signo é Sagitário.')
  elif (mes_nasc == 12 and 22 <= dia_nasc <= 31) or (mes_nasc == 1 and 1 <= dia_nasc <= 19):
    signo = 'Aquário'
    print('Seu signo é Aquário.')
  elif (mes_nasc == 2 and 19 <= dia_nasc <= 28) or (mes_nasc == 3 and 1 <= dia_nasc <= 20):
    signo = 'Peixes'
    print('Seu signo é Peixes.')
print(signo_usuario())

