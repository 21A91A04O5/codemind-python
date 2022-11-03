def prime(n):
    if n==1 or n==0:
        return False
    f=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            f=1
            break
    if f==0:
        return True
    else:
        return False
    
n=int(input())
c=0
temp=n
while n>0:
    r=n%10
    if(prime(r)==False):
        c=1
    n=n//10
if(c==0 and prime(temp)):
    print("Mega Prime")
else:
    print("Not Mega Prime")