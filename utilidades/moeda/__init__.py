def metade(preco, show=False):
    preco /= 2
    if show:
        return f'R${preco:.2f}'
    else:
        return preco


def dobro(preco, show=False):
    preco *= 2
    if show:
        return f'R${preco:.2f}'
    else:
        return preco


def moeda(preco):
    return f'R$ {preco:.2f}'


def resumo(preco, aum=0, red=0):
    precmais = 0
    precmenos = 0
    print('-' * 30)
    print(f'{" RESUMO ":=^30}')
    print('-' * 30)
    print(f'{"VALOR ANALISADO:"} \t {moeda(preco)}')
    print(f'{"DOBRO DO VALOR:"} \t {moeda(dobro(preco))}')
    print(f'{"METADE DO VALOR:"} \t {moeda(metade(preco))}')
    precmais = preco + (preco*(aum/100))
    print(f'{aum}{"% DE AUMENTO:"} \t {moeda(precmais)}')
    precmenos = preco - (preco*(red/100))
    print(f'{red}{"% DE REDUÇÃO:"} \t {moeda(precmenos)}')
