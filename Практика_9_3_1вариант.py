sp=[i for i in input("Введите числа в строку через пробел: ").split()]
for i in range (len(sp)):
    k=sp.count(sp[i])
    if k>1:
        print(sp[i],"YES")
    else:
        print(sp[i],"NO")
##Выводит сразу встречается элемент или нет, но повторяется. Как убрать повторения не придумала.




