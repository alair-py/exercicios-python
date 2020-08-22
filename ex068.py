from random import randint
from time import sleep
cont = 0
while True:
    comput = randint(0, 10)
    jogador = str(input('IMPAR OU PAR? ')).upper()
    num = int(input('Valor: '))
    print('UM...', end=' ')
    sleep(0.5)
    print('DOIS...', end=' ')
    sleep(0.5)
    print('TRÊS...', end=' ')
    sleep(0.5)
    print('JÁ!')

    result = comput + num
    print(f'Computador: {comput}. Jogador: {num}. Resultado: {result}!')
    if result % 2 == 0:
        result = 'PAR'
        if result == jogador:
            print('VENCEU!')
            cont += 1
        else:
            print('PERDEU!')
            print(f'Venceu {cont} vezes seguidas!')
            break
    else:
        result = 'IMPAR'
        if result == jogador:
            print('VENCEU!')
            cont += 1
        else:
            print('PERDEU!')
            print(f'Venceu {cont} vezes seguidas!')
            break
