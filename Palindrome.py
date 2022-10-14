def pal(n):
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev    
    
a=int(input())  
if a==pal(a):
    print("True")
else:
    print("False")