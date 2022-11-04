n=int(input())
x=list(map(int,input().split()))
b=len(x)-1
sum=0
for i in range(n):
    sum+=x[i]*(2**b)
    b-=1
print(sum)    