n = input('строка')
count=0

for i in range(len(n)):
    if n[i]=='.':
        n =n.replace('.',' ',1)
    count+=1
print(count)
print(n)
