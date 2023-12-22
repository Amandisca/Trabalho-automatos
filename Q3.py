class TransdutorMoeda:
    def __init__(self):
        self.estado_atual = 0  # Estado inicial
        self.saida = 0  # Saída inicial

    def processar_moeda(self, moeda):
        if moeda == 25:
            self.estado_atual += 25
        elif moeda == 50:
            self.estado_atual += 50
        elif moeda == 100:
            self.estado_atual += 100

        # Verifica se uma lata de refrigerante deve ser liberada
        if self.estado_atual >= 100:
            self.estado_atual -= 100
            self.saida = 1
        else:
            self.saida = 0

        return self.saida

# Exemplo de uso
transdutor = TransdutorMoeda()

# Sequência de moedas
sequencia_moedas = [50, 25, 50, 100, 25, 50, 100, 100, 50, 50, 25, 50, 25]

# Processamento da sequência
saidas = [transdutor.processar_moeda(moeda) for moeda in sequencia_moedas]

# Exibir resultados
print("Sequência de Entrada:", sequencia_moedas)
print("Sequência de Saída:", saidas)