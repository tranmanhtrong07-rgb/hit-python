n = int(input('So khoan phai chi:'))
ds_chi = []
for i in range(n):
    print('Khoan chi thu', i+1, ':')
    ten_khoan_chi = input('Ten khoan chi: ')
    so_tien = int(input('So tien: '))
    danh_muc = input('Danh muc: ')
    khoan_chi = (ten_khoan_chi, so_tien, danh_muc)
    ds_chi.append(khoan_chi)
print('Danh sach cac khoan chi:')
for i in ds_chi:
    print(i)
tong_chi_tieu = 0
for i in ds_chi:
    tong_chi_tieu += i[1]
print('Tong chi tieu:', tong_chi_tieu, 'VND')
print('Thong ke theo danh muc:')
danh_muc_xet = []
for i in ds_chi:
    if(i[2] not in danh_muc_xet):
        so_khoan_chi = 0
        tong_tien = 0
        for j in ds_chi:
            if(j[2]==i[2]):
                so_khoan_chi += 1
                tong_tien += j[1]
        print(i[2], ':')
        print('- So khoan chi:', so_khoan_chi)
        print('- Tong tien:', tong_tien, 'VND')
        danh_muc_xet.append(i[2])
if(tong_chi_tieu > 5000000):
    print('Tong chi tieu da vuot qua 5.000.000 VND')
khoan_chi_max = []
for i in ds_chi:
    if(i[1] not in khoan_chi_max):
        khoan_chi_max.append(i[1])
for i in range(len(khoan_chi_max)):
    for j in range(i+1, len(khoan_chi_max)):
        if(khoan_chi_max[i] > khoan_chi_max[j]):
            tg = khoan_chi_max[i]
            khoan_chi_max[i] = khoan_chi_max[j]
            khoan_chi_max[j] = tg
print('Khoan chi co so tien lon nhat:')
for i in ds_chi:
    if(i[1] == khoan_chi_max[len(khoan_chi_max) - 1]):
        print(i)