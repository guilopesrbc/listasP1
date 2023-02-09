menu = {'hamburguer de siri' : ('siri', 'pao', 'alface', 'tomate', 'queijo', 'picles'), 'pizza de siri' : ('siri', 'trigo', 'fermento', 'ovos', 'queijo'),
            'siri frito' : ('siri', 'manteiga') ,'siri a parmegiana' : ('siri', 'trigo', 'ovos', 'queijo', 'tomate')}

estoque = {'siri' : 5, 'pao' : 5, 'alface' : 5, 'tomate': 5, 'queijo' : 5, 'picles': 5, 'trigo': 5, 'fermento' : 5, 'ovos' : 5, 'manteiga' : 5,'batata': 5, 'arroz': 5}

precos = {'siri' : 8, 'pao' : 2, 'alface' : 1, 'tomate': 2, 'queijo' : 5, 'picles': 3, 'trigo': 3, 'fermento' : 2,
          'ovos' : 2, 'manteiga' : 6, 'batata' : 4, 'arroz': 3, 'hamburguer de siri' : 24, 'pizza de siri': 42, 'siri frito': 15, 'siri a parmegiana' : 24}

preco_final = 0
demanda_dic = {}
mais_pedido = {}
while True:
    try:
        # recebendo pedido
        pedido = input()
        # vereficando se pedido está no cardapio
        consta = False
        for chave in menu.keys():
            if chave == pedido:
                consta = True
        # caso o pedido não esteja no cardapio
        if consta == False:
            # ja tenha sido pedido 2x
            if demanda_dic.get(pedido) == 2:
                entrada_ingred = input()
                ingredientes = entrada_ingred.split()
                ingredientes = tuple(ingredientes)
                # adicionando ao cardapio e aos precos
                # adicionando o preco
                preco_aux = 0
                for chave, value in precos.items():
                    for i in ingredientes:
                        if chave == i:
                            preco_aux += value
                preco_aux += 5
                precos.update({f'{pedido}': preco_aux})
                # adicionando ao cardapio
                menu.update({f'{pedido}' : ingredientes})
                print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Siri Cascudo.')
            # caso ainda há pouca demanda
            else:
                # verificando se ja foi pedido
                foi = False
                for chave in demanda_dic.keys():
                    if chave == pedido:
                        foi = True
                # computando
                if foi == False:
                    print(f'{pedido} ainda não é uma opção disponível.')
                    demanda_dic.update({f'{pedido}' : 1})
                elif foi == True:
                    for chave, valor in demanda_dic.items():
                        if chave == pedido:
                            demanda_dic[pedido] = valor + 1
                    print(f'{pedido} ainda não é uma opção disponível.')

        # caso esteja no cardapio e computando a retirada do estoque
        else:
            aux = menu.get(pedido)
            for i in aux:
                for y in estoque.keys():
                    if i == y:
                        # verificação de ingredientes no estoque
                        if estoque[i] == 0:
                            for chave, valor in precos.items():
                                if i == chave:
                                    custo = + 4 * valor
                            preco_final -= custo
                            estoque[i] += 4
                        estoque[i] -= 1
            for chave1, valor1 in precos.items():
                if chave1 == pedido:
                    preco_final += valor1
            # salvando os pedidos mais feitos
            # verificando se ja foi feito
            ok = False
            for chave in mais_pedido.keys():
                if chave == pedido:
                    ok = True
            # computando
            if ok == False:
                mais_pedido.update({f'{pedido}': 0})
            elif ok == True:
                for chave, valor in mais_pedido.items():
                    if chave == pedido:
                        mais_pedido[pedido] = valor + 1
            print(f'{pedido} saindo...')

    except EOFError:
        break
# fim do expediente
print('##### Fim do expediente #####')
print(f'O lucro obtido no dia de hoje foi de R${preco_final}.')
# prato mais pedido
max_valor = max(mais_pedido.values())
for chave, valor in mais_pedido.items():
    if valor == max_valor:
        prato = chave
if prato == 'hamburguer de siri':
    print('O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!')
else:
    print(f'{prato.capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.')
