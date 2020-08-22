nome = str(input('Digite seu nome: ')).strip()

lista = nome.split()
ultimo = lista[-1]
penultimo = lista[-2]

print(f'O primeiro nome é {lista[0]}')
print(f'O ultimo nome é {ultimo}')
print(f'O penultimo nome é {penultimo}')