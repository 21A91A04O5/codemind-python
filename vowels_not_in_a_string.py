s=input()
c=0
b=[]
v=['a','e','i','o','u']
for i in s:
    if i in v:
        v.remove(i)
if len(v)==0:
    print("0")
else:    
    print(*v)