#variaveis e definicoes
fim = False
feito = 0
xingamento = False
bazinga = False
#programa e saídas
while (fim == False):
    mensagem = input()
#xingamentos
    if mensagem == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or mensagem == 'Leonard seu anão covarde' or mensagem == 'Tu é muito burro Raj':
        print('Não xingue seus amigos Sheldon!')
        xingamento = True
#bazingas anula o feito
    elif (mensagem == 'Bazinga') and (xingamento == False) and (bazinga == False):
        feito -= 1
        bazinga = True
    elif(mensagem == 'Bazinga') and (xingamento == True):
        feito += 0
    #sem nobel
    elif (feito == 0) and (mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Que potencial desperdiçado...')
        xingamento = False
        fim = True
    elif (feito == 1) and (mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Tão perto, mas tão longe')
        xingamento = False
        fim = True
    elif (feito == 2) and (mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Tão perto, mas tão longe')
        xingamento = False
        fim = True
    elif (feito == 3) and (mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Não desista Sheldon, você ainda têm muito para alcançar!')
        xingamento = False
        fim = True
    elif (feito == 4) and (mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Nãoooooo, esse momento ia ser seu Sheldon')
        xingamento = False
        fim = True
    elif (feito == 5) and (mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Nãoooooo, esse momento ia ser seu Sheldon')
        xingamento = False
        fim = True

#feitos e nobel
    elif (feito == 0) and (mensagem == 'Começou a Trabalhar na Caltech'):
        feito += 1
        xingamento = False
        bazinga = False
    elif (feito == 1) and (mensagem == 'Trabalho sobre a String Theory'):
        feito += 1
        xingamento = False
        bazinga = False
    elif (feito == 2) and (mensagem == 'Ganhar o Chancellor de ciência'):
        feito += 1
        xingamento = False
        bazinga = False
    elif (feito == 3) and (mensagem == 'Pensar na Teoria de Cooper-Hofstader'):
        feito += 1
        xingamento = False
        bazinga = False
    elif (feito == 4) and (mensagem == 'Criou a Super Assimetria'):
        feito += 1
        xingamento = False
        bazinga = False
    elif (feito == 5) and (mensagem == 'Ganhar o Nobel'):
        print('Você conseguiu Sheldon, o Nobel é seu!!!')
        xingamento = False
        bazinga = False
        fim = True
    else:
        xingamento = True