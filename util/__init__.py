cadastrados = dict()
cadfinal = list()


def cadastro(valor):
    nome = str(input('NOME: ')).strip().upper()
    while True:
        try:
            idade = int(input('IDADE: '))
            break
        except (TypeError, ValueError):
            print('VALOR INVÁLIDO!')

    try:
        a = open(valor, 'at')
    except:
        print('Erro ao abrir!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao cadastrar!')
        else:
            print('Cadastrado com Sucesso!')
            a.close()
    menu(valor)


def vercads(valor):
    print('-' * 30)
    print(f'{" NOMES CADASTRADOS ":^30}')
    print('-' * 30)
    try:
        a = open(valor, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>3} ANOS')
    menu(valor)


def menu(valor):
    print('-' * 30)
    print(f'{" MENU PRINCIPAL ":^30}')
    print('-' * 30)
    print('''1 - CADASTRAR PESSOA
2 - VER LISTA CADASTRADA
3 - SAIR DO PROGRAMA
    ''')
    while True:
        try:
            resp = int(input('OPÇÃO: '))
            if resp == 1:
                cadastro(valor)
                break
            elif resp == 2:
                vercads(valor)
                break
            elif resp == 3:
                print('SAINDO...')
                break
            else:
                print('OPÇÃO INVÁLIDA.')
        except (ValueError, TypeError):
            print('ERRO! Valor inválido!')


def testararq(valor):
    try:
        a = open(valor, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(valor):
    try:
        a = open(valor, 'wt+')
        a.close()
    except:
        print('Ocorreu erro na criação do arquivo')
    else:
        print(f'Arquivo {valor} criado com sucesso')
