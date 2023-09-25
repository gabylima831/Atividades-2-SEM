#Conversor de Moeda:
###Desenvolva um aplicativo que converte uma quantidade de uma moeda para outra, utilizando taxas de câmbio predefinidas.
### Bônus: faça o programa solicitar ao usuário a moeda de origem e a moeda de destino e a taxa de câmbio.

def converter_moeda():
  valor = float(input('Digite o valor a ser convertido: '))
  taxa_cambio = float(input('Digite a taxa de câmbio: '))
  moeda_origem = input('Digite a moeda de origem (ex.: USD): ').upper()
  moeda_destino = input('Digite a moeda de destino (ex.: EUR): ').upper()
  moeda_convertida = valor * taxa_cambio
  return moeda_convertida

print(converter_moeda())
  