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
    def print_details(model, color, make, year):
        print(f"{make} {model} of {color} was manufuctured in the year {year}")
    model = "Toyota"
    color = "Red"
    make =  "Mazda"
    year = 2020 



