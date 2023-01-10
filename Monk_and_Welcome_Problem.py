n=int(input())
lst=list(map(int,input().split()))
lst1=list(map(int,input().split()))
v=list(zip(lst,lst1))
for i in v:
    p=sum(i)
    print(p,end=" ")