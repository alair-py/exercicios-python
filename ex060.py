num = int(input('Numero para fatorar: '))
fat = 1
cont = 1

while cont <= num:
    fat *= cont
    cont += 1

print(f'O fatorial de {num} é {fat}')



