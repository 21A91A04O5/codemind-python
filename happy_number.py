n=int(input())
while(n>9):
    sum=0
    while(n>0):
        r=n%10
        sum=sum+r**2
        n=n//10
    n=sum   
if sum==1 or sum==7:
    print("True")
else:
    print("False")

