class Carro:
    def __init__(self, numero_chassi, numero_motor, custo_producao):
        self.numero_chassi = numero_chassi
        self.numero_motor = numero_motor
        self.custo_producao = custo_producao
        self.imposto = 0.20  # Imposto padrão de 20%
        self.lucro = 0.25  # Lucro da fábrica de 25%

    def calcular_custo_venda(self):
        imposto_valor = self.custo_producao * self.imposto
        lucro_valor = self.custo_producao * self.lucro
        return self.custo_producao + imposto_valor + lucro_valor

class CarroFlex(Carro):
    def __init__(self, numero_chassi, numero_motor, numero_portas, cilindrada, custo_producao):
        super().__init__(numero_chassi, numero_motor, custo_producao)
        self.numero_portas = numero_portas
        self.cilindrada = cilindrada

class CarroDiesel(Carro):
    def __init__(self, numero_chassi, numero_motor, capacidade_carga, volume_cacamba, custo_producao):
        super().__init__(numero_chassi, numero_motor, custo_producao)
        self.capacidade_carga = capacidade_carga
        self.volume_cacamba = volume_cacamba
        self.imposto = 0.30  # Imposto de 30% para carros a diesel

class CarroEletrico(Carro):
    def __init__(self, numero_chassi, numero_motor, potencia, duracao_bateria, custo_producao):
        super().__init__(numero_chassi, numero_motor, custo_producao)
        self.potencia = potencia
        self.duracao_bateria = duracao_bateria
        self.imposto = 0.10  # Imposto de 10% para carros elétricos

# Exemplo de uso
carro_flex = CarroFlex("123ABC", "456DEF", 4, 1.6, 50000)
carro_diesel = CarroDiesel("789GHI", "012JKL", 1000, 2.5, 70000)
carro_eletrico = CarroEletrico("345MNO", "678PQR", 150, 300, 80000)

print(f"Custo de venda do carro flex: {carro_flex.calcular_custo_venda()}")
print(f"Custo de venda do carro diesel: {carro_diesel.calcular_custo_venda()}")
print(f"Custo de venda do carro elétrico: {carro_eletrico.calcular_custo_venda()}")