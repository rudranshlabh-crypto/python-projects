costprice=float (input("tell me cost price"))
sellprice=float (input("tell me the selling price"))
if sellprice > costprice:
    profit= sellprice - costprice
    print ("the profit is", profit)
else:
    loss= sellprice - costprice
    print ("the loss is", loss)