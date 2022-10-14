def fact(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum=sum+i
    return sum
    
a=int(input())
if fact(a)>a:
    print("True")
else:
    print("False")