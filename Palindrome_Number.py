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
    
t=int(input())
for i in range(t):
    n=int(input())
    if pali(n):
        print("True")
    else:
        print("False")