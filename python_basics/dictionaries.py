# Name : Gabriel Egan Gakere
# Date : 18/02/2026
# A program to show the use of dictionaries in python



car = {"Model" : "Audi",
         "make" : "Q8",
           "color" : "cherry",
             "year" : "2025" }

print(car)

print(car["Model"])
print(car["make"])
print(car["color"])


students = {"Alice" : 24,
                 "James" : 18,
                   "Mark" : 22,
                     "Daisy" : 19}

for key in students:
    print(key)


for val in students.values():
    print(val)