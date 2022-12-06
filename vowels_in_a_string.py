s=input()
d=input()
f=0
for i in range(len(s)):
    if s[i]==d:
        f=1
        c=i
        break
if f==1:
    print("True")
    print(c)
else:
    print("False")
    
        