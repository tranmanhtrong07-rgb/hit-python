n = int(input('So khoi hinh hop chu nhat: '))
do_cao = list(map(int, input('Do cao: ').split()))
def luong_mua(n, do_cao):
    the_tich = 0
    for i in range(n):
        maxLeft = do_cao[0]
        maxRight = do_cao[i]
        for left in range(i+1):
            if(do_cao[left]>maxLeft):
                maxLeft = do_cao[left]
        for right in range(i, n):
            if(do_cao[right]>maxRight):
                maxRight = do_cao[right]
        the_tich += (min(maxLeft, maxRight) - do_cao[i])
    print('Hung duoc:', the_tich)
luong_mua(n, do_cao)