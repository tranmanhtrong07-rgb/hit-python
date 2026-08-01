n = int(input())
while(n<0 and n>10):
    n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

tong = 0
for i in lst:
    tong += i
tbc = tong/(len(lst))
print('tbc=', tbc)

max = lst[0]
min = lst[0]
for i in lst:
    if(i>max):
        max = i
    if(i<min):
        min = i
print('max=', max)
print('min=', min)

lst1= []
for i in lst:
    if(i>5):
        lst1.append(i)
print('cac diem lon hon diem tb:', lst1)

for i in lst:
    if(i==10):
        print('True')
        break

