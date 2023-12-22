class Automato:
    def __init__(self):
        self.estado_atual = 'q0'
        self.estados_finais = {'q1', 'q2', 'q4'}
        
    def transicao(self, simbolo):
        #linguagem: a*b | ab*
        #transições q0
        if self.estado_atual == 'q0' and simbolo == 'a':
            self.estado_atual = 'q1'
        elif self.estado_atual == 'q0' and simbolo == 'b':
            self.estado_atual = 'q2'

        #transições q1
        elif self.estado_atual == 'q1' and simbolo == 'a':
            self.estado_atual = 'q3'
        elif self.estado_atual == 'q1' and simbolo == 'b':
            self.estado_atual = 'q4'

        #transições q2 = inexistentes
        
        #transições q3
        elif self.estado_atual == 'q3' and simbolo == 'a':
            self.estado_atual = 'q3'
        elif self.estado_atual == 'q3' and simbolo == 'b':
            self.estado_atual = 'q2'

        #transições q4
        elif self.estado_atual == 'q4' and simbolo == 'b':
            self.estado_atual = 'q4'

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
cadeia2 = 'abbbbb'
cadeia3 = 'aaaaaaab'
cadeia4 = 'abba'
cadeia5 = 'bb'

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