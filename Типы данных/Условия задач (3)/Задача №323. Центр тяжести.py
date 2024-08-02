m=0
j=0
a=int(input())
for i in range(a):
    n,k=map(int,input().split())
    m+=n
    j+=k
itog1=m/a
itog2=j/a
print(itog1,itog2)