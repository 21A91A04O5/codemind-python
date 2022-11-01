n=int(input())
x=list(map(int,input().split()))
sum=0
for i in x:
    if i%2!=0:
        sum=sum+i
print(sum)        