"""
Crie uma classe chamada Carro que represente diferentes carros em uma revendedora de automóveis. A classe deve ter os seguintes atributos e métodos:
Atributos:
marca: Representa a marca do carro (por exemplo, Toyota, Ford, BMW, etc.).
modelo: Representa o modelo específico do carro.
ano: Representa o ano de fabricação do carro.
preco: Representa o preço do carro.
vendido: Um valor booleano que indica se o carro foi vendido ou não. Por padrão, todos os carros são considerados não vendidos.
Métodos:
exibir_informacoes(): Mostra todas as informações sobre o carro.
vender(): Marca o carro como vendido.
ajustar_preco(novo_preco): Ajusta o preço do carro para o valor especificado.

Instancie pelo menos 5 objetos.
"""
class Carro:

    modelos = {
        'Corolla': 18000,
        'Mustang': 100000,
        'Uno Mille': 1000,
        'Gol G3': 2000,
        'Marea Turbo': 1
    }

    def __init__ (self, marca, modelo, ano, preco): #init = início da função. (autoreferência) / self = si mesmo - dentro do objeto.
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = max(preco, self.modelos.get(modelo,0)) #max = valor máximo.\ self.modelos = para buscar.
        self.vendido = False
    
    def __str__(self): #srt = string.
        return f'O seu carro é um {self.marca} e seu modelo é {self.modelo} do ano {self.ano}.'

    def exibir_informacoes(self): #exibir_informacoes = método(ação).
        if self.vendido == False:
            return f'Marca: {self.marca}\n Modelo: {self.modelo}\n Ano: {self.ano}\n Preço: R$ {self.preco}\n Em estoque.'
        else: 
            return f'Marca: {self.marca}\n Modelo: {self.modelo}\n Ano: {self.ano}\n Preço: R$ {self.preco}\n Fora de estoque.'
        
    def vender(self):
        self.vendido = True
        print(f'Carro {self.marca} vendido!')

    def ajustar_preco(self, novo_preco): 
        preco_minimo = self.modelos.get(self.modelo, 0)
        if novo_preco >= preco_minimo:
            self.preco = novo_preco
        else:
            print(f'Erro! O valor informado é menor que o aceito!. \n O preço mínimo para esse veículo é R$ {preco_minimo}.')
            
        #if self.preco > 20000 and self.ano > 2023:
        #    return(f'O carro pode ser vendido.')
        #else:
        #    return(f'O carro não pode ser vendido.')

carro1 = Carro('Toyota','SUV', 2009, 50000) #instância = armazena elementos dentro de uma classe.
carro2 = Carro('Ford','Picape', 2005, 76388) #instância = armazena elementos dentro de uma classe.
carro3 = Carro('BMW','Sedã', 2016, 18022002) #instância = armazena elementos dentro de uma classe.
carro4 = Carro('Fiat','Uno', 2020, 29133113) #instância = armazena elementos dentro de uma classe.
carro5 = Carro('HB20','Hatch', 2020, 29133113) #instância = armazena elementos dentro de uma classe.

print(carro1.ajustar_preco(12222))
print(carro1.exibir_informacoes())
#print(carro1.preco)
#carro1.preco = 12222
#carro1.ajustar_preco(12345)
