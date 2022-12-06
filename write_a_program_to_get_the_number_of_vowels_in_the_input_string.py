s=input()
c=0
v="aeiouAEIOU"
for i in s:
    if i in v:
        c+=1
print(c)