a = int(input('введите а'))
b = int(input('введите б'))

if a<b:
    for i in range(a,b+1):
        print(i,end=" ")
else:
    for i in range(a,b-1,-1):
        print(i,end = "")
        