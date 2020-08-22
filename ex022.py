nome = str(input('Digite um nome: ')).strip()

print(f'{nome.upper()}')
print(f'{nome.lower()}')
print(len(nome) - nome.count(' '))

dividido = nome.split()
print(f'Seu primeiro nome é {dividido[0]} e tem {len(dividido[0])} letras')
print(f'Seu segundo nome é {dividido[1]} e tem {len(dividido[1])} letras')
print(f'Seu terceiro nome é {dividido[2]} e tem {len(dividido[2])} letras')

# oooooooooouuuuuu

print(nome.find(' '))
