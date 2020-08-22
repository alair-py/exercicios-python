num = int(input('Digite um número inteiro para conversão: '))

print('''Deseja converter para qual sistema:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')

resp = int(input('QUAL OPÇÃO: '))

if resp == 1:
    print(f'{num} para BINÁRIO é {bin(num)[2:]}')
elif resp == 2:
    print(f'{num} para OCTAL é {oct(num)[2:]}')
elif resp == 3:
    print(f'{num} para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção inválida!')
