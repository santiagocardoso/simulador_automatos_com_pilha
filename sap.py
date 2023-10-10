'''
    Trabalho final de LFA

    Alunos:
        Santiago Cardoso
        Lucas Gabriel
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
