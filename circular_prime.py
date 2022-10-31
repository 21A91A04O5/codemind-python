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
            
def reverse(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
    
n=int(input())
a=reverse(n)
if prime(n):
    if prime(a):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")