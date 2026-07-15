import random
playing=True
number=str(rondom.randiat(0,50))
print("i generate a number between 1 to 50 and you have to guess it correct")
print("the game ends when you get one")
while playing:
    guess=input("give me your best guess:")
    if number==guess:
        print("you won the game!")
        print("the number was", number)
        break
    else:
        print("the guess isn't right try it again")