s=input()
a=list(s)
c=0
v=['a','e','i','o','u','A','E','I','O','U']
for i in a:
    if i in v:
        c+=1
print(c)