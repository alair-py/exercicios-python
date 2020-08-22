dados = list()
valoresP = list()
valoresI = list()

for i in range(0, 7):
    dados.append(int(input('Valor: ')))

for i in dados:
    if i % 2 == 0:
        valoresP.append(i)
    else:
        valoresI.append(i)

dados.clear()
valoresI.sort()
valoresP.sort()
dados.append(valoresI[:])
dados.append(valoresP[:])
dados.sort()
print(dados)
