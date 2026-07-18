import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print('Toa do diem A(', x1, ', ', y1, ')')
print('Toa do diem B(', x2, ', ', y2, ')')
Euclidean = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
print('Euclidean giua A va B la: ', Euclidean)