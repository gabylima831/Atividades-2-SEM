#Conversor de Temperatura:
### Crie um conversor de temperatura que permita ao usuário converter entre Celsius e Fahrenheit.
### Bônus: permita que o usuário especifique o número de casas decimais que deseja exibir.

def conversor_temperatura():
  valor_usuario = input('Digite o valor que deseja converter: ')
  temperatura_em_F = float (valor_usuario)
  temperatura_em_C = (temperatura_em_F - 32) * (5/9)
  print(temperatura_em_F, 'em Celsius é igual a', temperatura_em_C)
conversor_temperatura()