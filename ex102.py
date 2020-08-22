def fatorial(a, b=False):
    """
    :param a: O número que será calculado
    :param b: Decidir se mostra calculo ou não
    :return: Retorna fatorial, ou calculo + fatorial
    """

    fat = 1
    for i in range(a, 0, -1):
        fat *= i
        if b:
            print(f'{i}', end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

    return fat


num = int(input('NUMERO PARA FATORIAL: '))
show = str(input('MOSTRAR CALCULO [S/N]: ')).upper()[0].strip()
if show == 'S':
    show = True
elif show == 'N':
    show = False
print(fatorial(num, show))
