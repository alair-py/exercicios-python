# PALINDROMO

frase = input('Digite uma frase: ')

fraseSespaco = frase.replace(' ', '')
frasemin = fraseSespaco.lower()
fraseinvert = frasemin[::-1]

if fraseSespaco == fraseinvert:
    print(f'Digitou [{frase}], invertido é [{fraseinvert}]. É um PALINDROMO!')
else:
    print('Não é um PALINDROMO!')
