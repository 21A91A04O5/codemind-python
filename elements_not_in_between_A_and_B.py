n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
count=0
for i in x:
    if i<a or i>b:
        count=1
        print(i,end=" ")
if(count==0):
    print('-1')