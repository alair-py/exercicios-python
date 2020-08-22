def leiadinheiro(msg):
    valor = str(input(msg)).replace(',', '.').strip()
    while True:
        if valor.isalpha() or valor == '':
            print('APENAS NÚMEROS!')
            valor = input('VALOR: ')
        else:
            return float(valor)

