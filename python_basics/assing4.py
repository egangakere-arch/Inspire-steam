# Name : Gabriel Egan Gakere
# Date : 16/02/2026
# A program to calculate income tax


salary = int(input("Input your gross  salary: "))


if salary< 50000:
    tax = (2.5 * salary)/100
    net_salary = salary - tax 
print(f"Gross salary = {salary}")
print(f"Net salary = {net_salary}")
print(f"Tax = {tax}")