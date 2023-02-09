nome_1 = input('digite o primeiro nome:')
pontuacao_1 = int(input('digite a pontuação do primeiro nome:'))

nome_2 = input('digite o segundo nome:')
pontuacao_2 = int(input('digite a pontuação do segundo nome:'))

nome_3 = input('digite o terceiro nome:')
pontuacao_3 = int(input('digite a pontuação do terceiro nome:'))
#empate
if (pontuacao_1 == pontuacao_2 == pontuacao_3):
    if (nome_1 < nome_2 and nome_1 < nome_3 and nome_2 < nome_3):
        print(f'{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}')
    elif (nome_1 < nome_2 and nome_1 < nome_3 and nome_3 < nome_2):
        print(f'{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}')
    elif (nome_2 < nome_1 and nome_2 < nome_3 and nome_1 < nome_3):
        print(f'{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}')
    elif (nome_2 < nome_1 and nome_2 < nome_3 and nome_3 < nome_1):
        print(f'{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}')
    elif (nome_3 < nome_2 and nome_3 < nome_1 and nome_2 < nome_1):
        print(f'{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}')
    elif (nome_3 < nome_2 and nome_3 < nome_1 and nome_1 < nome_2):
        print(f'{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}')
#pontuacao
if (pontuacao_1 < pontuacao_2 and pontuacao_1 < pontuacao_3 and pontuacao_2 < pontuacao_3):
    print(f'{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}')
elif (pontuacao_1 < pontuacao_2 and pontuacao_1 < pontuacao_3 and pontuacao_3 < pontuacao_2):
    print(f'{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}')
elif (pontuacao_1 < pontuacao_2 and pontuacao_1 < pontuacao_3 and pontuacao_3 == pontuacao_2 and nome_2 < nome_3):
    print(f'{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}')
elif (pontuacao_1 < pontuacao_2 and pontuacao_1 < pontuacao_3 and pontuacao_3 == pontuacao_2 and nome_3 < nome_2):
    print(f'{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}')
elif (pontuacao_1 == pontuacao_2 and pontuacao_1 < pontuacao_3 and nome_1 < nome_2):
    print(f'{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}')
elif (pontuacao_1 == pontuacao_3 and pontuacao_1 < pontuacao_2 and nome_1 < nome_3):
    print(f'{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}')

#pontuacao 2
elif (pontuacao_2 < pontuacao_1 and pontuacao_2 < pontuacao_3 and pontuacao_1 < pontuacao_3):
    print(f'{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}')
elif (pontuacao_2 < pontuacao_1 and pontuacao_2 < pontuacao_3 and pontuacao_3 < pontuacao_1):
    print(f'{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}')
elif (pontuacao_2 < pontuacao_1 and pontuacao_2 < pontuacao_3 and pontuacao_1 == pontuacao_3 and nome_1 < nome_3):
    print(f'{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}')
elif (pontuacao_2 < pontuacao_1 and pontuacao_2 < pontuacao_3 and pontuacao_1 == pontuacao_3 and nome_3 < nome_1):
    print(f'{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}')
elif (pontuacao_2 == pontuacao_1 and pontuacao_2 < pontuacao_3 and nome_2 < nome_1):
    print(f'{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}')
elif (pontuacao_2 == pontuacao_3 and pontuacao_2 < pontuacao_1 and nome_2 < nome_3):
    print(f'{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}')

#pontuacao 3
elif (pontuacao_3 < pontuacao_2 and pontuacao_3 < pontuacao_1 and pontuacao_2 < pontuacao_1):
    print(f'{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}')
elif (pontuacao_3 < pontuacao_2 and pontuacao_3 < pontuacao_1 and pontuacao_1 < pontuacao_2):
    print(f'{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}')
elif (pontuacao_3 < pontuacao_1 and pontuacao_3 < pontuacao_2 and pontuacao_1 == pontuacao_2 and nome_2 < nome_1):
    print(f'{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}')
elif (pontuacao_3 < pontuacao_1 and pontuacao_3 < pontuacao_2 and pontuacao_1 == pontuacao_2 and nome_1 < nome_2):
    print(f'{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}')
elif (pontuacao_3 == pontuacao_1 and pontuacao_3 < pontuacao_2 and nome_3 < nome_1):
    print(f'{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}')
elif (pontuacao_3 == pontuacao_2 and pontuacao_3 < pontuacao_1 and nome_3 < nome_2):
    print(f'{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}')




