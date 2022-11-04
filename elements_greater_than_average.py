n=int(input())
x=list(map(int,input().split()))
a=0
c=0
for i in range(n):
    a+=x[i]
avg=a//n
for i in range(n):
    if(x[i]>=avg):
        c+=1
print(c)        