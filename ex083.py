parent = list()

expr = str(input('Expressão: '))

for caract in expr:
    if caract == '(':
        parent.append(caract)
    elif caract == ')':
        if len(parent) > 0:
            parent.pop()
        else:
            parent.append(caract)


if len(parent) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')

