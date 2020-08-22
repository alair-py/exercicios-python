def ficha(j='desconhecido', g=0):
    print(f'O jogador {j} fez {g} gols!')


nome = str(input('NOME DO JOGADOR: ')).strip().upper()
gols = str(input('NUMERO DE GOLS: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)




