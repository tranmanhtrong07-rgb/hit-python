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
        