from datetime import date

dados = dict()

dados['Nome'] = str(input('SEU NOME: ')).strip().upper()
nasc = int(input('NASCIMENTO: '))
dados['CTPS'] = int(input('Nº CARTEIRA DE TRABALHO: '))
dados['Idade'] = date.today().year - nasc

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
    dados['Salário'] = float(input('SALÁRIO: R$ '))
    dados['Aposentadoria'] = 35 - (date.today().year - dados['Contratação'])
else:
    dados['Aposentadoria'] = 35


print()
for k, v in dados.items():
    print(f'{k} : {v}')

