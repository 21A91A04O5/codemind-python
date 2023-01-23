import math
def prime(n):
    f=0
    for i in range(2,n//2+1):
        if n%i==0:
            f=1
            break
    if f==0:
        return True
    else:
        return False
        
n=int(input())  
f=0
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0 and prime(i):
        if prime(n//i) and i!=n//i:
            f=1
            print(i,n//i)
            break
if f==0:
    print("-1")