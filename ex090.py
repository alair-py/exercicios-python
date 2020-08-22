dados = dict()

dados['Nome'] = str(input('NOME DO ALUNO: '))
dados['Média'] = float(input('MÉDIA: '))
if dados['Média'] < 7:
    dados['Situação'] = 'Reprovado'
else:
    dados['Situação'] = 'Aprovado'

print(f'NOME: {dados["Nome"]} > SITUAÇÃO: {dados["Situação"]}')

