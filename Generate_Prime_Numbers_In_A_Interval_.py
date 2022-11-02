import math
def prime(n):
    count=0
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            count=1
            break
    if count==0:
        return True
    else:
        return False
        
m=int(input())        
n=int(input())
for i in range(m,n+1):
    if prime(i):
        print(i)
        