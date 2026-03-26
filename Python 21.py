n1 = float(input('digite a primeira nota :\n'))
n2 = float(input('digite a segunda nota :\n'))
media = (n1 + n2) /2

if media >= 7 :
    print('Aprovado')
elif media >= 5 :
    print('Recuperacao')
else :
    print('Reprovado')
