def pfact(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    return s
    
a=int(input())
b=int(input())
if(pfact(a)==b and pfact(b)==a):
    print("Amicable")
else:
    print("Not Amicable")