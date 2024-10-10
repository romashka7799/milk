n = input('введи строку')
count=0
slowo=len(n)
for i in range(len(n)):
    if n[i]=='а':
        n =n.replace('а','о')
    count+=1
print(count)
print(n)
print(slowo)
