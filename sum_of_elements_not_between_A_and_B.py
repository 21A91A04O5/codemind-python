n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in x:
    if i<a or i>b:
        c=c+i
print(c)        