gia = int(input('Gia: '))
dua = int(input('Khach dua: '))
def tra_tien_thua(gia, dua):
    tra = dua - gia
    to20 = 0
    to10 = 0
    to5 = 0
    to2 = 0
    to1 = 0
    while tra!=0:
        to20 += tra//20
        du20 = tra-20*to20
        if(du20!=0):
            to10 += du20//10
            du10 = du20-10*to10
            if(du10!=0):
                to5 += du10//5
                du5 = du10-5*to5
                if(du5!=0):
                    to2 += du5//2
                    du2 = du5-2*to2
                    if(du2!=0):
                        to1 += du2
                        break
    to = to20+to10+to5+to2+to1
    print('Can dung it nhat', to, 'to tien de tra tien thua')
    print('Cach tra tien thua:')
    print('-', to20, 'to 20 nghin dong')
    print('-', to10, 'to 10 nghin dong')
    print('-', to5, 'to 5 nghin dong')
    print('-', to2, 'to 2 nghin dong')
    print('-', to1, 'to 1 nghin dong')
tra_tien_thua(gia, dua)