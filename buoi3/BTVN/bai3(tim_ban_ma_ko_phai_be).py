nguoi_A = input().split(',')
nguoi_B = input().split(',')
list_A = []
for i in nguoi_A:
    s = ' '.join(i.split())
    list_A.append(s.title())
hobby_A = set(list_A)
print('So thich cua A:', hobby_A)
list_B = []
for i in nguoi_B:
    s = ' '.join(i.split())
    list_B.append(s.title())
hobby_B = set(list_B)
print('So thich cua B:', hobby_B)
#in so thich chung cua A va B
A_chung_B = hobby_A.intersection(hobby_B)
so_chung = len(A_chung_B)
if(so_chung == 0):
    print('A va B khong co so thich chung')
else:
    print('So thich chung:', A_chung_B)
#so thich chi A co
chi_A = hobby_A.difference(hobby_B)
print('So thich chi A co:', chi_A)
#tat ca so thich cua ca 2 nguoi
A_va_B = hobby_A.union(hobby_B)
print('Tat ca so thich:', A_va_B)
#muc do tuong dong giua 2 nguoi
tong_so_thich = len(A_va_B)
if(so_chung == 0):
    print('Muc do tuong dong: 0%')
else:
    do_tuong_dong = (so_chung / tong_so_thich) * 100
    print('Muc do tuong dong:', round(do_tuong_dong, 2),'%')