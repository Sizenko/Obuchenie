N = int(input("Количество символов в списке: "))
if N<1 and N>100000:
    print ("Число должно быть от 1 до 100 000")
else:
    sp=[i for i in input("Введите элементы списк в строку через пробел: ").split()]
    del sp[N:]
y=sp[0]
for i in range(N-1):
    sp[i]=sp[i+1]
sp[N-1]=y
print(sp)





