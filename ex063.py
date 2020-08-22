num1 = int(input('NUMERO PARA FIBONACCI: '))

fib1 = 0
fib2 = 1
c = 0
while c <= num1:
    fib3 = fib1 + fib2
    print(fib3, end=' ')
    fib1 = fib2
    fib2 = fib3
    c += 1

