def find_max():
    n = int(input())
    if n==0:
        return 0
    else:
        return max(n,find_max())
print(find_max())