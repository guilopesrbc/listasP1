# verficar numero
def ver_numero(n, lista):
    global consta
    global fora
    for i in range(len(lista)):
        if n == lista[i]:
            consta = True
    if n > lista[-1] or n < lista[0]:
        print('Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.')
        fora = True
    # opeações
    if fora == False:
        binario(escolha, lista_binario)
        if bits >= len(lista_binario):
            # primeira porta
            porta_inicial(escolha, lista)
            # escolha das portas
            prox_porta(escolha, lista)
            # ajustando os bits
            item = ver_bits(bits, lista_binario)
            if consta == False:
                print(f'Meio, mas não consegui achar.')
            elif consta == True:
                print(f'Meio, seguindo por essas coordenadas você vai chegar no número ', end='')
                print(*item, sep='', end='')
                print('.')
        elif bits < len(lista_binario):
            if consta == False:
                print('Busquei muito, mas não achei a sala, que nem posso dizer, já que tenho poucos bits.')
            elif consta == True:
                print(
                    'Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.')


# função pra transformar inteiro
def trans_int(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])

# função porta inicial
def porta_inicial(n, lista):
    # variaveis usadas
    global num_meio
    global consta
    meio = int(len(lista) / 2)
    # caso ele n esteja na lista
    if consta == False:
        # e o numero está no intevalo do meio para direita
        if n > lista[meio]:
            print('Direita -> ', end='')
            for x in range(meio + 1):
                lista.pop(0)
        # do meio para a esquerda
        elif n < lista[meio]:
            print("Esquerda -> ", end='')
            for x in range(meio + 1):
                lista.pop(-1)
        return lista
    # está na lista
    else:
        # se o numero estiver no meio
        if n == lista[meio]:
            num_meio = True
        # e vai para a direita
        elif n > lista[meio]:
            print('Direita -> ', end='')
            for j in range(meio + 1):
                lista.pop(0)
        # e vai para a esquerda
        else:
            print("Esquerda -> ", end='')
            for j in range(meio + 1):
                lista.pop(-1)
        return lista

# função para proximas portas
def prox_porta(n, lista):
    # variaveis usadas
    inicio = 0
    meio = int(len(lista) / 2)
    final = -1
    global consta
    # caso base se consta for false
    if consta == False and len(lista) == 1:
        return lista
    # caso base
    elif len(lista) == 1:
        return lista
    # recursão para a esquerda
    elif n < lista[meio]:
        for i in range(meio):
            lista.pop(final)
        print("Esquerda -> ", end='')
        return prox_porta(n, lista)
    # recursão para a direita
    elif n > lista[meio]:
        for i in range(meio):
            lista.pop(inicio)
        print('Direita -> ', end='')
        return prox_porta(n, lista)
    elif n == lista[meio]:
        for i in range(len(lista)):
            lista.pop(0)
        return lista
# função transfomar em binario
def binario(escolha, lista):
    # caso base 0
    if escolha == 0:
        lista.append(0)
        lista.reverse()
        return lista
    # caso base 1
    elif escolha == 1:
        resto = escolha % 2
        lista.append(resto)
        lista.reverse()
        return lista
    # recursão binaria
    elif escolha > 1:
        resto = escolha%2
        lista.append(resto)
        escolha = int(escolha / 2)
        return binario(escolha, lista)

# função bits
def ver_bits(b, lista):
    if len(lista) == b:
        return lista
    elif len(lista) < b:
        lista.insert(0, 0)
        return ver_bits(b, lista)

# entrada da lista
lista = input()
lista = lista.split(' ')
lista_binario = []
# transformar a lista para inteiro
trans_int(lista)
# entrada escolha do numero
escolha = int(input())
# entrada do numero de bits
bits = int(input())
# variaveis usadas nas funções
consta = False
fora = False
num_meio = False
# marcação das portas
inicio = 0
meio = int(len(lista) / 2)
final = -1
# verificando caso numero está fora do intervalo e realizando todas as operações
ver_numero(escolha, lista)