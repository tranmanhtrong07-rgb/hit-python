import math
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
print('phuong trinh:', a, 'x^2 +', b, 'x +', c)
if(a == 0):
    print('khong ton tai phuong trinh bac 2')
else:
    delta = b**2-4*a*c
    if(delta<0):
        print('phuong trinh vo nghiem')
    elif(delta==0):
        x= -(b/(2*a))
        print('phuong trinhh co nghiem kep x1= x2=', x)
    else:
        x1= (-b+math.sqrt(delta))/(2*a)
        x2= (-b-math.sqrt(delta))/(2*a)
        print('phuong trinh co 2 nghiem phan biet x1=', x1, ', x2=', x2)