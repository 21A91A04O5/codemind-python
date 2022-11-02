def fact(n):
    fact=1
    for i in range(n,1,-1):
        fact=fact*i
    return fact
    
sum=0    
n=int(input())
temp=n
while n>0:
    r=n%10
    sum=sum+fact(r)
    n=n//10
if(sum==temp):
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")
    