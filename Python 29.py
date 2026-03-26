p1= int(input('qual o valor desse produto ?'))
p2= int(input('qual o valor deste outro produto'))
p3= int(input('qual o valor deste outro produto'))

if p1 <= p2 and p1 <= p3:
    print ('o valor do primeiro produto e o  mais barato', p1)
elif p2 <= p1 and p2<= p3:
    print ('o valor do segundo produto e o mais barato', p2)
else :
    print ('o valor do segundo produto e o mais barato', p3)
