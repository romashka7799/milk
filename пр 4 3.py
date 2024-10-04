a= int(input('введи а'))
b= int(input('введи б'))

if a>b:
    for i in range(a,b-1,-2):
        print(i ,end="")
else:
    print('в порядке возрастания')
    
    