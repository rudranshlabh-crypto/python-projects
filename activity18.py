medical = input ("do you have  a medical cause: (Y/N)").strip().upper()

if medical == "Y":
    print ("okay you are allowed")
else:
    attendance=int (input("enter number of days you were present"))
    if attendance > 75:
        print ("You are allowed in the exam")
    else:
        print ("you are not allowed in exam")