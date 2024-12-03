#8.1

N = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print('массив a[N][N]')
s  =0
for i in range(len(N)):
    for j in range(len(N)):
        if i==j:
            s+=N[i][j]
count = 0

for row in N:
    for elem in row:
        if elem>0:
            count+=1
print('сумма элементов ',s)
print('положительные',count)

