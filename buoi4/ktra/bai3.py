lst = input('Nhap chuoi: ').split(' ')
def tim(can_tim):
    can_tim = input('Can tim: ')
    vi_tri = []
    for i in range(len(lst)):
        if(lst[i]==can_tim):
            vi_tri.append(i)
    if(len(vi_tri)==0):
        print('-1')
    else:
        print(vi_tri)
can_tim = ''
tim(can_tim)