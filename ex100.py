from random import randint

sorteados = list()


def sorteia():
    for i in range(0, 5):
        num = randint(0, 100)
        sorteados.append(num)


def somapar():
    soma = 0
    for i in sorteados:
        if i % 2 == 0:
            soma += i
    print(f'A SOMA DOS PARES SORTEADOS É {soma}')


sorteia()
somapar()
print(f'OS SORTEADOS FORAM: {sorteados}')

