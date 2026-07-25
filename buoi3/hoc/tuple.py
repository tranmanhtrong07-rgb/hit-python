product = []   #danh sanh san pham
n = int(input('so san pham: '))   #nhap so luong san pham
for i in range(n):
    print('San pham:')
    #nhap ma san pham
    while True:
        ma = int(input('ma san pham: '))
        trung = False
        for sp in product:
            if(sp[0]==ma):
                trung = True
                break
        if not trung:
            break
        print('ma san pham da ton tai')
    #nhap ten san pham
    ten = input('ten sam pham: ')
    #nhap gia san pham
    while True:
        gia = input('gia: ')
        if(gia>0):
            break
    #nhap so luong san pham
    while True:
        so_luong = input('so luong san pham')
        if(so_luong>=0):
            break

    sp = (ma, ten, gia, so_luong)
    product.append(sp)
#tinh tien
print('thanh tien:')
for sp in product:
    thanh_tien = sp[2] * sp[3]
    print(sp[1], ':', thanh_tien)
#tim san pham gtri lon nhat
sp_gtri_max = product[0]
max_sp = sp_gtri_max[2]
for sp in product:
    gtri = sp[2]
    if(gtri>max_sp):
        max_sp = gtri
        sp_gtri_max = sp
print('San pham co gia tri lon nhat:', sp_gtri_max)
print('gia:', max_sp)
#tim san pham sap het hang
sp_het = product[0]
con = sp_het(3)
for sp in product:
    