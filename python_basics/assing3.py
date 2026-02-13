# Name : Gabriel Egan Gakere
# Date : 13/02/2026
# Assingment

# QUESTION ONE
 #Using for loop print the
  #(1)sin of numbers from -180 to 180 with 30 spteps
   #  (i) cos
   #  (ii) tan

# QUESTION TWO
#print the table of squares using for loop and (**)


# QUESTION ONE (i)
import math 

for x in range(-180,180,30):
    print(math.sin(x))

# QUESTION ONE (ii)
for y in range(-180,180,30):
    print(math.tan(y))


# QUESTION TWO
for z in range(0,30):
    print(z**2)