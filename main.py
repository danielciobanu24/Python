'''
#Match case vector
import random as ra
print("Meniu!\n\nA:Generare vector de n-elemente\nB:Afisare vector generat\nC:Afisare elemente>decat media aritmetica a elementelor vectorului:\nD:Determinare valoare maxima si pozitia acesteia in tablou\nE:Deplasare elemente cu x-pozitii;x-citit de la tastatura\nF:eliminare elemente care nu apartin intervalului [a,b]\nG:Info autor\nH:Exit\n\n")
x=[]
ma=0
while True:
  print("Tastati:")
  opt=str(input())  
  match(opt):
    case 'A':
       n=int(input("Spuneti numarul de elemente ale vectorului cuprins intre 0 si 20:"))
       while n<=0 or n>20:
           print("Numarul dumneavoastra nu se afla in intervalul (0,20]")
           n=int(input("Mai tastati odata numarul de elemente:"))
       else:
           print("Tastati capetele intervalului:")
           a = int(input())
           b = int(input())
           for i in range(n):
               x.append(ra.randrange(a,b))
    case 'B':
        print(x)
    case 'C':
       ma=sum(x)
       z=ma/len(x)
       print("Media aritmetica a vectorului este egala cu:%.2f"%z)
       print("Numerele mai mari din vector decat media aritmetia a vectorului sunt:",end='')
       for i in range(n):
           if z<x[i]:
               print(x[i],end=" ")
       print("\n")
    case 'D':
       maxim=-132311
       for i in range(n):
           if maxim<x[i]:
               maxim=x[i]
               g=i
       print("Valoarea maxima a intervalului este egala cu:%d iar pozitia acestuia in tablou este:%d"%(maxim,g))
    case 'G':
      print("Buna sunt Daniel Ciobanu,student la FIESC-calculatoare")
    case "E":
      v=int(input("Spuneti cu cate pozitii doriti sa deplasati elementele vectorului:"))
      h=x[v:]+x[:v]
      print("Vectorul deplasat cu %d pozitii este:"%v,end="")
      print(h)
    case 'F':
        print("Elementele pe care trebuie sa le elimin sunt:", end="")
        for i in range(n):
          if x[i]<=a or x[i]>=b:
             print(x[i],end=" ")
             x.remove(x[i])
        print("\n")
        print("Vectorul fara elementele care nu apartin intervalului sunt:",x)
    case 'H':
        exit(1)
    case default:
        print("Ati introdus o comanda gresita!")
 '''
#match case matrice
print("Meniu!!\n1:Citire matrice de la tastatura (pe linii)\n2:Afisare matrice\n3:Creare si afisare lista de elemente maxime de pe linii\n4:Creare si afisare lista de elemente maxime de pe coloane\n5: Afisare matrice transpusa\n6:Adauga linie\n7:Adauga coloana\n8:Sterge linie\n9:Sterge coloana\n10:Liniarizare matrice (creare si afisare vector rezultat)\n0:Exit")
mat=[]
while True:
    optiune=input('Tastati:')
    match(optiune):
       case "1":
         m=int(input("Introduceti numarul de linii:"))
         n=int(input("Introduceti numarul de coloane"))
         for i in range(m):
            rand=[]
            for j in range(n):
                 valoare=int(input("mat[%d][%d]="%(i,j)))
                 rand.append(valoare)
            mat.append(rand)
       case "2":
           print("Matricea citita este:")
           for i in range(m):
               for j in range(n):
                   print(mat[i][j],end=" ")
               print()
       case "3":
           lista_maximi=[]
           max=-3132312
           for i in range(m):
               for j in range(n):
                  if mat[i][j]>max:
                      max=mat[i][j]
               lista_maximi.append(max)
               max=-132341
           print("Elementele maxime de pe fiecare linie sunt:",end="")
           for g in range(len(lista_maximi)):
               print(lista_maximi[g],end=" ")
           print("\n")
       case "4":
           lista_maximi = []
           max = -3132312
           for j in range(n):
               for i in range(m):
                   if mat[i][j] > max:
                       max=mat[i][j]
               lista_maximi.append(max)
               max = -132341
           print("Elementele maxime de pe fiecare coloana sunt:", end="")
           for g in range(len(lista_maximi)):
               print(lista_maximi[g], end=" ")
           print("\n")
       case "5":
           transpusa=[]
           for i in range(n):
               linie=[]
               for j in range(m):
                   linie.append(mat[j][i])
               transpusa.append(linie)
           print("Matricea transpusa este:")
           for i in transpusa:
               print(*i)
       case "6":
            print("Introduceti elementele pentru linia noua:")
            v = [int(input()) for x in range(n)]
            mat.append(v)
            for i in mat:
                print(*i)
       case "7":
           print("Introduceti elementele pentru coloana noua:")
           v = [int(input()) for x in range(n)]
           for i in range(n):
               mat[i].append(v[i])
           for i in mat:
               print(*i)
       case "8":
            g=int(input("Tastati numarul liniei pe care doriti sa il stergeti:"))
            del mat[g-1]
            for i in mat:
                print(*i)
       case "9":
           g = int(input("Tastati numarul coloanei pe care doriti sa il stergeti:"))
           for i in mat:
               del i[g-1]
           for i in mat:
               print(*i)
       case "10":
           v=[]
           g=len(mat)
           h=len(mat[0])
           for i in range(g):
               for j in range(h):
                   v.append(mat[i][j])
           print("Liniarizare matrice:",end="")
           for i in range(len(v)):
               print(v[i],end=",")
           print("\b")
       case "0":
           exit()
       case default:
           print("Ati introdus o comanda gresita!!")
