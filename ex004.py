n = input('Digite algo: ')

print('O tipo primitivo de {} é {}' .format(n, type(n)))
print('{} possui espaços: {}'.format(n, n.isspace()))
print('{} é um numero: {}'.format(n, n.isnumeric()))
print('{} é alfabetico: {}'.format(n, n.isalpha()))
print('{} é alfanumerico: {}'.format(n, n.isalnum()))
print('{} está somente em maisculas: {}'.format(n, n.isupper()))
print('{} está somente em minusculas: {}'.format(n, n.islower()))



print(f'o valor digitado foi {n}')

