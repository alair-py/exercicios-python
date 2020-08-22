while True:
    num = int(input('Tabuada de qual valor? '))
    c = 1
    if num < 0:
        break
    print('-' * 25)

    while c < 11:
        print(f'{num} x {c} = {num * c}')
        c += 1

