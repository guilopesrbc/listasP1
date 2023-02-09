#Entrada dos nomes suspeitos e adicionando-s a uma lista:
nomes_suspeitos = input()
lista_suspeitos = nomes_suspeitos.split(',')

#Entrada das frases até sobrar 1 suspeito:
while int(len(lista_suspeitos)) > 1:
    frase = input()
    #Verificações das frases
    if frase == 'Não encontrei nada no primeiro suspeito':
        lista_suspeitos.pop(0)
    elif frase == 'O último da lista está limpo':
        lista_suspeitos.pop(-1)
    elif frase == 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita':
        tam_lista = len(lista_suspeitos)
        meio_lista = int(tam_lista/2)
        lista_suspeitos.pop(meio_lista)
    elif frase == 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:':
        indx = int(input())
        lista_suspeitos.pop(indx)
    elif frase == 'Acho que temos mais uma opção a ser analisada…':
        novo_suspeito = input()
        lista_suspeitos.append(novo_suspeito)
    else:
        print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')
#Saída final
print(f'Acho que encontramos o suspeito. O seu nome é {lista_suspeitos[0]}, vamos salvar o Sam!')