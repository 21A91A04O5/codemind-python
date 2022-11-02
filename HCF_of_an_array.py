n=int(input())
x=list(map(int,input().split()))
a=min(x)
found=0
for i in range(n):
    if(x[i]%a!=0):
        found=1
if(found==0):
    print(a)
else:
    print("1")
    