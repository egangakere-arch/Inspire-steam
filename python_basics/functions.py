# Name : Gabriel Egan Gakere
# Date : 18/02/2026
# A program to cook an egg


def cook_egg():
    oil = "20ml"
    pan = True
    moto = True
    eggs = 2
    print(f"The pan is {pan}, and the fire is {moto}, add {oil} amount")


print("Here is statement 1")


print("Here is statement 2")

cook_egg()

print("Here is statement 3")



# Bus fare creating function


def create_fare(route, distance, is_rush_hour):
    fare = distance * 10
    if is_rush_hour ==  True:
         fare = fare *1.5
    print(f"Your fare from {route} is {fare}")

    return fare


rush_hour = True 
retured_fare = create_fare("Juja-Olsoaps", 7, rush_hour)
print(f"The fare returned is: {retured_fare}")

# Passing a list aas a parameter 
def write_all_intrests(interest):
    for interest in interest:
            print(f"I am interested in {interest}")



all_interests = ["Bike riding", "Hiking", "Painting", "poetry"]

write_all_intrests(all_interests)


