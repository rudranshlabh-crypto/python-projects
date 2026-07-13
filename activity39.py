try:
    num1, num2= eval(input("enter 2 numbers, seprated by comma:"))
    number=num1 / num2
except ZeroDivisionError:
    print("division by two not allowed")
except SyntaxError:
    print ("comma is missing")
except:
    print("enter any two number seprated by comma")
else:
    print("good")
finally:
    print ("i will by exicuted")