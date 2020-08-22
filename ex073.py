times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
         'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense',
         'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('Primeiros colocados: ')
for cont in range(0, 5):
    print(f'{cont + 1}º lugar - {times[cont]}')

print('')
print('Últimos colocados: ')
for cont in range(-4, 0):
    print(f'{times[cont]}')

print('')
print('Ordem alfabética: ')
print(sorted(times))

print('')
print(f'Chapecoense está em {times.index("Chapecoense")+1}º lugar')