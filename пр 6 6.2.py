#6.2.1
n = int(input('введите длину массива:'))
a = []
indexi = 0
for i in range(n):
    print('введите',i, 'элемент:')
    a.append(int(input()))

mini=min(a)
for  index, n in enumerate(a):

    print('индекс минимального:',indexi)
    print(mini)

#6.2.2

n= int(input('введите длину массива\n'))
x = [] #второй массив
y = [] #третий массив
a=[] #просто массив
for i in range(n):
    print('введите',i,'элемент:')
    x.append(int(input()))
for i in range(n):
    print('введите',i ,'элемент:')
    y.append(int(input()))
for s in a:
    if s>0:
        x.append(s)
    else:
        y.append(s)
print('положительные:',x)
print('отрицательные:', y)
