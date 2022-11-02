def cou(n):
    c=0
    while n:
        r=n%10
        c+=1
        n=n//10
    return c    
        
n=int(input())
a=list(map(int,input().split()))
d=0
e=0
for i in range(n):
    if(cou(a[i])>d):
        d=cou(a[i])
for i in range(n):
    if(cou(a[i])==d):
        e+=1;
print(e)        