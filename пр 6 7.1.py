#7.1
n = int(input('введите длину массива \n'))
a = []
chet=0
nechet=1

for i in range(n):
    print('введите',i,'элемент:')
    a.append(int(input()))

for i in range(n):
    if i%2==0:
        chet+=a[i]
    else:
        nechet*=a[i]
print('сумма Четных:', chet ,' произведение Нечетных:', nechet)


