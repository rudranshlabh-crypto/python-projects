class IOSstring():

    def __init__(self):
        self.str1=""
    def getstr(self):
        self.str1=input("enter a string:")
    def printstring(self):
        print ("result is", self.str1.upper())

str1=IOSstring()
str1.getstr()
str1.printstring()