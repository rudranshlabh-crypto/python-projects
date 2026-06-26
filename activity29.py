print ("the half piramid pattern using * :")
num=int(input("enter number of rows you want:"))
i=1
for i in range (1, num):
    for j in range (i+1):
        print ("*", end=" ")
    print ()