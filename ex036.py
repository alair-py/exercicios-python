# AVALIAR EMPRESTIMO
valor = float(input('Qual valor do imóvel: R$ '))
salario = float(input('Qual salário do comprador: R$ '))
tempo = int(input('Em quantos anos deseja pagar: '))


mensal = valor / (tempo * 12)

if mensal < 0.3 * salario:
    print('EMPRESTIMO APROVADO!')
    print(f'Valor da prestação R$ {mensal:.2f} em {tempo * 12} meses.')
else:
    print('EMPRESTIMO NEGADO! LAMENTAMOS.')
    print(f'Valor da prestação R$ {mensal:.2f} excedeu 30% do salário')
