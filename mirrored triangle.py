print ("the half piramid pattern using * :")
num=int(input("enter number of rows you want:"))
i=0
for i in range (0, num):
    for j in range (i+1):
        print ("*", end=" ")
    print ()  

size = int(input("enter the number thats in your mind:"))
i=0
for i in range(1, size + 1):
    breaks = " " * (size - i)
    sparkles = "*" * i
    print(breaks+sparkles)
print ()

print ("the frist one is the normal right angle triangle and the other one is mirrored image of that")