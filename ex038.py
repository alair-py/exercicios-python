num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

maior = num1

if num2 > num1:
    maior = num2
    print(f'O segundo valor é maior. {maior}')
elif num1 > num2:
    print(f'O primeiro valor é maior. {maior}')
else:
    print(f'Os valores {num1} e {num2} são iguais')
