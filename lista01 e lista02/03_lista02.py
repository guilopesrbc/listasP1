# variáveis
fim = False
bazingas = 0
desgosto = 0

# entradas e somatórios
while (fim == False):
    piada = input()

    if piada == 'Fim do Show!':
        fim = True
    else:
        reacao = input()
        if reacao == 'BAZINGA!':
            bazingas += 1
        else:
            desgosto += 1

# saídas
if bazingas > (desgosto + bazingas) * 0.6:
    print('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')
elif desgosto > (bazingas + desgosto) * 0.6:
    print('Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!')
else:
    print('Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!')