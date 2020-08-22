contIdade = homens = mulheres = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).upper()[0].strip()

    if idade >= 18:
        contIdade += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F':
        if idade < 20:
            mulheres += 1
    resp = ''
    while resp not in 'SN':
        resp = input('DESEJA CONTINUAR: [S/N] ').upper()[0].strip()

    if resp == 'N':
        print('Fechando...')
        break

print(f'Pessoas acima de 18 anos: {contIdade}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres menores de 20 anos: {mulheres}')

