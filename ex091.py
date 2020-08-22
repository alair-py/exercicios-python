from random import randint
from time import sleep
from operator import itemgetter
valores = {
        'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)
}
rank = dict()

rank = sorted(valores.items(), key=itemgetter(1), reverse=True)

print(f'{"= RANKING =":=^30}')
for i in range(len(rank)):
    print(f'{i+1}º LUGAR: {rank[i][0]} COM {rank[i][1]} PONTOS!')
    sleep(1)
