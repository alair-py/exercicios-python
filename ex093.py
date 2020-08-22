final = dict()
gols = list()
final['nome'] = str(input('NOME DO JOGADOR: ')).strip().upper()
part = int(input('QUANTAS PARTIDAS JOGADAS: '))
for i in range(1, part + 1):
    gol = int(input(f'GOLS NA PARTIDA {i}: '))
    gols.append(gol)


final['Gols'] = (gols.copy())

totgols = 0
for i in range(len(gols)):
    totgols += gols[i]

print()
print(f'{" RESULTADO ":=^40}')
print(f'NOME: {final["nome"]} > TOTAL: {totgols} GOLS EM {part} PARTIDAS.')
print()
for i in range(len(gols)):
    print(f'NA {i+1}º PARTIDA FEZ: {gols[i]} GOLS')

