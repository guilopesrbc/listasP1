#entrada
print("LOCUTOR:'sheldon e raj vão tirar um game lagarto, spock e tesoura e você vai ajuda-los'")
n = int(input('escolha um numero maior que 0:\n'))
while (n < 1):
    print("escolha um numero maior que 0:\n")
    n = int(input())
sheldonwins = 0
rajwins = 0

while (n > 0):
    n -= 1
    acao_s = input('escolha a ação de sheldon:\n')
    acao_r = input('escolha a ação de raj:\n')
#vitorias sheldon
    if acao_s == 'lagarto' and acao_r == 'spock':
        sheldonwins += 1
        print('sheldon ganhou')
    elif acao_s == 'spock' and acao_r == 'tesoura':
        sheldonwins += 1
        print('sheldon ganhou')
    elif acao_s == 'tesoura' and acao_r == 'lagarto':
        sheldonwins += 1
        print('sheldon ganhou')
    elif acao_s == acao_r:
        sheldonwins += 0
#vitorias raj
    if acao_r == 'lagarto' and acao_s == 'spock':
        rajwins += 1
        print('raj ganhou')
    elif acao_r == 'spock' and acao_s == 'tesoura':
        rajwins += 1
        print('raj ganhou')
    elif acao_r == 'tesoura' and acao_s == 'lagarto':
        rajwins += 1
        print('raj ganhou')
    elif acao_s == acao_r:
        rajwins += 0
#resultados
if sheldonwins == rajwins:
    print('Oh não, precisamos de outra rodada.')
elif sheldonwins > rajwins:
    print('BAZINGA! EU SOU O SENHOR DA SALA!')
elif rajwins > sheldonwins:
    print('ENGOLE ESSA, SHELDON!')

