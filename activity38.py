try:
    value=int(input("enter the numuber"))
    print("the number is:", value)

except ValueError as ex:
    print ("exception", ex)