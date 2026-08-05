def nhap_du_lieu():
    kho_hang = {}
    so_mat_hang = int(input('Số mặt hàng trong kho: '))
    for i in range(so_mat_hang):
        mat_hang = input('Tên mặt hàng: ') 
        so_luong = int(input('Số lượng: ')) 
        kho_hang[mat_hang] = so_luong
    return kho_hang
def doc_du_lieu(kho_hang):
    if('laptop' in kho_hang.keys()):
        print('Số lượng laptop:', kho_hang.get('laptop'))
    else:
        print('Số lượng laptop: 0')
def cap_nhat_du_lieu(kho_hang):
    sp_moi = {}
    so_sp_moi = int(input('Số sản phẩm mới: '))
    for i in range(so_sp_moi):
        mat_hang_moi = input('Tên mặt hàng: ')
        so_luong_mat_hang_moi = int(input('Số lượng: '))
        sp_moi[mat_hang_moi] = so_luong_mat_hang_moi
    for ten_mat_hang, so_luong in sp_moi.items():
        if(ten_mat_hang in kho_hang):
            kho_hang[ten_mat_hang] += so_luong
        else:
            kho_hang[ten_mat_hang] = so_luong
    return kho_hang
def xoa_du_lieu(kho_hang):
    xoa = input('Mặt hàng cần xóa: ')
    if(xoa in kho_hang.keys()):
        kho_hang.pop(xoa)
    else:
        print(xoa, 'không tồn tại')
def trich_xuat_ds(kho_hang):
    for ten_mat_hang, so_luong in kho_hang.items():
        print(ten_mat_hang, so_luong)
    return kho_hang
def tinh(kho_hang):
    print('Tổng số lượng hàng trong kho:', sum(kho_hang.values()))
kho_hang = nhap_du_lieu()
doc_du_lieu(kho_hang)
cap_nhat_du_lieu(kho_hang)
xoa_du_lieu(kho_hang)
trich_xuat_ds(kho_hang)
tinh(kho_hang)