def fact(n):
    #fact=1
    if n==0 or n==1:
        return 1
    return n * fact(n-1)

num=fact(3)
print(num)
