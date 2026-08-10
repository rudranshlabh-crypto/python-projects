class myclass:
    _privatebar=26
    def __privatemeth(self):
        print ("i am inside my class")
    def hello(self):
        print ("private variable value ", myclass._privatebar)

two = myclass()
two.hello()
two.__privatemeth()