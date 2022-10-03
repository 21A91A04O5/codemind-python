def rev(num):
    re=0
    n=abs(num)
    while n>0:
        r=n%10
        if r==0:
            n=n//10
            continue
        re=re*10+r
        n=n//10
    return re
        
n=int(input())
if(n<0):
    print(-rev(n))
elif(n>0):
    print(rev(n))