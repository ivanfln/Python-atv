horas = float(input('digite as horas trabalhadas: \n'))
salario = horas * 20
print('salario:', salario)

if horas > 40:
    print('tem horas extras')
else:
    print('nao tem horas extras')
