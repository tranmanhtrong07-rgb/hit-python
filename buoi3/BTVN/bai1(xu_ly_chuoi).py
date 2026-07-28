string = input('Nhap chuoi: ')
while ' ' in string:
    print('Chuoi khong chua dau cach!')
    string = input('Nhap chuoi: ')
#dao nguoc chuoi
string_dao = ''
for i in range(len(string)-1, -1, -1):
    string_dao += string[i]
print('Chuoi dao nguoc: ', string_dao)
#sap xep chuoi tang dan
lst = list(string)
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if(lst[i]>lst[j]):
            tg = lst[i]
            lst[i] = lst[j]
            lst[j] = tg
print('Chuoi sau khi sap xep: ', ''.join(lst))
#kiem tra chuoi doi xung
if(string == string_dao):
    print('Day la chuoi doi xung')
else:
    print('Day khong phai chuoi doi xung')
#sap xep ky tu khac nhau
ky_tu = list(set(string))
for i in range(len(ky_tu)):
    for j in range(i+1, len(ky_tu)):
        if(ky_tu[i]>ky_tu[j]):
            tg = ky_tu[i]
            ky_tu[i] = ky_tu[j]
            ky_tu[j] = tg
#dem so lan xuat hien ky tu
dem = 0
for i in ky_tu:
    if(string.count(i)>dem):
        dem = string.count(i)
#in ky tu xuat hien nhieu nhat
for i in ky_tu:
    if(string.count(i)==dem):
        print('Ky tu xuat hien nhieu nhat:', i)
        print('So lan xuat hien:', dem)
#kien tra day du 5 nguyen am TA
nguyen_am = ['a', 'e', 'i', 'o', 'u']
day_du = True
for i in nguyen_am:
    if(i not in string):
        day_du = False
        break
if(day_du):
    print('Chuoi chua day du 5 nguyen am Tieng anh')
else:
    print('Chuoi khong chua day du 5 nguyen am Tieng Anh')