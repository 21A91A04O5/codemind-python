n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
arr=[]
for i in x:
    if i<a or i>b:
        arr.append(i)
if(len(arr)>0):
    print(max(arr)) 
else:
    print("-1")