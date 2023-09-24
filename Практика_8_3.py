m = int(input("Максимальная рузоподъёмность лодки(от 1 до 10^6): "))
n = int(input("Количество рыбаков(от 1 до 100): "))
sp=[]
for i in range(n):
    x=int(input())
    if x>=1 and x>m:
        print ("Масса рыбака не корректна!")
    else:
        sp.append(x)
sp.sort(reverse=True)
k=0
while len(sp)!=0:
    if sp[0]+sp[-1]<m:
        k=k+1
        del sp[0]
        del sp[-1]
    else:
        k=k+1
        del sp[0]
print("Необходимое количество лодок:",k)

            




