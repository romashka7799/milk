n = int(input('введите н'))

sum=1
x= 0 

for i in range(1,n+1):
    sum*=i
    x+=sum
print(x)