N = int(input("Количество символов в списке: "))
if N<=1 and N>=100000:
    print ("Число должно быть от 1 до 100 000")
else:
    sp1=[]
    for i in range(N):
        x=int(input())
        sp1.append(x)
    mn1=set(sp1)
    sp2=[]
    for j in range(N):
        y=int(input())
        sp2.append(y)
    mn2=set(sp2)
    mn=(mn1.intersection(mn2))
    print(len(mn))





