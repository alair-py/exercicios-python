notaslist = list()


def notas(* num):
    '''
    :param num: Recebe vários valores passados por lista
    :return: Retorna um dicionário c/ valores calculados
    '''

    notdict = {}
    media = sum(notaslist) / len(notaslist)
    if media < 6:
        sit = 'RUIM'
    else:
        sit = 'BOA'

    notdict['Quantidade'] = len(notaslist)
    notdict['Maior nota'] = max(notaslist)
    notdict['Menor nota'] = min(notaslist)
    notdict['Média'] = media
    notdict['Situação'] = sit

    return notdict


while True:
    n = float(input('NOTA: '))
    notaslist.append(n)
    resp = str(input('CONTINUAR [s/n]: ')).strip().lower()[0]
    if resp == 'n':
        break
    elif resp == 's':
        continue
    else:
        print('RESPOSTA INVÁLIDA!')
print(notas(notaslist))
help(notas)
