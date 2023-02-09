# entradas e definição do mapa
nome = input()
mapa = []
subiu1 = False
esquerda1 = False
subiu2= False
esquerda2 = False
# adicionando o mapa e separando-o cada caracter para facilitar o andamento na lista
for i in range(8):
    mapa.append(list(input()))
# achar o index do demodog e pessoa
for x in range(len(mapa) - 1):
    for l in mapa[x]:
        if l == 'd':
            # 'd' é index demodog
            d = x
        elif l == 'p':
            # 'p' é index pessoa
            p = x
# localização da pessoa e demodog
for k in range(len(mapa) - 1):
    v = 0
    for j in mapa[k]:
        if j == 'd':
            #localização do demodog
            demodog = mapa[k][v]
            demoindex2 = v
        elif j == 'p':
            #localização pessoa
            pessoa = mapa[k][v]
            pessoaindex2 = v
            #localização da chegada
        elif j == 'o':
            chegada = mapa[k][v]
        v += 1
a = pessoaindex2
b = demoindex2
# loop de andamento da pessoa e do demodog
acabou = False
final1 = 0
final2 = 0
final3 = 0
final4 = 0
while acabou == False:
    # finalizando o loop caso a pessoa chegue ao final ou os dois estejam a um passo da chegada
    if mapa[p][a + 1] == chegada or mapa[p + 1][a] == chegada or mapa[p - 1][a] == chegada or mapa[p][a - 1] == chegada:
        if mapa[d][b + 1] == chegada or mapa[d + 1][b] == chegada or mapa[d - 1][b] == chegada or mapa[d][b - 1] == chegada:
            mapa[p][a] = '.'
            acabou = True
            final1 += 1
        else:
            mapa[p][a] = '.'
            acabou = True
            final1 += 1
    # finalizando o loop caso demodog alcance a pessoa e ela tava indo para a direita
    elif mapa[p][a + 1] == '|' and mapa[p + 1][a] == '_' and mapa[p - 1][a] == '_' and mapa[p][a - 1] == 'd':
        mapa[d][a] = demodog
        mapa[d][a - 1] = '.'
        acabou = True
        final3 += 1
    # finalizando o loop caso o demodog alcance a pessoa e ela tava indo para baixo
    elif mapa[p][a + 1] == '|' and mapa[p + 1][a] == 'p' and mapa[p - 1][a] == '_' and mapa[p][a - 1] == '|' :
        mapa[d][a] = demodog
        mapa[d - 1][a] = '.'
        acabou = True
        final3 += 1
    # finalizando o loop caso o demodog alcance a pessoa e ela n consegue ir para cima
    elif mapa[p][a + 1] == '|' and mapa[p + 1][a] == '_' and mapa[p - 1][a] == 'p' and mapa[p][a - 1] == '|':
        mapa[d][a] = demodog
        mapa[d + 1][a] = '.'
        acabou = True
        final3 += 1
    # finalizando o loop caso demodog alcance a pessoa e ela n consegue ir para a esquerda
    elif mapa[p][a - 1] == '|' and mapa[p + 1][a] == '_' and mapa[p - 1][a] == '_' and mapa[p][a + 1] == 'd':
        mapa[d][a] = demodog
        mapa[d][a + 1] = '.'
        acabou = True
        final2 += 1
    # finalizando o loop caso o demodog chegue ao final
    elif mapa[d][b + 1] == chegada or mapa[d + 1][b] == chegada or mapa[d - 1][b] == chegada or mapa[d][b - 1] == chegada:
        # pessoa tava indo para a direita
        if esquerda1 == False and mapa[p][a + 1] == '.':
            mapa[p][a + 1] = pessoa
            mapa[p][a] = '.'
            mapa[d][b] = '.'
            acabou = True
            final4 += 1
        # pessoa tava indo para baixo
        elif subiu1 == False and mapa[p + 1][a] == '.':
            mapa[p + 1][a] = pessoa
            mapa[p][a] = '.'
            mapa[d][b] = '.'
            acabou = True
            final4 += 1
        # pessoa tava indo para cima
        elif mapa[p - 1][a] == '.':
            mapa[p - 1][a] = pessoa
            mapa[p][a] = '.'
            mapa[d][b] = '.'
            acabou = True
            final4 += 1
        # pessoa tava indo para esquerda
        elif mapa[p][a - 1] == '.':
            mapa[p][a - 1] = pessoa
            mapa[p][a] = '.'
            mapa[d][b] = '.'
            acabou = True
            final4 += 1
    else:
        # pessoa casos
        # direita
        if esquerda1 == False and mapa[p][a + 1] == '.':
            mapa[p][a + 1] = pessoa
            mapa[p][a] = '.'
            a += 1
            subiu1 = False
        # baixo
        elif subiu1 == False and mapa[p + 1][a] == '.':
            mapa[p + 1][a] = pessoa
            mapa[p][a] = '.'
            p += 1
            esquerda1 = False
        # cima
        elif mapa[p - 1][a] == '.':
            mapa[p - 1][a] = pessoa
            mapa[p][a] = '.'
            p -= 1
            subiu1 = True
            esquerda1 = False
        # esquerda
        elif mapa[p][a - 1] == '.':
            mapa[p][a - 1] = pessoa
            mapa[p][a] = '.'
            a -= 1
            esquerda1 = True
            subiu1 = False
        # demodog casos
        # direita
        if esquerda2 == False and mapa[d][b + 1] == ('.' or 'p'):
            mapa[d][b + 1] = demodog
            mapa[d][b] = '.'
            b += 1
            subiu2 = False
        # baixo
        elif subiu2 == False and mapa[d + 1][b] == ('.' or 'p'):
            mapa[d + 1][b] = demodog
            mapa[d][b] = '.'
            d += 1
            esquerda2 = False
        # cima
        elif mapa[d - 1][b] == ('.' or 'p'):
            mapa[d - 1][b] = demodog
            mapa[d][b] = '.'
            d -= 1
            subiu2 = True
            esquerda2 = False
        # esquerda
        elif mapa[d][b - 1] == ('.' or 'p'):
            mapa[d][b - 1] = demodog
            mapa[d][b] = '.'
            b -= 1
            esquerda2 = True
            subiu2 = False

    # prints das linhas do mapa
    if acabou == True:
        for linha in mapa:
            print(*linha, sep=' ')
    else:
        for linha in mapa:
            print(*linha, sep=' ')
# OUTPUTS FINAIS
if final1 == 1:
    print(f'UFA!!! Você e {nome} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
elif final2 == 1:
    print(f'Ah não, você e {nome} foram pegos pelo demodog e agora ele vai atravessar o portal e talvez a eleven não consiga salvar todos.')
elif final3 == 1:
    print(f'Ah não, você e {nome} foram pegos pelo demodog e agora ele vai atravessar o portal e talvez a eleven não consiga salvar todos.')
elif final4 == 1:
    print(f'Ah não, você e {nome} não foram rápidos o bastante e o demodog passou pelo portal.')
