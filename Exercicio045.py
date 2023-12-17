from random import randint
from time import sleep
item = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint(0 , 2 )
print('''SUAS OPÇOES 
[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOOO!!!')
sleep(1)
print('**' * 20)
print('O computador escolheu {}'.format(item [computador]))
print('O jogador escolheu {}'.format(item [jogador]))
print('**' * 20)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('OPÇÃO INVALIDA')
if computador == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador ganha')
    else:
        print('OPÇÃO INVALIDA')
if computador == 2:
    if jogador == 0:
        print('O jogador vence')
    elif jogador == 1:
        print('O computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('OPÇÃO INVALIDA')