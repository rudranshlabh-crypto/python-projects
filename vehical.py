class vehical:
    def __init__(self,car_color,lenght_cm):
        self.car_color=car_color
        self.lenght_cm=lenght_cm
    def show_traits():
        print ("car_color", self.car_color)
        print ("lenght", self.lenght_cm)

class car(vehical):
    def __init__(self,cars_name,years_old,car_color,lenght_cm):
        self.cars_name=cars_name
        self.years_old=years_old
    
    def show_traits(self):
        print ("car's name ", self.cars_name)
        print ("years old ", self.years_old)
        super().show_traits()

obj=car("Bayerische Motoren Werke",110,"without shine black","4.3 meters")