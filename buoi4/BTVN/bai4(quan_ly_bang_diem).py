si_so = int(input('Sĩ số: '))
lop = []
for i in range(si_so):
    print('Học sinh', i+1, ':')
    ho_ten = input('Họ tên: ')
    diem_toan = int(input('Điểm Toán: '))
    diem_van = int(input('Điểm Văn: '))
    diem_anh = int(input('Điểm Anh: '))
    hoc_sinh = {
        'Họ tên': ho_ten,
        'Điểm': {
            'Toán': diem_toan,
            'Văn': diem_van,
            'Anh': diem_anh,
        }
    }
    lop.append(hoc_sinh)
print('Danh sách lớp:')
for i in lop:
    print(i)
diem_giam_dan = sorted(
    lop, 
    key = lambda hoc_sinh: hoc_sinh['Điểm']['Toán'], 
    reverse = True
)
ds_toan = []
for i in diem_giam_dan:
    ds_toan.append(i['Họ tên'])
print(ds_toan)
diem_anh_cao_nhat = max(
    lop, 
    key = lambda hoc_sinh: hoc_sinh['Điểm']['Anh']
)
print('Học sinh có điểm Anh cao nhất:', diem_anh_cao_nhat)
for i in range(si_so):
    for j in range(i+1, si_so):
        tong_3mon_giam = sorted(
            lop,
            key=lambda hoc_sinh: sum(hoc_sinh['Điểm'].values()),
            reverse = True
        )
        if(sum(tong_3mon_giam[i]['Điểm'].values()) == sum(tong_3mon_giam[j]['Điểm'].values())):
            tong_3mon_giam = sorted(
                (tong_3mon_giam[i], tong_3mon_giam[j]),
                key = lambda hoc_sinh: hoc_sinh['Họ tên'].split()[-1],
                reverse = False
            )
ds_3mon = []
for i in tong_3mon_giam:
    ds_3mon.append(i['Họ tên'])
print(tong_3mon_giam)
hsg = list(filter(lambda hoc_sinh: sum(hoc_sinh['Điểm'].values()) >= 24, lop))
hsg = sorted(
    hsg,
    key= lambda hoc_sinh: sum(hoc_sinh['Điểm'].values()),
    reverse = True
)
gioi = list(map(lambda hoc_sinh: hoc_sinh['Họ tên'], hsg))
print(gioi)