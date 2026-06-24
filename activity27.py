string=input("enter the string which you want:")
character=input("enter the character of your type:")
i=0
num=0
while (i < len (string)):
    if (string[i]==character):
        num=num+1
    i=i+1
print ("the number of times ", character, " occurs ", num)