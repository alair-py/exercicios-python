jogador = dict()
partidas = []
final = []
gols = []

while True:
    jogador['nome'] = str(input('NOME DO JOGADOR: ')).strip().upper()
    total = int(input('TOTAL DE PARTIDAS: '))

    for c in range(0, total):
        partidas.append(int(input(f'QUANTOS GOLS {jogador["nome"]} FEZ NA {c + 1} PARTIDA? ')))

    gols.append(partidas[:])
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    final.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    resp = str(input('CONTINUAR [s/n]: ')).strip().lower()[0]
    if resp == 'n':
        break
    elif resp == 's':
        continue
    else:
        print('Resposta inválida!')


print()
print(f'{" RESULTADO ":=^30}')
print(f'{"Nº":^3}{"JOGADOR":^20}{"GOLS":^5}')
for i, c in enumerate(final):
    print(f'{i+1:<3}{c["nome"]:^20}{c["Total"]:^3}')

print(f'{" GOLS POR PARTIDA ":=^30}')
while True:
    busca = int(input('DADOS DE QUAL JOGADOR? [999 para SAIR]: '))
    if busca == 999:
        break
    elif busca >= len(final):
        print('Valor inválido!')
    busca -= 1
    print(f'MOSTRANDO DADOS DO JOGADOR {final[busca]["nome"]}: ')
    for i, g in enumerate(final[busca]['Gols']):
        print(f'> {g} GOLS NA {i + 1}º PARTIDA')
    print()
