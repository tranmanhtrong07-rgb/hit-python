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

for i in range(si_so):
    for j in range(i+1, si_so):
        lop_sap_xep = sorted(
            lop,
            key=lambda hs: sum(hs['Điểm'].values()),
            reverse = True
        )
        if(sum(lop_sap_xep[i]['Điểm'].values()) == sum(lop_sap_xep[j]['Điểm'].values())):
            lop_sap_xep = sorted(
                (lop_sap_xep[i], lop_sap_xep[j]),
                key = lambda hs: hs['Họ tên'].split()[-1],
                reverse = False
            )
for hs in lop_sap_xep:
    print(hs['Họ tên'])