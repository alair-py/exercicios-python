dias = int(input('Quantos dias ficou alugado: '))
kms = int(input('Quantos KMs foram percorridos: '))

valor = (dias * 60) + (kms * 0.15)

print(f'O valor a pagar por {dias} dias e {kms} km rodados é: R$ {valor:.2f}')
