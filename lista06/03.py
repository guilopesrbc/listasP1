# função para definir a vida do vilão
def vida_vilao(vilao,vida):
    if vilao == 'Vingador':
        vida = 30
        return vida
    elif vilao == 'Tiamat':
        vida = 20
        return vida
    elif vilao == 'Vingador das Sombras':
        vida = 14
        return vida
    else:
        vida = 9
        return vida
# dicionarios com informações
grupo_arma = {'Bobby': 'grande espada', 'Diana': 'dardo',
        'Eric': 'grande espada', 'Hank': 'espada',
         'Presto': 'cajado' ,'Sheila': 'espada','Uni': 'chifre'}

grupo_armadura = {'Bobby': 'armadura media', 'Diana': 'armadura leve',
        'Eric': 'armadura pesada', 'Hank': 'armadura media',
         'Presto': 'armadura leve' ,'Sheila': 'armadura leve','Uni': 'armadura leve'}

armas = {'chifre': 2 ,'cajado': 4 ,'espada': 6 ,'grande espada': 8 ,'dardo': 12 }

armaduras = {'armadura leve' : 3, 'armadura media' : 1, 'armadura pesada' : 0 }

# definições e entradas
aux = []
vilao = input()
turnos = int(input())
vida = 0
vida = vida_vilao(vilao, vida)
check = False
# loop da luta
while turnos > 0:
    heroi = input()
    # caso apareça o mestre dos magos
    if heroi == 'Mestre dos Magos':
        print('Muito obrigado amigo, que nos vejamos novamente um dia')
        check = True
        break
    # armazenando valor de acrescimo do progresso do vilao e o dano da arma
    acres_prog = armaduras.get(grupo_armadura.get(heroi))
    arma_utilizada = armas.get(grupo_arma.get(heroi))
    # golpe
    vida -= arma_utilizada
    # caso o vilao morra
    if vida <= 0:
        print(f'{heroi} executou o ultimo golpe em {vilao}, estamos livres!')
        check = True
        break
    # salvando o progresso caso não seja derrotado
    turnos -= acres_prog
    turnos -= 1
# caso o vilao não tenha sido derrotado
if check == False:
    print(f'Oh nao, {vilao} e muito forte, este e o fim!')