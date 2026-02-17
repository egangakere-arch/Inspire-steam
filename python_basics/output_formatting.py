# Name : Gabriel Egan Gakere
# Date : 17/02/2026
# A program to format the output in different styles

name = "Gabriel Egan"
weight = "78"  # in kgs
favourite_team ="Manchester city"
height = 126.45 #in cms


# (1)Format using printf(f""")

print(f"My name is {name} and i weigh  {weight}kgs.")


# (2) using f string
msg = f"my name is {name} and i support {favourite_team}"
print(msg)



# (3) using {} and .format()
print("my name is {0} and i am {1} cms tall".format(name,height))


# (4) using output specifiers %s -strings
import math
print("The value of pi is aproximately %5.3f")
print("I support %s" %favourite_team)