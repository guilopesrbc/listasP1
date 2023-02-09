# função comparação
def comparar(dic1, dic2):
    x = 0
    for i in dic1.values():
        for z, y in dic2.items():
            if i == y:
                x += 1
                del dic2[z]
                break
    return x
# entradas e definições
n = int(input())
piccolo = {}
gohan = {}
entrada1 = input()
entrada2 = input()
list_aux1 = entrada1.split()
list_aux2 = entrada2.split()

# definindo os dicionarios
for i in range(n):
    gohan.update({f'd{i}' : list_aux1[i] })
    piccolo.update({f'd{i}' : list_aux2[i] })
# chamar a comparação
x = comparar(gohan, piccolo)
#prints
if x == len(gohan):
    print('Dale Gohan!')
else:
    print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')

