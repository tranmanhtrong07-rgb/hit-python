ngay = int(input('ngay: '))
thang = int(input('thang: '))
if (thang == 1 and ngay in range(1, 20)) or (thang == 12 and ngay in range(22, 32)):
    print('Ma Ket')
elif (thang == 1 and ngay in range(20, 32)) or (thang == 2 and ngay in range(1, 19)):
    print('Bao Binh')
elif (thang == 2 and ngay in range(19, 30)) or (thang == 3 and ngay in range(1, 21)):
    print('Song Ngu')
elif (thang == 3 and ngay in range(21, 32)) or (thang == 4 and ngay in range(1, 20)):
    print('Bach Duong')
elif (thang == 4 and ngay in range(20, 31)) or (thang == 5 and ngay in range(1, 21)):
    print('Kim Nguu')
elif (thang == 5 and ngay in range(21, 32)) or (thang == 6 and ngay in range(1, 21)):
    print('Song Tu')
elif (thang == 6 and ngay in range(21, 31)) or (thang == 7 and ngay in range(1, 23)):
    print('Cu Giai')
elif (thang == 7 and ngay in range(23, 32)) or (thang == 8 and ngay in range(1, 23)):
    print('Su Tu')
elif (thang == 8 and ngay in range(23, 32)) or (thang == 9 and ngay in range(1, 23)):
    print('Xu Nu')
elif (thang == 9 and ngay in range(23, 31)) or (thang == 10 and ngay in range(1, 23)):
    print('Thien Binh')
elif (thang == 10 and ngay in range(23, 32)) or (thang == 11 and ngay in range(1, 22)):
    print('Bo Cap')
elif (thang == 11 and ngay in range(22, 31)) or (thang == 12 and ngay in range(1, 22)):
    print('Nhan Ma')