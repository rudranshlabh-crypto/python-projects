print ("which one do you want to ride?")
print ("1.bike")
print ("2.car")

choice = int (input("pick your ride"))
if ( choice == 1 ):
    print ("1.scooty")
    print ("2.scooter")
    choice2= int (input("pick your ride"))
    if (choice2 == 1):
        print ("you have chosen scooty")
    else:
        print ("you have picked scooter")
elif ( choice == 2 ):
    print ("1.seden")
    print ("2.XUV")
    choice3= int (input("pick your ride"))
    if (choice3 == 1):
        print ("you have chosen seden")
    else:
        print ("you have picked XUV")
else:
    print ("wrong choice")