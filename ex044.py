valor = float(input('PREÇO NORMAL DO PRODUTO: R$ '))

print('''[1] PARA PAGAMENTO À VISTA (DINHEIRO/CHEQUE)
[2] PARA PAGAMENTO À VISTA (CARTÃO)
[3] PARA PARCELAR 2X NO CARTÃO
[4] PARA PARCELAR 3X OU MAIS NO CARTÃO''')

pag = int(input('FORMA DE PAGAMENTO: '))

if pag == 1:
    total = valor - (valor * 0.10)
    print(f'À VISTA (DINHEIRO/CHEQUE): R$ {total:.2f}')
elif pag == 2:
    total = valor - (valor * 0.05)
    print(f'À VISTA (CARTÃO): R$ {total:.2f}')
elif pag == 3:
    total = valor
    parc = total / 2
    print(f'2X NO CARTÃO: R$ {total:.2f} em 2x parcelas de R$ {parc:.2f}')
elif pag == 4:
    parc = int(input('Quantas vezes? '))
    total = valor + (valor * 0.20)
    final = total / parc
    print(f'{parc}X NO CARTÃO: R$ {total:.2f}. Cada parcela: R$ {final:.2f}')
else:
    print('Opção inválida de pagamento!')

print('OBRIGADO!')
