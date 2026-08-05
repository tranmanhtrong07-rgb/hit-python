#chuan hoa ten nguoi dung
ten = input().split()
ten_nguoi_dung = ''
for i in ten:
    ten_nguoi_dung += i[0].upper() + i[1:].lower() + ' '
print('Ten nguoi dung:', ten_nguoi_dung)
#ten dang nhap
while True:
    username = input('Ten dang nhap: ')
    tk_dung = True
    if(len(username)<6 or len(username)>20):
        tk_dung = False
    elif(username[0].isalpha() == False):
        tk_dung = False
    else:
        co_so = False
        for i in username:
            if(i.isnumeric() == True):
                co_so = True
                break
        if(co_so == False):
            tk_dung = False
    if(tk_dung == True):
        break
    else:
        print('Ten dang nhap khong hop le')
#mat khau
while True:
    mat_khau = input("Mat khau: ")
    mk_dung = True
    if(len(mat_khau)<8):
        mk_dung = False
    else:
        co_hoa = False
        co_thuong = False
        co_so = False
        co_khoang_cach = False
        co_ky_tu_dac_biet = False
        for i in mat_khau:
            if(i.isupper() == True):
                co_hoa = True
            elif(i.islower() == True):
                co_thuong = True
            elif(i.isnumeric() == True):
                co_so = True
            elif(i == ' '):
                co_khoang_cach = True
            else:
                co_ky_tu_dac_biet = True
                break
        if not (co_hoa and co_thuong and co_so and  co_khoang_cach and co_ky_tu_dac_biet):
            mk_dung = False
        if(co_khoang_cach == True):
            mk_dung = False
    if(mk_dung == True):
        break
    else:
        print('Mat khau chx dat dieu kien')