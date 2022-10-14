def cou(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    return cou(n-1)+cou(n-2)+cou(n-3)    
a=int(input())
print(cou(a))