# Name : Gabriel Egan Gakere
# Date : 19/02/2026
# A program to show objects

class Human:
    # First we define the attributes o a human being
    type = "Mammal"
    Legs = 2
    Brain = True
    Warm_blooded = True
    City = "Nairobi"


    # We need to create a conctructor for the class/object
    # The constructor will be used to create copies of tbis objects
    def __init__(self, name, age ):
        self.Human_name = name
        self.Human_age = age 
    def tell_story(self):
        print(f"Hello, i am {self.Human_name} here is a story")
        print(f"Once upon a time there was a boy who live in a village in a far away land past the hills of camalot....................")


# Creating the objects
Amani = Human("Amani", 17)
Triza = Human("Triza", 18)
Malcom = Human("Malcom", 12)

# Let the humans created do things
Amani.tell_story()
print(f"Amani's age is:", Amani.Human_age)

# Modify on of the objects, without modifying othrt objects
Triza.city = "Kiambu"
print(f"Triza's location:", Triza.city)
print(f"Amani's location:", Amani.City)
