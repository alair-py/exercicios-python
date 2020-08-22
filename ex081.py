num = list()

while True:
    num.append(int(input('Valor: ')))
    resp = ''
    resp = input('Continuar: [s/n] ').strip().lower()[0]
    if resp == 'n':
        break
    elif resp not in 'ns':
        print('Resposta inválida!')

print(f'Foram digitados {len(num)} valores.')
num.sort(reverse=True)
print(f'Valores decrescente: {num}')
if num.count(5):
    print('O número 5 está lista!')
else:
    print('O número 5 não está na lista!')

