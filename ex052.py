# NUMERO PRIMO

num = int(input('DIGITE UM NUMERO: '))

mult = 0

for c in range(1, num + 1):
    if num % c == 0:
        print(f'{num} é divisivel de {c}')
        mult += 1

if mult == 2:
    print(f'{num} é PRIMO!')
else:
    print(f'{num} NÃO é PRIMO!')

