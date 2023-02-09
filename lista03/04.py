# entrada das linhas da matriz
n = int(input())
linhas = []
pares = []
senha = []
for i in range(n):
    entradas_matriz = input()
    matriz = entradas_matriz.split(' ')
    linhas.append(matriz)
# transformar os números para inteiro
for j in range(n):
    for k in range(n):
        linhas[j][k] = int(linhas[j][k])

# soma das linhas
par_maior = ''
maior_soma = 0
soma_par = 0
for x in linhas:
    for z in range(n - 1):
        soma_par = (x[z] + x[z + 1])
        if soma_par >= maior_soma:
            if maior_soma == soma_par and par_maior != '':
                maior_soma = soma_par
            else:
                maior_soma = soma_par
                par_maior = (f'{x[z]}, {x[z + 1]}')
pares.append(par_maior)
senha.append(max(pares))
pares = []

#soma das colunas
w = 0
q = 0
a = 0
par_maior = ''
maior_soma = 0
soma_par = 0
for r in linhas:
    q = 0
    for c in range(n - 1):
        soma_par = linhas[q][w] + linhas[q+1][w]
        if soma_par >= maior_soma:
            if maior_soma == soma_par and par_maior != '':
                maior_soma = soma_par
            else:
                maior_soma = soma_par
                par_maior = (f'{linhas[q][w]}, {linhas[q+1][w]}')
        q += 1
    w += 1
    a += 1
pares.append(par_maior)
senha.append(max(pares))
pares = []

#soma dos pares da diagonal
par_maior = ''
maior_soma = 0
soma_par = 0
for t in range(n - 1):
    soma_par = linhas[t][t] + linhas[t+1][t+1]
    if soma_par >= maior_soma:
        if maior_soma == soma_par and par_maior != '':
            maior_soma = soma_par
        else:
            maior_soma = soma_par
            par_maior = (f'{linhas[t][t]}, {linhas[t+1][t+1]}')
pares.append(par_maior)
senha.append(max(pares))
pares = []
#final
senha_int = []
for d in senha:
    senha_int.append(d.split(', '))
senha_final = []
for m in senha_int:
    senha_final.append(m[0])
    senha_final.append(m[1])

print('Falei que era fácil Dustinzinho...\nPegando todas os números que formam as combinações dos pares de cada sentido temos...')
print("Password: ", end='')
print(*senha_final, sep = '')
