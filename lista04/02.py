# definindo a função
def nome_do_hospital(palavra_total, hospital_silabas):
        # variavel para checar se a palavra consta no nome do hospital
        consta = False
        # separação das letras das palavras
        palavra = list(palavra_total)
        # armazenamento das silabas da palavra
        silabas = []
        # loop para dividir a palavra em silabas
        j = 0
        while j < len(palavra):
            # caso seja uma silaba com 3 letras 'ch ou sh'
            if (palavra[j] == 'c' or palavra[j] == 's') and palavra[j + 1] == 'h' and (palavra[j + 2] == 'a' or palavra[j + 2] == 'e' or palavra[j + 2] == 'i' or palavra[j + 2] == 'o' or palavra[j + 2] == 'u'):
                silabas.append(palavra[j] + palavra[j + 1] + palavra[j + 2])
                j += 1

            elif (palavra[j] != 'a' and palavra[j] != 'e' and palavra[j] != 'i' and palavra[j] != 'o' and palavra[j] != 'u') and (palavra[j + 1] == 'a' or palavra[j + 1] == 'e' or palavra[j + 1] == 'i' or palavra[j + 1] == 'o' or palavra[j + 1] == 'u'):
                silabas.append(palavra[j] + palavra[j + 1])
            j += 1
        # verificando se há duas silabas iguais na palavra
        y = 1
        for a in silabas:
            x = y
            while x < len(silabas):
                if a == silabas[x]:
                    silabas.remove(a)
                x += 1
            y += 1
        # armazenando a palavra total com as silabas (caso haja silabas repetidas e a palavra esteja totalmente no nome do hospital)
        palavra_total = ''
        for g in silabas:
            palavra_total += str(g) + ''
        # verificando se as silabas estão nas silabas do hospital
        silabas_na_palavra = []
        s = 0
        for i in silabas:
            for k in hospital_silabas:
                if i == k:
                    s += 1
                    silabas_na_palavra.append(i)
                else:
                    s += 0
        # se n contém nenhuma
        if s == 0:
            print('Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')
        # se tiver uma silaba
        elif s == 1:
            # saida uma silaba
            if consta == False:
                print(f'Lembrei! A sílaba {silabas_na_palavra[0]} está no nome do hospital. Obrigada, Totoro!')
            # confirmando a silaba no nome do hospital
            for l in silabas_na_palavra:
                for p in hospital_silabas:
                    if l == p:
                        z = l
                        hospital_silabas.remove(z)

        # se tiver mais de uma silaba
        else:
            # verificando se a palavra está no nome do hospital
            g = 0
            while g < int(len(hospital_silabas) - (len(silabas) - 1)):
                # caso seja uma palavra de 6 silabas
                if len(silabas) == 6 and len(hospital_silabas) == 6 and palavra_total == (hospital_silabas[g]+ hospital_silabas[g+1]+ hospital_silabas[g+2] + hospital_silabas[g+3] + hospital_silabas[g+4] + hospital_silabas[5]):
                    print('A palavra', end=' ')
                    print(palavra_total, end=' ')
                    print('está toda no nome do hospital. Acertou em cheio, Totoro!')
                    consta = True
                # caso seja uma palavra de 5 silabas
                elif len(silabas) == 5 and len(hospital_silabas) >= 5 and palavra_total == (hospital_silabas[g]+ hospital_silabas[g+1]+ hospital_silabas[g+2] + hospital_silabas[g+3] + hospital_silabas[g+4]):
                    print('A palavra', end=' ')
                    print(palavra_total, end=' ')
                    print('está toda no nome do hospital. Acertou em cheio, Totoro!')
                    consta = True
                # caso seja uma palavra de 4 silabas
                elif len(silabas) == 4 and len(hospital_silabas) >= 4 and palavra_total == (hospital_silabas[g]+ hospital_silabas[g+1]+ hospital_silabas[g+2] + hospital_silabas[g+3]):
                    print('A palavra', end=' ')
                    print(palavra_total, end=' ')
                    print('está toda no nome do hospital. Acertou em cheio, Totoro!')
                    consta = True
                # caso seja uma palavra de 3 silabas
                elif len(silabas) == 3 and len(hospital_silabas) >= 3 and palavra_total == (hospital_silabas[g]+ hospital_silabas[g+1]+ hospital_silabas[g+2]):
                    print('A palavra', end=' ')
                    print(palavra_total, end=' ')
                    print('está toda no nome do hospital. Acertou em cheio, Totoro!')
                    consta = True
                # caso seja uma palavra de 2 silabas
                elif len(silabas) == 2 and len(hospital_silabas) >= 2 and palavra_total == (hospital_silabas[g]+ hospital_silabas[g+1]):
                    print('A palavra', end=' ')
                    print(palavra_total, end=' ')
                    print('está toda no nome do hospital. Acertou em cheio, Totoro!')
                    consta = True

                g += 1
            # saida caso a palavra não esteja no nome do hospital
            if consta == False:
                print('Lembrei! As sílabas:', end=' ')
                print(*silabas_na_palavra, sep=', ', end=' ')
                print('estão no nome do hospital. Obrigada, Totoro!')
            # confirmando as silabas no nome do hospital
            for m in silabas_na_palavra:
                for n in hospital_silabas:
                    if m == n:
                        w = m
                        hospital_silabas.remove(w)
        # fim da função
        if len(hospital_silabas) == 0:
            print('Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')


# definição do nome do hospital e separação em silabas
hospital = 's,h,i,c,h,i,k,o,k,u,y,a,m,a'.split(',')
hospital_silabas = []

# dividindo o noem do hospital em silabas
h = 0
while h < len(hospital):

    if (hospital[h] == 'c' or hospital[h] == 's') and hospital[h + 1] == 'h' and (hospital[h + 2] == 'a' or hospital[h + 2] == 'e' or hospital[h + 2] == 'i' or hospital[h + 2] == 'o' or hospital[h + 2] == 'u'):
        hospital_silabas.append(hospital[h] + hospital[h + 1] + hospital[h + 2])
        h += 1
    elif (hospital[h] != 'a' and hospital[h] != 'e' and hospital[h] != 'i' and hospital[h] != 'o' and hospital[h] != 'u') and (hospital[h + 1] == 'a' or hospital[h + 1] == 'e' or hospital[h + 1] == 'i' or hospital[h + 1] == 'o' or hospital[h + 1] == 'u'):
        hospital_silabas.append(hospital[h] + hospital[h + 1])
    h += 1
# loop das palavras
while len(hospital_silabas) != 0:
    palavra_total = input()
    nome_do_hospital(palavra_total, hospital_silabas)