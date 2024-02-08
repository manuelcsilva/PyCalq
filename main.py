print('--Calculadora--')
n1 = int(input('Número 1: '))
op = input('Operação(+, -, x, :): ')
n2 = int(input('Número 2: '))

if op == '+':
  r = n1 + n2
elif op == '-':
  r = n1 - n2
elif op == 'x':
  r = n1 * n2
else:
  r = n1 / n2
print(f'O resultado de {n1} {op} {n2} é {r}')
