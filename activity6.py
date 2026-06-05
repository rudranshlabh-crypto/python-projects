amount=int (input("enter the total amount"))
note1=amount // 500
note2=(amount % 500)//200
note3=((amount % 500 )% 200)//100
note4=(((amount % 500)%200)%100)//50
print ("the number of 500 rupee notes are ", note1)
print ("the number of 200 rupee notes are ", note2)
print ("the number of 100 rupee notes are ", note3)
print ("the number of 50  rupee notes are ", note4)