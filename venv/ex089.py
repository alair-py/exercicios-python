dados = []

while True:
    nome = str(input('Nome: ')).strip().upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    resp = str(input('CONTINUAR? [s/n]: ')).lower()[0].strip()
    if resp == 'n':
        break
    elif resp == 's':
        continue
    else:
        print('Resposta inválida!')


print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')


print(f'{"= VERIFICAR NOTAS CADASTRADAS POR ALUNO =":=^10}')
while True:
    print('')
    cad = int(input('VER NOTAS DO ALUNO NÚMERO [999 PARA SAIR] > Nª: '))
    if cad == 999:
        break
    if cad <= len(dados) - 1:
        print(f'NOTAS DO ALUNO: {dados[cad][0]} > NOTAS: {dados[cad][1]}')


