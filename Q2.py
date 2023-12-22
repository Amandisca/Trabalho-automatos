class Automato:
    def __init__(self):
        self.estado_atual = 'q1'


# a função de transição teve que ser colocada dentro da "processar cadeia" para possibiltar o funcionamento do contador.
        
    def processar_cadeia(self, cadeia):
        self.estado_atual = 'q1'
        contador = 0
        ocorrencias = []
        for simbolo in cadeia:
            #linguagem: computador
            if self.estado_atual == 'q1' and simbolo == 'c':
                self.estado_atual = 'q2'
            elif self.estado_atual == 'q2' and simbolo == 'o':
                self.estado_atual = 'q3'
            elif self.estado_atual == 'q3' and simbolo == 'm':
                self.estado_atual = 'q4'
            elif self.estado_atual == 'q4' and simbolo == 'p':
                self.estado_atual = 'q5'
            elif self.estado_atual == 'q5' and simbolo == 'u':
                self.estado_atual = 'q6'
            elif self.estado_atual == 'q6' and simbolo == 't':
                self.estado_atual = 'q7'
            elif self.estado_atual == 'q7' and simbolo == 'a':
                self.estado_atual = 'q8'
            elif self.estado_atual == 'q8' and simbolo == 'd':
                self.estado_atual = 'q9'
            elif self.estado_atual == 'q9' and simbolo == 'o':
                self.estado_atual = 'q10'
            elif self.estado_atual == 'q10' and simbolo == 'r':
                self.estado_atual = 'q11'
            elif self.estado_atual == 'q11' and simbolo == ' ':
                self.estado_atual = 'q1'
                ocorrencias.append((contador-10))

            elif simbolo == ' ':
                self.estado_atual = 'q1'

            else:
            # Estado de erro, caso um símbolo não seja reconhecido
                self.estado_atual = 'erro'
        
        
            contador = contador + 1
            
            
        self.estado_atual = 'q0'
        return ocorrencias


# Texto de entrada
Texto = "O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico"
automato = Automato()

# Encontrar ocorrências
ocorrencias = automato.processar_cadeia(Texto)
tamanho = len(ocorrencias)

# Exibir resultados
if ocorrencias:
    print(f'A palavra foi encontrada {tamanho} vezes.')
    print(f'Ocorrências da palavra "computador" nas posições: {ocorrencias}')
else:
    print(f'A palavra não foi encontrada no texto.')