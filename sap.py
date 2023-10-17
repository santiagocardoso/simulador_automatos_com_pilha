'''
    Trabalho final de LFA

    Alunos:
        Santiago Cardoso
        Lucas Gabriel
'''

class Transicao:
    def __init__(self, simbolo_lido, simbolo_topo_retirar, simbolo_colocar, Estado, pilha):
        self.simbolo = simbolo_lido
        self.simbolo_topo_retirar = simbolo_topo_retirar
        self.simbolo_colocar = simbolo_colocar
        self.Estado = Estado
        self.pilha = pilha

class Estado:
    def __init__(self, nome, Transicoes, pilha):
        self.nome = nome
        self.Transicoes = Transicoes


entrada = "abbcbba"
pilha = [""]
vazio = ""

Q0 = Estado("Q0")
Q2 = Estado("Q2")

Q0 = Estado("Q0", [Transicao('a', vazio, 'a', Q0), Transicao('b', vazio, 'b', Q0)], Transicao('a', 'a', "aa", Q0), Transicao('a', 'b', "ab", Q0), Transicao('b', 'b', "bb", Q0), Transicao('b', 'a', "ba", Q0), Transicao('c', vazio, vazio, Q2), Transicao('c', 'a', 'a', Q2), Transicao('c', 'b', 'b', Q2), pilha)

Q2 = Estado("Q2", [Transicao('a', 'a', vazio, Q2), Transicao('b', 'b', vazio, Q2)], pilha)


'''
alfabeto = ['a', 'b']
estados = ["Q0", "Q1", "Q2"]

inicial = "Q0"
finais = ["Q2"]

transicoes = {"Q0":{'a':"Q1", 'b':"Q2"}, "Q1":{'a':"Q1", 'b':"Q2"}}

palavra = "aab"

atual = inicial

for e in palavra:
    if transicoes[inicial][e]:
        print(f"Estado atual = {transicoes[atual][e]}")
        atual = transicoes[atual][e]

if atual in finais:
    print("Palavra válida!")
else:
    print("Palavra não é válida!")
'''

'''
& / inicial
& / leu a -> a
a / leu b -> ba
ba / leu b -> bba
bba / leu c -> bba
bba / leu b -> &ba
ba / leu b -> &a
a / leu a -> &
&
'''
