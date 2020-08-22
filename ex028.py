from random import randint

num = randint(0, 5)

resp = int(input('Digite um numero de 1 a 5: '))

if num == resp:
    print(f'Sorteado foi {num}, PARABÉNS!')
else:
    print(f'Sorteado foi {num}, SINTO MUITO!')
