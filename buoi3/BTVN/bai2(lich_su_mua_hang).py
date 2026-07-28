san_pham = input('Cac san pham da mua: ').split(',')
sp_check = input('San pham can kiem tra: ').split(',')
#chuan hoa danh sach san pham da mua
list_san_pham = []
for i in san_pham:
    s = ' '.join(i.split())
    list_san_pham.append(s.title())
print('Danh sach san pham:', list_san_pham)
#tong so san pham da mua
tong_sp = len(list_san_pham)
print('Tong so san pham da mua:', tong_sp)
#in san pham o giua danh sach
if(tong_sp % 2 != 0):
    vi_tri = int((tong_sp - 1)/2)
    print('San pham o vi tri giua:', list_san_pham[vi_tri])
#tim san pham mua nhieu nhat
dem = 0
for i in list_san_pham:
    if(list_san_pham.count(i) > dem):
        dem = list_san_pham.count(i)
#in san pham mua nhieu nhat
sp_mua_nhieu = []
for i in list_san_pham:
    if(list_san_pham.count(i)==dem) and (i not in sp_mua_nhieu):
        sp_mua_nhieu.append(i)
for a in range(len(sp_mua_nhieu)):
    for b in range(a+1, len(sp_mua_nhieu)):
        if(sp_mua_nhieu[a] > sp_mua_nhieu[b]):
            tg = sp_mua_nhieu[a]
            sp_mua_nhieu[a] = sp_mua_nhieu[b]
            sp_mua_nhieu[b] = tg
print('San pham duoc mua nhieu nhat:')
for i in sp_mua_nhieu:
    print(i, ':', dem, 'lan')
#chuan hoa san pham can kiem tra
list_sp_check = []
for i in sp_check:
    s = ' '.join(i.split())
    list_sp_check.append(s.title())
print('San pham can kiem tra:', list_sp_check)
#kiem tra san pham da mua chua
da_mua = True
for i in list_sp_check:
    if(i not in list_san_pham):
        da_mua = False
if(da_mua):
    print('Da mua', i)
else:
    print('Chua mua', i)
#them vao dau danh sach
them = ' '.join(input('Mua them:').split())
list_san_pham.insert(0, them.title())
#xoa sp sua
for i in list_san_pham:
    if(i == 'Sua'):
        list_san_pham.remove('Sua')
print('Danh sach sau khi cap nhat:', list_san_pham)