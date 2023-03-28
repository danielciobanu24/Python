'''1
x=int(input("x="))
y=int(input("y="))
print(x,y)
print(x/y)
print(x//y)
x=float(x)
y=float(y)
print("x=%.2f, y=%.1f, x?y=%d" % (x,y,int(x)**int(y)))
'''

''' 2,3
x="Ana"
y="are"
z="mere"
print(x,y,z,sep=("---"),end=(":)))"))
print("\n")
g=int(input("x="))
print("g=%x"%g)
'''
'''Ex propuse
1
x=int(input("X="))
if x<=100:
    print("%x"%x)
else:
    print("%o"%x)
'''
'''2
print("Ecuatia de gradul 1 are forma ax+b=0!");print("Spuneti-mi cat doriti sa fie a si b in cazul ecuatiei dumneavoastra:")
x=int(input("a="))
y=int(input("b="))
print("Ecuati dumneavoastra este:%dx+%d=0"%(x,y))
print("Solutia ecuatiei dumneavoastra este x=%.1f"%(-y/x))
'''
'''3
print("Spuneti 3 numere si eu va voi spune daca acele 3 numere sunt consecutive:")
x,y,z=float(input()),float(input()),float(input())
if z>=y>=x:
    print("Numerele sunt in ordine consecutiva!")
else:
    print("Numerele nu sunt in ordine consecutiva!")
'''
'''4
print("Spuneti numarul dumneavoastra si eu va voi spune daca este par sau impar!")
x=float(input("Numarul este:"))
if x%2==0:
    print("Numarul dumneavoastra este par!")
else:
    print("Numarul dumneavoastra este impar!")
'''
'''5
print("Tastati numarul dumneavoastra:")
x=float(input())
if x<=0:
    print("Numarul dumneavoastra nu poate fi raza unui cerc!")
else:
    print("Numarul dumneavoastra poate fi raza unui cerc!")
    v=(x**3)*3.14*(4/3)
    a=(x**2)*3.14*4
    v=float(v)
    a=float(a)
    print("Volumul cercului dumneavoastra este egal cu:%.2f"%v)
    print("Aria cercului dumneavoastra este egala cu:%.2f"%a)
'''
'''6
print("Tastati 2 numere si eu va voi afisa minimul si maximul a celor 2 numere!")
x=float(input("Primul numar este:"))
y=float(input("Al doilea numar este:"))
if x>y:
    print("Maximul este %d iar minimul este %d!"%(x,y))
else:
    print("Maximul este %d iar minimul este %d!"%(y,x))
'''
'''7
print("Tastati un numar:")
x=int(input())
print("Tastati limita inferioara a intervalului dumneavoastra:")
y=int(input())
print("Tastati limita superioara a intervalului dumneavoastra:")
z=int(input())
if z>=x>=y:
    print("Numarul dumneavoastra se afla in intervalul:[%d %d]!"%(y,z))
else:
    print("Numarul dumnavoastra nu apartine intervalului:[%d %d]!"%(y,z))
    '''
'''Beni for
n=int(input("Spuneti Cardinalul elementelor vectorului:"))
v=[int(input("v["+str(i)+"]=")) for i in range(n)]
print(*v)
'''
'''
ex 8
x=int(input("Primul numar este:"))
y=int(input("Al doilea numar este:"))
z=int(input("Al treilea numar este:"))
if(x>=y>=z):
    print("Maximul este %d"%x,end=" ")
    print("iar minimul este %d"%z)
    print("Sirul ordonat crescator este:%d %d %d"%(z,y,x))
elif(x>=z>=y):
    print("Maximul este %d"%x,end=" ")
    print("iar minimul este %d"%y)
    print("Sirul ordonat crescator este:%d %d %d"%(y,z,x))
elif(y>=x>=z):
    print("Maximul este %d"%y,end=" ")
    print("iar minimul este"%z)
    print("Sirul ordonat crescator este:%d %d %d"%(z,x,y))
elif(y>=z>=x):
    print("Maximul este %d"%y,end=" ")
    print("iar minimul este %d"%x)
    print("Sirul ordonat crescator este:%d %d %d"%(x,z,y))
elif(z>=y>=x):
    print("Maximul este %d"%z,end=" ")
    print("iar minimul este %d "%x)
    print("Sirul ordonat crescator este:%d %d %d"%(x,y,z))
elif(z>=x>=y):
    print("Maximul este %d"%z,end=" ")
    print("iar minimul este %d"%y)
    print("Sirul ordonat crescator este:%d %d %d"%(y,x,z))
'''
'''
from math import sqrt
print("Ecuatia de gradul al 2-lea are urmatoarea forma:axpatrat+bx+c=0")
print("Spuneti variabilele pt ecuatia de gradul 2 a dumneavoastra:a b si c:")
x=int(input())
y=int(input())
z=int(input())
m=0+1j
print("Ecuatia dumneavoastra este:%dxpatrat+%dx+%d=0!"%(x,y,z))
d=(y**2)-4*x*z

print("Delta este egala cu:%d"%d)
if d>0:
    print("Solutiile ecuatiei dumneavoastra sunt:x1=%.2f si x2=%.2f"%((-y+(sqrt(d)))/2*x,(-y-(sqrt(d)))/2*x))
elif d==0:
    print("Solutia ecuatiei dumneavoastra este:%f"%(-y/2*x))
else:
    print(-y +(m*(sqrt(-d))) / 2 * x)
    #print("Solutiile ecuatiei dumneavoastra sunt complexe si sunt de tipul:x1=%j si x2=%j",-y+(sqrt(-d))/2*x,-y-(sqrt(-d))/2*x)
'''
'''
print("Introduceti coordonatele unui punct P din plan:")
x=int(input("Introduceti coordonata x:"))
y=int(input("Introduceti coordonata y:"))
if x>0 and y>=0:
    print("Punctul dumneavoastra P(%d,%d) se afla in cadranul 1"%(x,y))
elif x>0 and y<0:
    print("Punctul dumneavoastra P(%d,%d) se afla in cadranul 4"%(x,y))
elif x<0 and y>0:
    print("Punctul dumneavoastra P(%d,%d) se afla in cadranul 2"%(x,y))
elif x<0 and y<0:
    print("Punctul dumneavoastra P(%d,%d) se afla in cadranul 3"%(x,y))
elif x==0 and y==0:
    print("Punctul dumneavoastra este originea sistemului de coordonate")
elif x==0 and y!=0:
    print("Punctul dumneavoastra se afla pe coordonata y")
elif x!=0 and y==0:
    print("Punctul dumneavoastra se afla pe coordonata x")
'''




