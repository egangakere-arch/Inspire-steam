# Name : Gabriel Egan Gakere
# Date : 16/02/2026
# A program to calculate factors of numbers



number = int(input("Enter the value of x: "))
factorial = 1 # initialize factorial to be 1
for x in range(0,number):
    factorial = (factorial) * (x+1)#calculates the factorial of the number

print(f"the factorial of {number} is: {factorial}")

