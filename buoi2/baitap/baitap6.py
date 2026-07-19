n= int(input('n='))
while(n<100 or n>200):
    print('n khong hop le')
    n= int(input('n='))
luy_thua= 1
while(luy_thua<=n):
    luy_thua*= 2
print('so can tim:', luy_thua)