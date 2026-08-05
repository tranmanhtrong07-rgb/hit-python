chuyen_doi_nhiet_do = lambda c : c * (9 / 5) + 32
print('F= ', chuyen_doi_nhiet_do(int(input('Nhiệt độ: '))))

kiem_tra_chan_le = lambda x : x % 2 == 0
if(kiem_tra_chan_le(float(input('Số: '))) == True):
    print('Chẵn')
else:
    print('Lẻ')

tinh_tien_tip = lambda hoa_don, phan_tram_tip : hoa_don * (phan_tram_tip / 100)
print('Tiền tip:', tinh_tien_tip(float(input('Hóa đơn: ')), float(input('Phần trăm tip: '))))

rut_gon_ten = lambda ho_va_ten : ho_va_ten.upper()
print('Họ và tên:', rut_gon_ten(input('Họ và tên: ')))