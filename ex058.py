from random import randint

comput = randint(1, 10)
cont = 1
resp = int(input('Adivinhe qual número de 1 a 10: '))

while resp != comput:
    print(f'{resp} - Errado...')
    resp = int(input('Tente novamente, entre 1 e 10: '))
    cont += 1
    if resp < comput:
        print('Mais...')
    else:
        print('Menos...')

print(f'Chutou: {resp}, Computador foi: {comput}, precisou de {cont} tentativas')
