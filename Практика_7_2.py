st = input("Введите строку ")
sim =len(st)
st1=st[0]
i=1
while i<sim:
    if st[i]!=' ':
        st1=st1+st[i]
    elif st[i-1]!=' ':
        st1=st1+" "
    i=i+1
print (st1) 
    

        
    


        
    
           
              








