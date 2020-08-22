from utilidades import moeda
from utilidades import dado

p = dado.leiadinheiro('VALOR: ')
aumentar = float(input('AUMENTAR EM QUANTO %: '))
reduzir = float(input('REDUZIR EM QUANTO %: '))
moeda.resumo(p, aumentar, reduzir)
