#6.1
n = int(input('введите длину массива \n'))
a = []


for i in range(n):
    print('введите',i,'элемент:')
    a.append(int(input()))
maxi = max(a)
reverseda = a[::-1]
print(maxi)
print('обратный порядок',reverseda)  

#6.2

n = int(input('введите длину массива \n'))
a = []


for i in range(n):
    print('введите',i,'элемент:')
    a.append(int(input()))

srarifm=sum(a)/len(a)

for  i in range(len(a)):
    if a[i]==0:
        a[i]=srarifm
print(srarifm)