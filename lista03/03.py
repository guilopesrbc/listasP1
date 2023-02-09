#entradas qtd de mochilas e nomes
m = int(input())
nomes = input()
nomes_lista = nomes.split(' ')
mochilas_totais = []
tamanho_mochilas = []

#loop para definir a quantidade e tamanhos das mochilas e os itens iniciais de todas as mochilas
for i in range(m):
   tamanho = int(input())
   tamanho_mochilas.append(tamanho)
   mochila_inicial = []
   mochila_inicial.append('Lanterna')
   mochila_inicial.append('Omega 3 da top therm')
   mochilas_totais.append(mochila_inicial)


#loop para adicionar itens
n = int(input())
for p in range(n):
   item = input()
   numero_da_mochila = int(input())
   #se estiver cheia
   if len(mochilas_totais[numero_da_mochila]) >= int(tamanho_mochilas[numero_da_mochila]):
       print('Mochila cheia. Não vai dar para levar.')
   #adcionando o item
   else:
       mochilas_totais[numero_da_mochila].append(item)

#loop para ações
acabou = False

while acabou == False:
    auxiliar = 0
    acao = input()
    if acao == 'Tirar da mochila' or acao == 'Guardar na mochila':
        item_acao = input()
        mochila_acao = int(input())
#ação tirar da mochila
        if acao == 'Tirar da mochila':
            #se tiver o item na mochila, ele vai ser usado
            for a in mochilas_totais[mochila_acao]:
                auxiliar = 0
                if a == item_acao:
                    auxiliar += 1
                    if auxiliar == 1:
                        mochilas_totais[mochila_acao].remove(a)
                        print(f'{item_acao} usado com sucesso da mochila {mochila_acao}.')
            #se não tiver o item na mochila
            if auxiliar == 0:
                print(f'Você não tem {item_acao} na mochila {mochila_acao}.')

#ação de guardar na mochila
        elif acao == 'Guardar na mochila':
            #se estiver cheia
            if len(mochilas_totais[mochila_acao]) > int(tamanho_mochilas[mochila_acao]):
                print(f'Mochila {mochila_acao} cheia!')
            #guardar na mochila
            else:
                mochilas_totais[mochila_acao].append(item_acao)
                print(f'{item_acao} adicionado na mochila {mochila_acao}.')
#ação final de chegada ao cin
    elif acao == 'CHEGAMOS NO CIN!':
        acabou = True
# se não for nenhuma das ações
    else:
        print('Ação inválida.')


f = 0
#outputs finais
for j in nomes_lista:
    print(f'Mochila de {j} chegou assim:')
    for z in mochilas_totais[f][0:]:
        print(z)
    f += 1








