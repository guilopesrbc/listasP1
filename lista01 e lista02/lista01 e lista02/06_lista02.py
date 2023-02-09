# entrada estrelas e primeiras condições
e = int(input())
# output 6
if e <= 0:
    print('Isso está quebrado, acho que Howard pode me ajudar.')
# output 7
elif e > 0 and e < 3:
    print('Acho que bebi demais, eu juro que tinha mais estrelas!')
else:
    # entrada estrela 1
    a_x = int(input())
    a_y = int(input())
    # variaveis para a sequência de fibonacci
    fibonacci = 0
    contador = 0
    # variaveis para a distância euclidiana funcionar
    star = 0
    d = 0
    soma = 0
    # variavel para os outputs finais
    final = e

    # programa
    while (e > 1):
        # variaveis para sequencia de fibonacci
        n1 = 0
        n2 = 1
        # entrada estrela 2 e sequência do código...
        b_x = int(input())
        b_y = int(input())
        # cálculo das distâncias
        d = ((a_x - b_x) ** 2 + (a_y - b_y) ** 2) ** 0.5
        while (n1 <= int(d)):
            n = n1 + n2
            n1 = n2
            n2 = n
            if int(d) == n1:
                fibonacci += 1
            contador += 1
        print(f'Distância [star{star + 1} <-> star{star + 2}]: {int(d)}')
        a_x = b_x
        a_y = b_y
        # soma das distâncias
        soma += int(d)
        # contagem de loops
        e -= 1
        star += 1
    # usar while para achar numero primo
    semprimo = False
    contador = 2
    while (contador <= (soma - 1)):
        if soma % contador == 0:
            semprimo = True
        contador += 1
    # saidas finais
    ######## todos os finais tem que ser -1 pois o numero de distancias é o numero de estrelas -1
    # output 1
    if fibonacci == int((final - 1)) and semprimo == True:
        print('Yes! Eu consegui!')

    # output 2
    elif fibonacci == int((final - 1)) and semprimo == False:
        print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')

    # output 3
    elif fibonacci == int((final - 2)):
        print('Oh, não! Eu quase consegui!')

    # output 4
    elif fibonacci <= int((final - 3)) and semprimo == True:
        print('Eu vou acabar como o Stuart :/')

    # output 5
    elif fibonacci <= int((final - 3)) and semprimo == False:
        print('Pelo menos o programa está funcionando...')
