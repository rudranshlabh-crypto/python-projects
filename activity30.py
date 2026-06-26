rows=int(input("enter how many rows do you you want:"))
number=1
print ("flouis triangle")
for i in range (1, rows +1):
    for j in range (1, number+1):
        print (number, end=" ")
        number=number+1
    print ()