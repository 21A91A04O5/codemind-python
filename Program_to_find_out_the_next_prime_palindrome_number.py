def prime(n):
    count=0
    if n==1:
        return False
    else:
        for i in range(2,(n//2)+1):
            if(n%i==0):
                count=1
                break
        if count:
            return False
        else:
            return True
            
def pali(n):
    rev=0
    temp=n
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        return True
    else:
        return False
    
a=int(input())
a=a+1
while True:
    if(prime(a) and pali(a)):
        print(a)
        break
    else:
        a+=1