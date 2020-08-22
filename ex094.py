
cadastros = list()
dados = dict()
media = soma = 0
while True:
    dados['nome'] = str(input('NOME: ')).strip().upper()
    dados['sexo'] = str(input('SEXO: [M/F] ')).strip().upper()[0]
    dados['idade'] = int(input('IDADE: '))
    cadastros.append(dados.copy())
    soma += dados['idade']
    resp = str(input('CONTINUAR [s/n]: ')).upper()
    if resp == 'N':
        break
    elif resp == 'S':
        continue
    else:
        print('Resposta inválida!')

media = soma / len(cadastros)
print(f'{" RESULTADO ":=^30}')
print(f'PESSOAS CADASTRADAS: {len(cadastros)}')
print(f'MÉDIA DE IDADE DO GRUPO: {media}')

print('MULHERES CADASTRADAS: ', end='')
for i in range(len(cadastros)):
    if cadastros[i]["sexo"] == 'F':
        print(f'{cadastros[i]["nome"]};', end='')

print()

print('PESSOAS COM IDADE ACIMA DA MÉDIA: ', end='')
for i in range(len(cadastros)):
    if cadastros[i]["idade"] > media:
        print(f'{cadastros[i]["nome"]}; ', end='')


