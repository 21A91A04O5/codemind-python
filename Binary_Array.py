n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    if i!=0 and i!=1:
        c=1
        break
if c==1:
    print("False")
else:
    print("True")