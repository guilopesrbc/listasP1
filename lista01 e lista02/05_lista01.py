nome_da_quadrilha = input()
pontuacao = float(0)
pontuacao_final = False
erro = False
passo_1 = input().capitalize()
passo_2 = input().capitalize()
passo_3 = input().capitalize()
passo_4 = input().capitalize()
passo_5 = input().capitalize()
#passo 1 regras
if (passo_1 == 'Cumprimento'):
    pontuacao = pontuacao + 100
elif (passo_1 == 'Balancê'):
    pontuacao = pontuacao + 50
elif (passo_1 == 'Passeio'):
    pontuacao = pontuacao + 70
elif (passo_1 == 'Túnel'):
    pontuacao = pontuacao * 0.9
elif (passo_1 == 'Serrote'):
    pontuacao = pontuacao + 100
elif (passo_1 == 'Casamento'):
    pontuacao_final = True
elif (passo_1 == 'Despedida'):
    pontuacao = pontuacao + 0
else:
    erro = True
#passo 2 regras
if (passo_2 == 'Cumprimento'):
    pontuacao = pontuacao + 10
elif (passo_2 == 'Balancê'):
    pontuacao = pontuacao + 50
elif (passo_2 == 'Passeio'):
    pontuacao = pontuacao + 70
elif (passo_2 == 'Túnel'):
    pontuacao = pontuacao * 0.9
elif (passo_2 == 'Serrote'):
    pontuacao = pontuacao + 100
elif (passo_2 == 'Casamento'):
    pontuacao_final = True
elif (passo_2 == 'Despedida'):
    pontuacao = pontuacao + 0
else:
    erro = True

#passo 3 regras
if (passo_3 == 'Cumprimento'):
    pontuacao = pontuacao + 10
elif (passo_3 == 'Balancê'):
    pontuacao = pontuacao + 50
elif (passo_3 == 'Passeio'):
    pontuacao = pontuacao + 70
elif (passo_3 == 'Túnel'):
    pontuacao = pontuacao * 0.9
elif (passo_3 == 'Serrote'):
    pontuacao = pontuacao + 100
elif (passo_3 == 'Casamento'):
    pontuacao_final = True
elif (passo_3 == 'Despedida'):
    pontuacao = pontuacao + 0
else:
    erro = True

#passo 4 regras
if (passo_4 == 'Cumprimento'):
    pontuacao = pontuacao + 10
elif (passo_4 == 'Balancê'):
    pontuacao = pontuacao + 50
elif (passo_4 == 'Passeio'):
    pontuacao = pontuacao + 70
elif (passo_4 == 'Túnel'):
    pontuacao = pontuacao * 0.9
elif (passo_4 == 'Serrote'):
    pontuacao = pontuacao + 100
elif (passo_4 == 'Casamento'):
    pontuacao_final = True
elif (passo_4 == 'Despedida'):
    pontuacao = pontuacao + 0
else:
    erro = True

#passo 5 regras
if (passo_5 == 'Cumprimento'):
    pontuacao = pontuacao + 10
elif (passo_5 == 'Balancê'):
    pontuacao = pontuacao + 50
elif (passo_5 == 'Passeio'):
    pontuacao = pontuacao + 70
elif (passo_5 == 'Túnel'):
    pontuacao = pontuacao * 0.9
elif (passo_5 == 'Serrote'):
    pontuacao = pontuacao + 100
elif (passo_5 == 'Casamento'):
    pontuacao_final = True
elif (passo_5 == 'Despedida'):
    pontuacao = pontuacao + 35
else:
    erro = True

if (pontuacao_final == True):
    pontuacao = pontuacao * 2

if (erro == False ):
    print(f'Parabéns, {nome_da_quadrilha}! Bela apresentação. A pontuação foi de {pontuacao}!')
else:
    print(f'Poxa, {nome_da_quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')









