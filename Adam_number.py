def reve(n):
    re=0
    while(n>0):
        r=n%10
        re=re*10+r
        n=n//10
    return re
    
n=int(input())
a=n*n
b=reve(n)*reve(n)
if(a==reve(b)):
    print("True")
else:
    print("False")