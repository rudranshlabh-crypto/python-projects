class inheritance:
    def __init__ (self,eye_color,hieght_cm):
        self.eye_color=eye_color
        self.height_cm=hieght_cm

    def show_traits():
        print ("eye_color", self.eye_color)
        print ("height", self.height_cm)

class kid(inheritance):
    def __init__ (self,name,age,eye_color,height_cm):
        self.name=name
        self.age=age
        super().__init__(eye_color,height_cm)

    def show_traits(self):
        print ("name", self.name)
        print ("age",self.age)
        super().show_traits()

    def favourite_hobby(self,hobby):
        print (self.name, "love", self.hobby)

child=kid("rohan", 10, "brown", "125cm")
child.favourite_hobby("sketching")