#variáveis
parar = False
temperatura = 30
fome = True
internet = 0

#entradas e somatórios
while (parar == False):
    acao = input()
    if acao == 'parar':
        parar = True
    elif acao == 'ir para o grad':
        temperatura -= 5
        internet += 300
    elif acao == 'sair para a rua':
        temperatura += 5
    elif acao == 'comer uma quentinha':
        fome = False
    elif acao == 'conectar no wifi':
        internet += 100
    else:
        print('Entrada inválida')
#saídas
if temperatura >= 30:
    print('A temperatura aqui não está agradável')
elif temperatura <= 25:
    print('Agora sim, está aconchegante')
if fome == True:
    print('Meu corpo precisa de comida')
if internet < 100:
    print('Essa conexão está horrível')
if fome == False and temperatura <= 25 and internet >= 300:
    print('Finalmente um lugar preciso para mim!')

