from abc import ABC, abstractmethod

class absclass (ABC):
    def print (self,x):
        print ("passed value", x)
    
    def task(self):
        print ("we are inside abs class task")

class testclass(absclass):
    def task(self):
        print ("we are inside test class")

test_obj= testclass()
test_obj.task()
test_obj.print(100)