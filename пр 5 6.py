n = input('введи строку')

slowo=len(n)
for i in range(len(n)):
    if n[i]=='а':
        n =n.replace('а',' ')
print(n)
print(slowo)
