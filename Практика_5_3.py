X = int(input("Минимальная сумма инвестиций "))
A = int(input("Количество долларов у Майкла "))
B = int(input("Количество долларов у Ивана "))
if (A>=X) and (B>=X):
    print("2")
else:
    if A>=X:
        print("Make")
    else:
        if B>=X:
            print("Ivan")
        else:
            if(A+B)>=X:
                print ("1")
            else:
                print ("0")

                
        

            
    
    


