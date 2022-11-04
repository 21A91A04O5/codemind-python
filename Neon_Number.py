def sod(n):
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
    return sum
    
n=int(input())
a=n*n
b=sod(a)
if b==n:
    print("Neon Number")
else:
    print("Not Neon Number")