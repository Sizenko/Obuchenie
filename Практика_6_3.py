A=int(input("A="))
B=int(input("В="))
if A<=B:
    x=A%2
    if x==0:
        print(*range(A,B+1,2))
    else:
        print(*range(A+1,B+1,2))
else: print("Введённые данные противоречат условию задачи, попробуйте снова")



