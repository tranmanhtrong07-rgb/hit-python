python_club = set(input('sinh vien tham gia clb: ').split(','))
ai_club = set(input('sinh vien tham gia clb: ').split(','))
english_club = set(input('sinh vien tham gia clb: ').split(','))
#tim svien tham gia it nhat 1 clb
min_1clb = python_club.union(ai_club).union(english_club)
print('sinh vien tham gia it nhat 1 clb: ', min_1clb)
#tim svien tham gia ca 3 clb
ca_3clb = python_club.intersection(ai_club).intersection(english_club)
print('sinh vien tham gia ca 3 clb: ', ca_3clb)
#sinh vien chi tham gia clb python
chi_python = python_club.difference(ai_club).difference(english_club)
print('sinh vien chi tham gia clb python: ', chi_python)
#sinh vien chi tham gia 1 clb
chi_ai = ai_club.difference(python_club).difference(english_club)
chi_english = english_club.difference(python_club).difference(ai_club)
chi_mot = chi_python.union(chi_ai).union(chi_english)
print('sinh vien chi tham gia 1 clb: ', chi_mot)
#sinh vien tham gia it nhat 2 clb
python_ai = python_club.intersection(ai_club)
python_english = python_club.intersection(english_club)
ai_english = ai_club.intersection(english_club)
min_2clb = python_ai.union(python_english).union(ai_english).union(ca_3clb)
print('sinh vien tham gia it nhat 2 clb: ', min_2clb)
#nhap ma svien va tim clb svien tham gia
ma_svien = input('nhap ma sinh vien: ')
tim = False
if(ma_svien in python_club):
    print('sinh vien', ma_svien, 'tham gia clb Python')
    tim = True
if(ma_svien in ai_club):
    print('sinh vien', ma_svien, 'tham gia clb AI')
    tim = True
if(ma_svien in english_club):
    print('sinh vien', ma_svien, 'tham gia clb English')
    tim = True
if not tim:
    print('sinh vien', ma_svien, 'khong tham gia clb nao')