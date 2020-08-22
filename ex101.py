def voto(a=0):
    from datetime import date
    idade = date.today().year - a
    if idade < 16:
        return 'VOTO NEGADO'
    elif 16 <= idade < 18:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


nasc = int(input('ANO DE NASCIMENTO: '))
print(f'RESULTADO: {voto(nasc)}')
