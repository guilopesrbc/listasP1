# Entradas dos nomes, qtds, filmes e notas:
dono = input()
qtd = int(input())
lista_final = []
filmes = ''
notas = []
lista_int = []
# Loop para dividir o nome dos filmes e as notas
for i in range(qtd):
    filmes_notas = input()
    lista_filmes_notas = filmes_notas.split(' - ')
    #adicionando em float, as notas a uma lista
    notas.append(float(lista_filmes_notas[1]))
    #fixando os valores da lista split em uma lista intermediaria, para não resetar no loop
    lista_int.append(lista_filmes_notas)
#ordenando as notas corretamente em ordem decrescente
for z in range(len(notas)):
    for j in range(0, len(notas) - z - 1):
        if notas[j] < notas[j + 1]:
            temp = notas[j]
            notas[j] = notas[j + 1]
            notas[j + 1] = temp


#encontrando as notas nos elementos da lista intermediaria e adicionando o filme junto com a nota a uma lista final
for x in notas:
    for y in lista_int:
        if x == float(y[1]):
            lista_final.append(f'{y[0]} - {x}')

# Imprimir o dono e os filmes sugeridos em notas decrescentes
print(f'Os filmes sugeridos por {dono} são:')
for n in lista_final:
    print(n)








