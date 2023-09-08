slovo=input("Введите слово латинскими строчными буквами. ")
bukv=len(slovo)
a=slovo.count("a")
e=slovo.count("e")
i=slovo.count("i")
o=slovo.count("o")
u=slovo.count("u")
if a==0:
    print ("False, a")
else:
    print ("Букв a",a)
if e==0:
    print ("False, e")
else:
    print ("Букв e",e)
if i==0:
    print ("False, i")
else:
    print ("Букв i",i)
if o==0:
    print ("False, o")
else:
    print ("Букв o",o)
if u==0:
    print ("False, u")
else:
    print ("Букв u",u)
gl=a+e+i+o+u
sgl=bukv-gl
print("Всего в слове гласных букв:",gl)
print("Согласных букв в слове:",sgl)


