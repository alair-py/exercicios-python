vel = int(input('Velocidade do carro: '))

if vel > 80:
    print(f'{vel} km/h: Velocidade ACIMA do permitido')
    valor = 7*(vel-80)
    print(f'Valor da multa: R${valor:.2f}')
else:
    print(f'{vel} km/h: Velocidade DENTRO do permitido')

