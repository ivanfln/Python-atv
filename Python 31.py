peso = float(input('digite o seu peso : \n'))
altura = float(input('digite a sua altura :\n'))

imc = peso / (altura ** 2)

print('IMC:', imc)

if imc < 18.5:
    print('esta abaixo do peso')
elif imc <= 24.9:
    print('peso normal')
else :
    print('acima do peso')
