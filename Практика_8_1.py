N = int(input("Количество символов в списке: "))
if N<1 and N>10000:
    print ("Число должно быть от 1 до 10 000")
else:
    sp=[]
    for i in range(N):
        x=int(input())
        if x>10**5:
            print ("Число должно быть менее 10^5. Попробуйте снова")
        else:
            sp.append(x)
    sp.reverse()
    print (sp)





