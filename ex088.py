from random import randint
from time import sleep

palpites = []

resp = int(input('Quantos jogos para gerar: '))

for i in range(resp):
    jogos = []
    for j in range(0, 6):
        n = randint(1, 60)
        if n in jogos:
            n = randint(1, 60)
            jogos.append(n)
        else:
            jogos.append(n)

    jogos.sort()
    palpites.append(jogos[:])
    print(f'Jogo {i + 1}: {palpites[i]}')
    sleep(0.5)

print('')
print(f'{" = BOA SORTE = ":~^35}')
