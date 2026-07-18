tien = int(input('So tien:'))
if(tien < 28):
    print('khong mua duoc')
else:
    chai = tien // 28
    vo = chai
    while(vo >= 3):
        doi = vo // 3
        chai += doi
        vo = vo % 3 + doi
    print('tong so chai bia:', chai)