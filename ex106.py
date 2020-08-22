def ajuda():
    print('-' * 30)
    print(f'{" SISTEMA DE AJUDA ":^30}')
    print('-' * 30)
    while True:
        resp = str(input('FUNÇÃO OU BIBLIOTECA [N para sair] > ')).strip().lower()
        if resp == 'n':
            print('SAINDO...')
            break
        else:
            help(resp)


ajuda()
