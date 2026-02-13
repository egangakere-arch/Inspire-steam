# Name : Gabriel Egan Gakere
# Date : 13/02/2026
# A program to calculate arithmetic progression

# Calculating the nth term

a = (int(input("Enter the first term: ")))
n = (int(input("Enter number of terms: ")))
d = (int(input("Enter the common difference: ")))


Nth_term = a + ( n - 1 ) * d
sn = (n / 2) * (2 * a + (n - 1 ) * d)
print(f"The Nth term is: {Nth_term}")
print(f"The sn is: {sn}")

