import math
def z(a,b,d):
    z=a*b
    p = 1/2*(d**2)*(math.sin(a))
    return z
A= []
for i in range(2):
    print('введите',i,'cтороны квадрата')
    a= int(input('a:'))
    b= int(input('b:'))
    d =int(input('d:'))
    A.append(z(a,b,d))
for i in range(3):
    print('площадь',i,'-го квадрата {:.2f}'.format(A[i]))
