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
        self.aceita = False
        
        
    def ler_entrada(self):
    
        transicoes_atuais = self.estado_inicial.Transicoes
        contaLetras = 0
        for letra in self.entrada:
            contaLetras+=1
            MovimentoVazio = False
            
            for transicao in transicoes_atuais:
                if transicao.simbolo_lido == "":
                    MovimentoVazio = True
                    
            
            if MovimentoVazio:
                nova_entrada = self.entrada[contaLetras-1:] 
                novaPilha = self.pilha.copy()
                
                for estado in self.estados:
                    if transicao.estado == estado.nome:
                        novo_Estado_inicial = estado
                
                novoAutomato = Automato_pilha(novo_Estado_inicial, self.estados, self.estado_final, nova_entrada, novaPilha)
                novoAutomato.ler_entrada()
                if(novoAutomato.aceita):
                    self.aceita = True
                    return
            
            for transicao in transicoes_atuais:
                
                #nao retira nada do topo mas coloca alguma coisa na pilha
                if transicao.simbolo_lido == letra and transicao.simbolo_topo_retirar=="":
                    self.pilha.append(transicao.simbolo_colocar)
                    break
                    
            
                #nem retira nem coloca nada, so le a entrada
                elif transicao.simbolo_topo_retirar=="" and transicao.simbolo_colocar=="":
                    break
                    
                elif len(self.pilha)==0 and transicao.simbolo_topo_retirar!="":
                    return
                
                #so retira e nao coloca nada na pilha
                elif transicao.simbolo_lido == letra and self.pilha[-1] == transicao.simbolo_topo_retirar and transicao.simbolo_colocar=="":
                    self.pilha.pop()
                    break
                    
                
                #retira algo e coloca algo
                elif transicao.simbolo_lido == letra and self.pilha[-1] == transicao.simbolo_topo_retirar:
                    self.pilha.pop()
                    self.pilha.append(transicao.simbolo_colocar)
                    break
                
                elif transicao == transicoes_atuais[-1]:
                    return
                
                    
            proximo_estado = transicao.estado
            for estado in self.estados:
                if proximo_estado == estado.nome:
                    transicoes_atuais = estado.Transicoes
                            
        
        if proximo_estado == self.estado_final.nome and len(self.pilha)==0 and contaLetras == len(self.entrada):
            print(f"palavra aceita\nPilha = {self.pilha}")
            self.aceita = True
            return
            
        
        


pilha = []
vazio = ""

'''
entrada = "abbcbba"
TransicoesQ0 = [Transicao('a', vazio, 'a','Q0'), Transicao('b', vazio, 'b','Q0'), Transicao('a', 'a', "aa",'Q0'), Transicao('a', 'b', "ab",'Q0'), Transicao('b', 'b', "bb",'Q0'), Transicao('b', 'a', "ba",'Q0'), Transicao('c', vazio, vazio,'Q2'), Transicao('c', 'a', 'a','Q2'), Transicao('c', 'b', 'b','Q2')]
Q0 = Estado("Q0", TransicoesQ0 , pilha)
Q2 = Estado("Q2", [Transicao('a', 'a', vazio,'Q2'), Transicao('b', 'b', vazio,'Q2')], pilha)
'''

Q0 = Estado("Q0", [Transicao('a', vazio, 'a', 'Q0'), Transicao('b',vazio, 'b', 'Q0'), Transicao(vazio, vazio, vazio, 'Q1')],pilha)
Q1 = Estado('Q1', [Transicao('a','a',vazio,'Q1'),Transicao('b', 'b', vazio, 'Q1')],pilha)
entrada = 'aaaa'

'''
entrada = "aaabbb"
Q0 = Estado("Q0",[Transicao('a', vazio, 'a', 'Q0'), Transicao('b', 'a', vazio, 'Q1')],pilha)
Q1 = Estado("Q1",[Transicao('b', 'a', vazio, 'Q1')],pilha)
'''

automato = Automato_pilha(Q0, [Q0,Q1], Q1, entrada, pilha)
automato.ler_entrada()

if(not automato.aceita):
    print("Palavra nao aceita")


#FALTA FAZER COM AFN





