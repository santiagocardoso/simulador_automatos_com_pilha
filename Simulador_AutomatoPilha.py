'''
    Trabalho final de LFA

    Alunos:
        Santiago Cardoso
        Lucas Gabriel
'''

class Transicao:
    def __init__(self, simbolo_lido, simbolo_topo_retirar, simbolo_colocar, estado):
        self.simbolo_lido = simbolo_lido
        self.simbolo_topo_retirar = simbolo_topo_retirar
        self.simbolo_colocar = simbolo_colocar
        self.estado = estado

class Estado:
    def __init__(self, nome, Transicoes, pilha):
        self.nome = nome
        self.Transicoes = Transicoes
        self.pilha = pilha
        
    def get_transicoes(self):
        return self.Transicoes
        

class Automato_pilha:
    
    def __init__(self, estado_inicial, estados, estado_final, entrada, pilha):
        self.estado_inicial = estado_inicial
        self.estados = estados
        self.estado_final = estado_final
        self.entrada = entrada
        self.pilha = pilha
        
    def ler_entrada(self):
    
        transicoes_atuais = self.estado_inicial.Transicoes
        for letra in self.entrada:
            
            for transicao in transicoes_atuais:
                if transicao.simbolo_lido == letra and (self.pilha[-1] == transicao.simbolo_topo_retirar):
                    self.pilha.pop(-1)
                    
                    for i in range(len(transicao.simbolo_colocar)):
                        self.pilha.append(transicao.simbolo_colocar[len(transicao.simbolo_colocar)-i-1])
                        
                    
                    break
                    
            proximo_estado = transicao.estado
            for estado in self.estados:
                if proximo_estado == estado.nome:
                    transicoes_atuais = estado.Transicoes
            
            
                            
        
        if proximo_estado == self.estado_final.nome and len(self.pilha)==0:
            print(f"palavra aceita\nPilha = {self.pilha}")
                    
                    
            
                
            
            
        
        

entrada = "abbcbba"
pilha = [""]
vazio = ""

TransicoesQ0 = [Transicao('a', vazio, 'a','Q0'), Transicao('b', vazio, 'b','Q0'), Transicao('a', 'a', "aa",'Q0'), Transicao('a', 'b', "ab",'Q0'), Transicao('b', 'b', "bb",'Q0'), Transicao('b', 'a', "ba",'Q0'), Transicao('c', vazio, vazio,'Q2'), Transicao('c', 'a', 'a','Q2'), Transicao('c', 'b', 'b','Q2')]
Q0 = Estado("Q0", TransicoesQ0 , pilha)
Q2 = Estado("Q2", [Transicao('a', 'a', vazio,'Q2'), Transicao('b', 'b', vazio,'Q2')], pilha)

#Q0 = Estado("Q0", Transicao('a', vazio, 'a', 'Q0'))
#Q1 = Estado('Q1', Transicao('a','a',vazio,'Q1',)
automato = Automato_pilha(Q0, [Q0,Q2], Q2, entrada, pilha)
automato.ler_entrada()

#FALTA FAZER COM AFN





