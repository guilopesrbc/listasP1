# definindo as funções recursivas
# função 1 barra '('
def contagem_barra_1(ep,x):
    # caso seja o ultimo termo
    if x == (len(ep) - 1):
        # caso base
        if ep[x] != '(':
            return 0
        else:
            return 1
    else:
        if ep[x] != '(':
            return 0 + contagem_barra_1(ep,x+1)
        else:
            return 1 + contagem_barra_1(ep,x+1)
# função 2 barra ')'
def contagem_barra_2(ep,x):
    # caso seja o ultimo termo
    if x == (len(ep) - 1):
        # caso base
        if ep[x] != ')':
            return 0
        else:
            return 1
    else:
        if ep[x] != ')':
            return 0 + contagem_barra_2(ep,x+1)
        else:
            return 1 + contagem_barra_2(ep,x+1)
# função de prints
def prints(contagem1, contagem2):
    if contagem_1 == contagem_2:
        print('Essa sentença está com os parênteses balanceados, HOORAY!')
    elif contagem_1 > contagem_2:
        print('A quantidade de parênteses \'(\' está maior que a de \')\', vamos descartá-la')
    elif contagem_2 > contagem_1:
        print('A quantidade de parênteses \')\' está maior que a de \'(\', vamos descartá-la')
# entrada da qtd de expressões
n = int(input())

# loop para inputs da0s expressões
for i in range(n):
    exp = list(input())
    contagem_1 = 0
    contagem_2 = 0
    # contagem e chamada das funções
    contagem_1 += contagem_barra_1(exp,0)
    contagem_2 += contagem_barra_2(exp,0)
    # prints pós contagem
    prints(contagem_1, contagem_2)