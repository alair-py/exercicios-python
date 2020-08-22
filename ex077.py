pal = (
        'caderno', 'celular', 'teclado', 'monitor',
        'sorvete', 'mulher', 'caneca', 'cadeira',
        'controle', 'roteador', 'porta'
)

for c in pal:
    print(f'\nNa palavra {c.upper()} temos as vogais: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
