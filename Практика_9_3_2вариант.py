sp=[i for i in input("Введите числа в строку через пробел: ").split()]
mn=set()
for i in range (len(sp)):
    x=sp[i]
    if x in mn:
        print(x,"YES")
    else:
        mn.add(x)
        print(x,"NO")
##В первый раз выводит NO, включает в множество и уже YES (мне такое решение не нравится)





