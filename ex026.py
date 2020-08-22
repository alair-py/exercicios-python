frase = str(input('Digite uma frase: ')).strip()


print('A frase tem '), frase.lower().count('a')
print('O primeiro (A) está na posição: '), frase.lower().find('a')
print('O ultimo (A) está na posição: '), frase.lower().rfind('a')
