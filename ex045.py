# JO KEN PO
import random
from time import sleep

jokenpo = ['Pedra', 'Papel', 'Tesoura']
comput = random.choice(jokenpo)

print('''[1] PEDRA
[2] PAPEL
[3] TESOURA''')

resp = int(input('QUAL ESCOLHA: '))

print('JO...')
sleep(0.5)
print('KEN...')
sleep(0.5)
print('PO...')
sleep(0.5)

if comput == 'Pedra' and resp == 2:
    print(f'''COMPUTADOR: {comput}; VOCÊ: Papel.
    VOCÊ GANHOU!''')
elif comput == 'Papel' and resp == 3:
    print(f'''COMPUTADOR: {comput}; VOCÊ: Tesoura. 
    VOCÊ GANHOU!''')
elif comput == 'Tesoura' and resp == 1:
    print(f'''COMPUTADOR: {comput}; VOCÊ: Pedra.
    VOCÊ GANHOU!''')
elif comput == 'Pedra' and resp == 3:
    print(f'''COMPUTADOR: {comput}; VOCÊ: Tesoura.
    VOCÊ PERDEU!''')
elif comput == 'Papel' and resp == 1:
    print(f'''COMPUTADOR: {comput}; VOCÊ: Pedra.
    VOCÊ PERDEU!''')
elif comput == 'Tesoura' and resp == 2:
    print(f'''COMPUTADOR: {comput}; VOCÊ: Papel
    VOCÊ PERDEU!''')
else:
    print(f'COMPUTADOR: {comput}. EMPATE!')
