def pali(n):
    rev=0
    temp=n
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if(temp==rev):
        return True
    else:
        return False
        
def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
    
n=int(input())  
while True:
    n=n+reverse(n)
    if pali(n):
        print(n)
        break
    