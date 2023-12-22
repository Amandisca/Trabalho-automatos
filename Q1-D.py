class Automato:
    def __init__(self):
        self.estado_atual = 'q0'
        self.estados_finais = {'q1', 'q3'}
        
    def transicao(self, simbolo):
        #linguagem: a*b*(a | ac*)
        #transições q0
        if self.estado_atual == 'q0' and simbolo == 'a':
            self.estado_atual = 'q1'
        if self.estado_atual == 'q0' and simbolo == 'b':
            self.estado_atual = 'q2'

        #transições q1
        elif self.estado_atual == 'q1' and simbolo == 'a':
            self.estado_atual = 'q1'
        elif self.estado_atual == 'q1' and simbolo == 'b':
            self.estado_atual = 'q2'
        elif self.estado_atual == 'q1' and simbolo == 'c':
            self.estado_atual = 'q3'

        #transições q2
        elif self.estado_atual == 'q2' and simbolo == 'b':
            self.estado_atual = 'q2'
        elif self.estado_atual == 'q2' and simbolo == 'a':
            self.estado_atual = 'q3'
        
        #transições q3
        elif self.estado_atual == 'q3' and simbolo == 'c':
            self.estado_atual = 'q3'

        else:
            # Estado de erro, caso um símbolo não seja reconhecido
            self.estado_atual = 'erro'
            
    def processar_cadeia(self, cadeia):
        for simbolo in cadeia:
            self.transicao(simbolo)
            
        aceito = self.estado_atual
        self.estado_atual = 'q0'
        return aceito in self.estados_finais

# Exemplo de uso
automato = Automato()
cadeia1 = ''
cadeia2 = 'a'
cadeia3 = 'aabbaccc'
cadeia4 = 'ccac'
cadeia5 = 'babac'

resultado1 = automato.processar_cadeia(cadeia1)
resultado2 = automato.processar_cadeia(cadeia2)
resultado3 = automato.processar_cadeia(cadeia3)
resultado4 = automato.processar_cadeia(cadeia4)
resultado5 = automato.processar_cadeia(cadeia5)

print(f'A cadeia "{cadeia1}" é aceita? {resultado1}')
print(f'A cadeia "{cadeia2}" é aceita? {resultado2}')
print(f'A cadeia "{cadeia3}" é aceita? {resultado3}')
print(f'A cadeia "{cadeia4}" é aceita? {resultado4}')
print(f'A cadeia "{cadeia5}" é aceita? {resultado5}')
