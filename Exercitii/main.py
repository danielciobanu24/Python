'''
x=str(input("Sirul x este:"))
y=str(input("Sirul in care vreau sa gasesc sirul x este:"))
c=len(y)
z=len(x)
a=0
b=0
for j in range(z):
   for i in range(c):
          if x[j]==y[i]:
            a=1
   if a==1:
        b+=1
   a=0
b=int(b)
z=int(z)
if b==z:
    print("Sirurile sunt echilibrate!")
'''
'''
3
x=str(input("Tastati sirul dumneavoastra:"))
y=str(input("Tastati subsirul dumneavoastra:"))
z=x.split()
g=len(z)
for i in range(g):
    if z[i].lower()==y:
        print(z[i],end=' ')
'''
'''
4
x=input("Tastati sirul dumneavoastra:")
z=len(x)
c=""
for i in range(len(x)):
    if x[i] in 'AaeEiIoOuU':
       c=c+x[i]+x[i]
    else:
        c=c+x[i]
print(c)
'''
'''
x=input("Tastati sirul dumneavoastra:")
y=x.split()
z=len(y)
c=int(input("Tastati cate cuvinte doresti sa aiba cuvantul din interior:"))
for i in range(z):
    if c==len(y[i]):
        print(y[i])
'''
'''
x=input("Tastati sirul dumneavoastra:")
a=len(x)
for i in range(a):
    if x[i] in ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789':
        print(x[i],end="")
'''
'''
7
x=str(input("Tastati sirul dumneavoastra:"))
g=x.split()
a=sorted(g)
for i in range(len(a)):
    print(a[i],end="\n")
'''
'''
x=input("Tastati sirul dumneavoastra:")
g=x.split()
for i in range(len(g)):
    print(g[i][::-1],end=" ")
'''

