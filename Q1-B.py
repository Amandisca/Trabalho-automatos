class Automato:
    def __init__(self):
        self.estado_atual = 'q0'
        self.estados_finais = {'q3', 'q7'}
        
    def transicao(self, simbolo):
        #linguagem: aaa(b | c)* | (b | c)* aaa
        #transições q0
        if self.estado_atual == 'q0' and simbolo == 'a':
            self.estado_atual = 'q1'
        elif self.estado_atual == 'q0' and (simbolo == 'b' or simbolo == 'c'):
            self.estado_atual = 'q4'

        #transições q1
        elif self.estado_atual == 'q1' and simbolo == 'a':
            self.estado_atual = 'q2'

        #transições q2
        elif self.estado_atual == 'q2' and simbolo == 'a':
            self.estado_atual = 'q3'

        #transições q3
        elif self.estado_atual == 'q3' and (simbolo == 'b' or simbolo == 'c'):
            self.estado_atual = 'q3'

        #transições q4
        elif self.estado_atual == 'q4' and (simbolo == 'b' or simbolo == 'c'):
            self.estado_atual = 'q4'
        elif self.estado_atual == 'q4' and simbolo == 'a':
            self.estado_atual = 'q5'
        
        #transições q5
        elif self.estado_atual == 'q5' and simbolo == 'a':
            self.estado_atual = 'q6'

        #transições q6
        elif self.estado_atual == 'q6' and simbolo == 'a':
            self.estado_atual = 'q7'

        #q7 não contem transições

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
cadeia2 = 'aaabcbcbc'
cadeia3 = 'bbccbaaa'
cadeia4 = 'aaaaa'
cadeia5 = 'caa'

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
