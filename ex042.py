n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

cor = {'azul': '\033[34m',
       'amarelo': '\033[33m',
       'limpa': '\033[m'
       }

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('É possivel formar um triangulo: ')
    if n1 == n2 and n2 == n3:
        print('{}Equilátero{}'.format(cor['amarelo'], cor['limpa']))
    elif n1 != n2 and n2 != n3 and n3 != n1:
            print('{}Escaleno{}'.format(cor['amarelo'], cor['limpa']))
    else:
            print('{}Isósceles{}'.format(cor['amarelo'], cor['limpa']))
else:
    print('Não é possivel formar um {} triangulo {}!'.format(cor['azul'], cor['limpa']))

