def rev(num):
    re=0
    while num>0:
        r=num%10
        re=re*10+r
        num=num//10
    return re
        
n=int(input())
print(rev(n))