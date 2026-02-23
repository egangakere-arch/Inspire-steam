# Name : Gabriel Egan Gakere
# Date : 23/02/2026
# A program to show classes in python


class Car():
    # Attributes of the car
    def __init__(self, model, color, make, year):
            self.model = model
            self.color = color
            self.make = make
            self.year = year

    # Print car details
    def print_details(self,model, color, make, year):
        print(f"{make} {model} of {color} was manufuctured in the year {year}")

#instantiatin the car class

my_car = Car("Toyota", "Red", "Mazda", 2020)
dads_car = Car("corolla", "white", "toyota", 2018)

my_car.print_details("Toyota", "Red", "Mazda", 2020)
dads_car.print_details("corolla", "white", "Toyota", 2018)



