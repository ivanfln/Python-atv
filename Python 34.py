a = float(input('lado 1: \n'))
b = float(input('Lado 2: \n'))
c = float(input('Lado 3: \n'))

if a + b > c and a + c > b and b + c > a:
    print('forma um triangulo')
else:
    print('nao forma um triangulo')