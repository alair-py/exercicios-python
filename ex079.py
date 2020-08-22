num = list()

while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in num:
        num.append(valor)
    resp = ''
    resp = input('Continuar? [s/n] ').strip().lower()[0]
    if resp == 'n':
        break
    elif resp == 's':
        resp = 's'
    else:
        print('Resposta inválida!')

num.sort()
print(num)
