
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    num = int(input('Digite um número de 0 a 20: '))
    while num < 0 or num > 20:
        num = int(input('Valor inválido! Digite um número de 0 a 20: '))

    print(f'Digitou o número: {extenso[num]}')

