'''
    Trabalho final de LFA

    Alunos:
        Lucas Gabriel
        Santiago Cardoso
'''

alfabeto = ['a', 'b']
estados = ["Q0", "Q1", "Q2"]

inicial = "Q0"
finais = {"Q2"}

transicoes = {"Q0":{'a':"Q1", 'b':"Q2"}, "Q1":{'a':"Q1", 'b':"Q2"}}

palavra = "aab"

for e in palavra:
    if transicoes[inicial][e]:
        print(f"Estados atual = {transicoes[inicial][e]}")
