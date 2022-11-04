n=int(input())
x=list(map(int,input().split()))
a=1
sum=0
for i in range(n-1,-1,-1):
    sum+=x[i]*a
    a=a*2
print(sum)    