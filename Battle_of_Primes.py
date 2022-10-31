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
            
n=int(input())
m=int(input())
a=1
while True:
    if prime(n+m+a):
        print(a)
        break
    else:
        a+=1