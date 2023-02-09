# definindo a função
def mensagem_gatos(n):
    mensagem_final = []
    acabou = False
    for j in range(len(n[0])):
        n[0][j] = int(n[0][j])

    for k in n[0]:

        if int(k) == 100:
            mensagem_final.append(espaco)

        elif int(k) > 100 or int(k) < 0:
            acabou = True
            break
        else:
            # aderindo até 26 as letras minusculas
            if int(k) < 26:
                for a in range(26):
                    if k == a:
                        for b in minusculo:
                            if a == minusculo.index(b):
                                k = b
                        mensagem_final.append(k)
            # aderindo até 49 as letras minusculas
            elif int(k) > 25 and int(k) < 50:
                for c in range(26, 50):
                    if k == c:
                        for d in minusculo:
                            if (c - 26) == minusculo.index(d):
                                k = d
                        mensagem_final.append(k)
            # aderindo até 75 as letras maiusculas
            elif int(k) > 49 and int(k) < 76:
                for e in range(50, 76):
                    if k == e:
                        for f in maiusculo:
                            if (e - 50) == maiusculo.index(f):
                                k = f
                        mensagem_final.append(k)
            # aderindo até 99 as letras maiusculas
            elif int(k) > 75 and int(k) < 100:
                for g in range(76, 100):
                    if k == g:
                        for h in maiusculo:
                            if (g - 76) == maiusculo.index(h):
                                k = h
                        mensagem_final.append(k)
    if acabou == True:
        print('Infelizmente os números nao dizem nada')
    elif acabou == False:
        print(*mensagem_final, sep='')

# definição das listas de letras
import string
minusculo = list(string.ascii_lowercase)
maiusculo = list(string.ascii_uppercase)
espaco = ' '
# entrada dos numeros da frase e chamada da função
numeros = input()
n = [numeros.split(' ')]
mensagem_gatos(n)

