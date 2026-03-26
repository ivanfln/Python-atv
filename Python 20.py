a = int(input('digite um numero : '))
b = int(input('digite outro numero : '))
c = int(input('digite mais outro numero : '))

if a >= b and a >=c:
    print('O numero maior é : ' , a)
elif b >= a and b >=c:
    print('O numero maior é : ' , b)
else :
    print('O numero maior é : ' , c)
