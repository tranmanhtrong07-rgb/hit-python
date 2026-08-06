n = int(input('Kho chứa số loại sản phẩm: '))
danh_sach_sp = []
for i in range(n):
    print('Sản phẩm ', i+1, ':')
    ma_sp = input('Mã sản phẩm: ')
    ten_sp = input('Tên sản phẩm: ')
    danh_muc = input('Danh mục: ')
    gia = int(input('Giá: '))
    ton_kho = int(input('Tồn kho: '))
    san_pham = {
        'Mã sản phẩm': ma_sp,
        'Tên sản phẩm': ten_sp,
        'Danh mục': danh_muc,
        'Giá': gia,
        'Tồn kho': ton_kho
    }
    danh_sach_sp.append(san_pham)
print('Danh sách sản phẩm:')
for sp in danh_sach_sp:
    print(sp)
sp_dien_tu = list(filter(lambda sp: sp['Danh mục'] == 'điện tử', danh_sach_sp))
print('Sản phẩm điện tử: ', sp_dien_tu)
sp_ban_het = list(filter(lambda sp: sp['Tồn kho'] == 0, danh_sach_sp))
print('Sản phẩm đã bán hết: ', sp_ban_het)
ds_ten_sp = []
ten = map(lambda sp: sp['Tên sản phẩm'], danh_sach_sp)
ds_ten_sp.append(ten)
print('Các sản phẩm trong kho:', ds_ten_sp)
sp_cao_cap = list(filter(lambda sp: sp["Giá"] >= 1000000, danh_sach_sp))
thong_bao = list(map(print('Tặng voucher 100k cho khách mua', sp['Tên sản phẩm']), sp_cao_cap))
for km in thong_bao:
    print(km)