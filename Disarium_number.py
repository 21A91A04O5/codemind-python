def cou(n):
    c=0
    while(n>0):
        r=n%10
        c+=1
        n=n//10
    return c
    
def dis(n):
    a=0
    b=cou(n)
    while(n>0):
        r=n%10
        a=a+r**b
        n=n//10
        b+=-1
    return a    
    
x=int(input())
if x==dis(x):
    print("True")
else:
    print("False")
    