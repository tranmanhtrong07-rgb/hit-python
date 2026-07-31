n = int(input('n = '))
a = input().split(',')
def tinh(a, n):
    tong = 0
    for i in range(len(a)):
        tong += int(a[i]) * int(n**(len(a)-1-i))
    print(tong)
tinh(a, n)