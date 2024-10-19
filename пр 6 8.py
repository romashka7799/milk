n = int(input('введите длину массива \n'))
a = []
proiz=1
for i in range(n):
    print('введите',i,'элемент:')
    a.append(int(input()))

suma= sum(a)
for i in a:
        proiz*=i
print('сумма эдементов:' ,suma,'прооизведение  элементов:',proiz)

