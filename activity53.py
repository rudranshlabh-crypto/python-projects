class employee:

     def __init__(self):
        print ("employee created")
    def __del__(self):
        print ("employee deleted")
    def createobj():
        print ("creating object")
        obj=employee()
        return obj
obj=createobj()
print ("program end")