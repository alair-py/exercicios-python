# CALCULO IMC 

alt = float(input('Sua altura > Ex: 1.72: '))
peso = float(input('Seu peso >  Ex: 62: '))

imc = peso / (alt**2)

if imc < 18.5:
    print(f'IMC: {imc:.2f}. ABAIXO DO PESO IDEAL')
elif 18.5 <= imc < 25:
    print(f'IMC: {imc:.2f}. PESO IDEAL')
elif 25 <= imc < 30:
    print(f'IMC: {imc:.2f}. SOBREPESO')
elif 30 <= imc < 40:
    print(f'IMC: {imc:.2f}. OBESIDADE')
else:
    print(f'IMC: {imc:.2f}. OBESIDADE MÓRBIDA')

