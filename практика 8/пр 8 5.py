#5.1
n = int(input('введите количество строк: '))
m = int(input('введите количество столбцов: '))
a = []
for i in range(n): 
    b = []
    for j in range(m): 
        print('Введите [', i, ',', j, '] элемент: ')
        b.append(int(input()))
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()


for i in range(len(a)):
    a[i].sort()  
print('Массив по возрастанию  с элементами:',a)

