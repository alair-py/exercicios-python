num = 0
quant = -1
soma = 0

while num != 999:
    quant += 1
    soma += num
    num = int(input('Digite um número: [999 - Para sair]: '))

print(f'A soma dos números digitados é: {soma}')
print(f'A quantidade de números digitados foi: {quant}')

