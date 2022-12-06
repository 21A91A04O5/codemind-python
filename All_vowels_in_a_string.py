s=input()
s.lower()
v="aeiou"
c=0
a=set(s)
for i in a:
    if i in v:
        c+=1
if c==5:
    print("True")
else:
    print("False")