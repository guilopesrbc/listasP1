import string
# operacao mod
def mod_11(x):
    return x%11

# fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# fatorial
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n  * fatorial(n-1)

# multiplicador de listas
def multiplica(lista1, lista2):
    lista = []
    for a in range(len(lista1)):
        lista.append(lista1[a]*lista2[a])
    return lista

# soma de listas
def soma(lista1, lista2):
    lista = []
    for a in range(len(lista1)):
        lista.append(lista1[a]+lista2[a])
    return lista
# armazenando o alfabeto, entradas das senhas e palavras
alfabeto = list(string.ascii_lowercase)
senha = list(input())
n = int(input())
comp_palavras = []

# entrada das palavras
for j in range(n):
    comp_palavras.append(list(input()))

# operacao das palavras
# variavel para salvar se achar a palavra
achou = False
for k in range(len(comp_palavras)):
    nova_palavra = []
    # verificar qual letra do alfabeto é para achar o numero dela e fazer o mod 11
    for l in range(len(comp_palavras[k])):
        for a in range(len(alfabeto)):
            # realizar o mod 11 da letra
            if comp_palavras[k][l] == alfabeto[a]:
                operacao1 = mod_11(a)

                # salvando em lista os resultados de fibonacci e fatorial
                operacao2 = []
                operacao3 = []
                # loop para salvar em listas os resultados
                for f in range(operacao1):
                    operacao2.append(fibonacci(f))
                for f in range(operacao1):
                    operacao3.append(fatorial(f))

                # analisar e adicionar as letras
                # caso seja 0
                if operacao1 == 0:
                    nova_palavra.append('1')
                    break
                # caso seja impar
                elif operacao1 % 2 != 0:
                    # multiplicar os termos de fibonacci com fatorial
                    resultado = multiplica(operacao2, operacao3)
                    # verificar quais letras
                    for i in resultado:
                        index = i % 26
                        nova_palavra.append(alfabeto[index])
                    break
                # caso seja par
                elif operacao1 % 2 == 0:
                    # somar os termos de fibonacci com fatorial
                    resultado = soma(operacao2, operacao3)
                    # verificar quais letras
                    for i in resultado:
                        index = i % 26
                        nova_palavra.append(alfabeto[index])
                    break
    # comparar a nova palavra com a senha
    certo = 0
    for i in range(len(senha)):
        if len(nova_palavra) == len(senha):
            if nova_palavra[i] == senha[i]:
                certo += 1
    if certo == len(senha):
        achou = True
# prints finais
if achou == True:
    print('Achamos! Achamos a senha.')
else:
    print('É... Temos que procurar mais.')