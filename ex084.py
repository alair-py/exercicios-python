peso = list()
pessoas = list()
dados = list()

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    resp = str(input('Continuar? [s/n] ')).strip().lower()[0]
    if resp == 'n':
        break
    elif resp == 's':
        resp = resp
    else:
        print('Valor inválido!')

print(f'{len(pessoas)} pessoas cadastradas!')

print(f'{max(peso)}KG foi o maior peso cadastrado!', end=' ')
for p in pessoas:
    if p[1] == max(peso):
        print(f'Nome: {p[0]}')

print(f'{min(peso)}KG foi o menor peso cadastrado!', end=' ')
for p in pessoas:
    if p[1] == min(peso):
        print(f'Nome: {p[0]}')


