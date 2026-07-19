n= int(input('n='))
while(n<20 or n>30):
    print('n khong hop le')
    n= int(input('n='))
x= float(input('x='))
if(x==0):
    print('phuong thinh khong hop le')
else:
    giatri= 2022*x**n
    for i in range(1, n+1):
        giatri += i/(x**i)
    print('P=', giatri)