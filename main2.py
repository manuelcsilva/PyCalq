print('--PyCalq--')

def calq(n1, op, n2):
    if op == '+':
        r = n1 + n2
        print(r)
    elif op == '-':
        r = n1 - n2
    elif op == 'x':
        r = n1 * n2
    else:
        r = n1 / n2
    return r