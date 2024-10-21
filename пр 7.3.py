import math

def z(a, b):
    return math.sqrt(a**2 + b**2)

def w(d, c):
    return math.sqrt(d**2 + c**2)

A = []
for i in range(1):
    print('Введите', i, 'катеты первого треугольника')
    a = int(input('a: '))
    b = int(input('b: '))
    A.append(z(a, b))

B = []
for i in range(1):
    print('Введите', i, 'катеты второго треугольника')
    d = int(input('a1: '))
    c = int(input('b1: '))
    B.append(w(d, c))

gip1 = A[0]  #первое значение из списка A
gip2 = B[0]  #первое значение из списка B 

if gip1 > gip2:
    result = 'Гипотенуза 1 больше гипотенузы 2'
elif gip1 < gip2:
    result = 'Гипотенуза 2 больше гипотенузы 1'
else:
    result = 'Гипотенузы равны'
print(f"Гипотенуза 1: {gip1}, гипотенуза 2: {gip2}")
print(result)