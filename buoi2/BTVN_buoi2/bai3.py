import math
n = int(input())
n = abs(n)
if(n == 0):
    dem = 1
    tong = 0
else:
    dem = 0
    tong = 0
    while(n > 0):
        dem += 1
        tong += n % 10
        n //= 10
print('So chu so: ', dem)
print('tong cac chu so: ', tong)
if(n < 2):
    print('n khong phai so nguyen to')
else:
    for i in range(2, int((math.sqrt(n) + 1))):
        if(n % i != 0):
            print('n la so nguyen to')
        else:
            print('n khong phai so nguyen to')