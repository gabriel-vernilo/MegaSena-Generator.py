#Gerador de jogos na Mega -

from random import randint

qtd = int(input("Quantos jogos você quer fazer ?\n"))
for _ in range(qtd):
    itens_combinados = [randint(1, 60) for _ in range(6)]
    while len(itens_combinados) != len(set(itens_combinados)): #nao repetir na mesma linha
        itens_combinados = [randint(1, 60) for _ in range(6)]
    a,b,c,d,e,f = sorted([f"{n:02d}" for n in itens_combinados]) #sorted(), para ficar em ordem crescente assim como no jogo. {n:02d}, para adicionar 0 se n < 10.
    print(a,b,c,d,e,f)
