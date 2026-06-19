age= input ("are you between 11 or 12 years: (Y/N)").strip().upper()

if (age == "Y"):
    age = int (input("pick your age 11 or 12"))

    if type (age) == 11 or 12:
        print ("okay your are good")
    else:
        print ("wrong option")
else:
    print ("go to another group in which your age is there")