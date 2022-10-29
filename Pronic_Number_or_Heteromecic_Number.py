n=int(input())
flag=0
if n==0:
    print("YES")
for i in range(1,n):
    if(n%i==0 and n%(i+1)==0):
        if(i*(i+1)==n):
            flag=1
            break
        else:
            flag=0
if flag==1:
    print("YES")
else:
    print("NO")

