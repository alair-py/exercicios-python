num = int(input('Qual distância da viagem: '))

if num <= 200:
    total = num*0.50
    print(f'{num} km. Valor: R${total:.2f}')
else:
    total = num*0.45
    print(f'{num} km. Valor: R${total:.2f}')

