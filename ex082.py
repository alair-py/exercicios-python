num = list()
numPar = list()
numImpar = list()

while True:
    num.append(int(input('Valor: ')))
    resp = ''
    resp = input('Continuar: [s/n] ').strip().lower()[0]
    if resp == 'n':
        break
    elif resp not in 'sn':
        print('Resposta inválida!')


for i in range(len(num)):
    if num[i] % 2 == 0:
        numPar.append(num[i])
    else:
        numImpar.append(num[i])

print(num)
print(numPar)
print(numImpar)
