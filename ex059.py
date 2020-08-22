resp = 0

while resp != 5:
    num1 = float(input('Primeiro valor: '))
    num2 = float(input('Segundo valor: '))
    print('''O QUE DESEJA:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR ENTRE OS DOIS
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    resp = int(input(' '))
    if resp == 1:
        print(f'A soma de {num1} + {num2} é: {num1 + num2}')
        resp = 5
    elif resp == 2:
        print(f'A multiplicação de {num1} x {num2} é: {num1 * num2}')
        resp = 5
    elif resp == 3:
        if num1 > num2:
            print(f'O maior entre {num1} e {num2} é: {num1}')
        elif num2 > num1:
            print(f'O maior entre {num1} e {num2} é: {num2}')
        else:
            print(f'{num1} e {num2} são iguais.')
        resp = 5
    elif resp ==4:
        num1 = float(input('Primeiro valor: '))
        num2 = float(input('Segundo valor: '))
        print('''O QUE DESEJA:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR ENTRE OS DOIS
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
        resp = int(input(' '))
    elif resp == 5:
        print('FECHANDO...')
    else:
        print('DIGITE UMA OPÇÃO VÁLIDA!')
