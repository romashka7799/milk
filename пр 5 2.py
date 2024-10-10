n = input('строка')

count = 0

for i in range(len(n)):
    if n[i]==':':
        n = n.replace(':','%')
        count+=1
print(count)