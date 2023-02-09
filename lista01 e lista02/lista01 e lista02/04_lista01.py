#dados das cidades
cidade_um = input('digite aqui o nome da primeira cidade:').title()
nota_um = float(input('digite aqui a nota da primeira cidade:'))
distancia_um = int(input('distancia em km da primeira cidade:'))

cidade_dois = input('digite aqui o nome da segunda cidade:').title()
nota_dois = float(input('digite aqui a nota da segunda cidade:'))
distancia_dois = int(input('distancia em km da segunda cidade'))

cidade_tres = input('digite aqui o nome da terceira cidade:').title()
nota_tres = float(input('digite aqui a nota da terceira cidade:'))
distancia_tres = int(input('distancia em km da terceira cidade'))
#resultado final das cidades
if ((nota_um < 4.0) and (nota_dois < 4) and (nota_tres < 4)):
    print('Nota mínima não atingida')
elif ((nota_um >= 4.0) and (nota_um > nota_dois) and (nota_um > nota_tres) or (distancia_um < distancia_dois) or (distancia_um < distancia_dois)):
    print(cidade_um)
elif ((nota_dois >= 4.0) and (nota_dois > nota_tres) or (distancia_dois < distancia_tres) or (distancia_dois < distancia_um)):
    print(cidade_dois)
elif ((nota_tres >= 4.0) or (distancia_tres < distancia_dois) or (distancia_tres < distancia_um)):
    print(cidade_tres)

