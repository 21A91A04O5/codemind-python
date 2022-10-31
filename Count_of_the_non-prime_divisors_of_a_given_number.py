def notprime(n):
    count=0
    if(n==1):
        return True
    for i in range(2,(n//2)+1):
        if(n%i==0):
            count+=1
            break
    if count:
        return True
    else:
        return False
    
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0 and notprime(i)):
        c+=1
print(c)        