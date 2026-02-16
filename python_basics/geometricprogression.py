# Name : Gabriel Egan Gakere
# Date : 13/02/2026
# A program to calculate geometric progression



a = (int(input("Enter the first number: ")))
r = (int(input("Enter the value of the common ratio: ")))
n = (int(input("Enter the value of the number of terms: ")))



nth_term =  a*(r**(n-1))
print(f"The value of the nth term is: {nth_term}")