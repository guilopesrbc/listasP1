# definindo as funções:
# função soma de matrizes
def soma_matriz(matriz1,matriz2):
    matriz_resultante = []
    for x in range(len(matriz1)):
        # cria uma nova linha para a matriz resultante
        linha_matriz = []
        for y in range(len(matriz2)):
            # soma os valores nas matrizes
            linha_matriz.append((matriz1[x][y] + matriz2[x][y]))
        # armazena a linha na matriz resultante
        matriz_resultante.append(linha_matriz)
    return matriz_resultante

# função subtração de matrizes
def subtracao_matriz(matriz1,matriz2):
    matriz_resultante = []
    for x in range(len(matriz1)):
        #cria uma nova linha para a matriz resultante
        linha_matriz = []
        for y in range(len(matriz2)):
            # soma os valores nas matrizes
            linha_matriz.append((matriz1[x][y] - matriz2[x][y]))
        # armazena a linha na matriz resultante
        matriz_resultante.append(linha_matriz)
    return matriz_resultante

# função matriz escarlar
def matriz_escalar(matriz,k):
    matriz_resultante = []
    for x in range(len(matriz)):
        linha_matriz = []
        for y in range(len(matriz)):
            linha_matriz.append((matriz[x][y] * k))
        matriz_resultante.append(linha_matriz)
    return matriz_resultante

# função multiplicação de matrizes
def multi_matriz(m1,m2):
    matriz_resultante = []
    for x in range(len(m1)):
        linha_matriz = []
        index = []
        # pegando a linha da matriz 1
        for y in range(len(m1)):
            linha_matriz.append(m1[x][y])
        for u in range(len(m2)):
            # pegando a coluna da matriz 2
            coluna_matriz = []
            for z in range(len(m2)):
                coluna_matriz.append(m2[z][u])
            termo = 0
            # multiplicando os termos, somando os termos e armazenando em uma linha
            for w in range(len(m2)):
                valor = linha_matriz[w] * coluna_matriz[w]
                termo += valor
            index.append(int(termo))
        matriz_resultante.append(index)
    return matriz_resultante

# função para achar a operação
def achar_op(op_lista):
    operacao = ''
    for b in range(len(op_lista) - 1):
        # achando a operação soma
        if op_lista[b] == '+':
            op_lista[b] = f'soma_matriz({op_lista[b-1]},{op_lista[b+1]})'
            op_lista.pop(b - 1)
            op_lista.pop(-1)
            operacao = ''.join(op_lista)
        # achando a operação subtração
        elif op_lista[b] == '-':
            op_lista[b] = f'subtracao_matriz({op_lista[b-1]},{op_lista[b+1]})'
            op_lista.pop(b - 1)
            op_lista.pop(-1)
            operacao = ''.join(op_lista)
        # achando a operação multiplicação
        elif op_lista[b] == '.':
            op_lista[b] = f'multi_matriz({op_lista[b-1]},{op_lista[b+1]})'
            op_lista.pop(b - 1)
            op_lista.pop(-1)
            operacao = ''.join(op_lista)
        # achando a operação multiplicação escalar
        elif op_lista[b] == '*':
            if op_lista[b - 1] == 'm1' or op_lista[b - 1] == 'm2':
                op_lista[b] = f'matriz_escalar({op_lista[b-1]},{op_lista[b+1]})'
                op_lista.pop(b - 1)
                op_lista.pop(-1)
                operacao = ''.join(op_lista)
            else:
                op_lista[b] = f'matriz_escalar({op_lista[b + 1]},{op_lista[b - 1]})'
                op_lista.pop(b - 1)
                op_lista.pop(-1)
                operacao = ''.join(op_lista)
    return operacao

# função transformar para inteiro
def trans_int(matriz):
    for j in range(len(matriz)):
        for l in range(len(matriz)):
            matriz[j][l] = int(matriz[j][l])
    return matriz
# função de print saida
def saida_matriz(m):
    for linha in m:
        print(*linha, sep=' ')

# entrada do numero de linhas e colunas da matriz quadrada
n = int(input())
# criando a primeira matriz e a segunda matriz
m1 = []
for a in range(n):
    linha = input()
    m1.append(linha.split(' '))
m2 = []
for a in range(n):
    linha = input()
    m2.append(linha.split(' '))

# transformação os indexs das matrizes para inteiro
m1 = trans_int(m1)
m2 = trans_int(m2)

# numero de operações que serão realizadas
qtd_op = int(input())

# armazenando as operações em uma lista para depois entender qual operação será feita:
operacao_lista = []
for b in range(qtd_op):
    op = []
    op = input()
    operacao_lista.append(op.split(' '))

# realizando operações
for c in range(len(operacao_lista)):
    operacao = ''
    operacao = achar_op(operacao_lista[c])
    exec(str(operacao))

# saida final
if operacao_lista[-1][0] == 'm1':
    saida_matriz(m1)
elif operacao_lista[-1][0] == 'm2':
    saida_matriz(m2)