n=int(input())
x=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if i%2==0:
        c=c+x[i]
    elif i%2!=0:
        d=d+x[i]
print(abs(c-d))        