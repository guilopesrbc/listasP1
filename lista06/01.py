# função para executar os comandos
def comandos_pokedex(comandos,pokedex):
    for i in range(len(comandos)):
        for y in comandos[i]:
            # comando de add ou desc
            if y == 'ADD' or y == 'DESC':
                # caso seja a primeira adição
                if y == 'ADD' and len(pokedex) == 0:
                    descricao = ''
                    for k in comandos[i + 1]:
                        if k == comandos[i + 1][-1]:
                            descricao += k
                        else:
                            descricao += k + ' '
                    pokedex.update({f'{comandos[i][1]}': f'{descricao}'})
                    print('Pokémon adicionado com sucesso')
                    break
                else:
                    check = False
                    # verificando na pokedex
                    for chave,valor in pokedex.items():
                        # caso ja foi adicionado
                        if y == 'ADD' and comandos[i][1] == chave:
                            print('Pokémon já adicionado na Pokédex')
                            break
                        # adicionando
                        elif y == 'ADD':
                            descricao = ''
                            for k in comandos[i+1]:
                                if k == comandos[i + 1][-1]:
                                    descricao += k
                                else:
                                    descricao += k + ' '
                            pokedex.update({f'{comandos[i][1]}' : f'{descricao}'})
                            print('Pokémon adicionado com sucesso')
                            break
                        # printando descrição
                        elif y == 'DESC'and comandos[i][1] == chave:
                            print(valor)
                            check = True
                            break
                    # caso o pokemon não esteja adicionado e foi pedido sua descrição
                    if y == 'DESC' and check == False:
                        print('Ainda não há registro desse Pokémon')
                        break
                break
# definições
pokedex = {}
comandos = []
# entrada
while True:
    try:
        entrada = input()
        entrada = entrada.split()
        comandos.append(entrada)
    except EOFError:
        break
# chamar a função
comandos_pokedex(comandos, pokedex)