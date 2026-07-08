def total_bill(amount,tipperc):
    total = bill amount*(1+0.01 tipperc)
    total=round(total,2)
    print ("total bill amount is", total)
total_bill(150, 20)