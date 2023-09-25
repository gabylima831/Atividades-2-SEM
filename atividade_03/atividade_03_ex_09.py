#Calculadora de IMC (Índice de Massa Corporal):
### Crie uma calculadora que permite ao usuário calcular seu IMC com base em seu peso e altura.
### Bônus: responda se o usuário está acima, abaixo ou dentro do peso ideal.

def calculadora_imc():
  peso = float (input('Digite o seu peso em kg: '))
  altura = float (input('Digite sua altura aqui: '))
  conta = peso/(altura * altura)
  imc = '{:.2f}'.format(conta)
  if float(imc) <= 16:
    return 'Magreza grave', 'Seu IMC é: ', imc
  elif 16 < float(imc) <= 17:
    return 'Magreza moderada', 'Seu IMC é: ', imc
  elif 17 < float(imc) <= 18.5:
    return 'Magreza leve', 'Seu IMC é: ', imc
  elif 18.5 < float(imc) <= 25:
    return 'Saudável', 'Seu IMC é: ', imc
  elif 25 < float(imc) <= 30:
    return 'Sobrepeso', 'Seu IMC é: ', imc
  elif 30 < float(imc) <= 35:
    return 'Obesidade grau 1', 'Seu IMC é: ', imc
  elif 35 < float(imc) <= 40:
    return 'Obesidade grau 2', 'Seu IMC é: ', imc
  elif float(imc) >= 40:
    return 'Obesidade grau 3', 'Seu IMC é: ', imc
  else:
    return 'IMC fora da faixa.'
resultado = calculadora_imc()
print(resultado)