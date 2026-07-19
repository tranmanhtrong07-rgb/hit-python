import math
n= int(input('n='))
while(n<0):
    print('n phai la so duong')
    n= int(input('n='))
if(n<2):
    print('n khong phai so nguyen to')
else:
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            print('n khong la so nguyen to')
            break
        else:
            print('n la so nguyen to')