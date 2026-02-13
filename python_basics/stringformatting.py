
#Name : Gabriel Egan Gakere
#Date : 12/02/2026
#String fomartting 
#Get string lenght

 
sentence ="I watch series"
string_lenth = len(sentence)
print(f"The length is : {string_lenth}")


# splitting a string 
sentence_2 = "Mathematics Pysics"
split = sentence_2 . split(" ")
print(f"The first subject is: ", split[0])


#Make everything CAPS
mpesa_code ="uh23n234re"
capitalized = mpesa_code.upper()


print("New mpesa code: ", capitalized)


#Make everething in lowercase
mpesa_code_2 = "UDD34EESLW24353W"
lower_caps = mpesa_code_2.lower()



print(f"New mpesa code i: ", lower_caps)



# Replacing characters in a string
balance = "100kes"
amount_added = "50kes"


cleaned_balance = balance.replace("kes", "")

print(f"Cleaned ballance: ", cleaned_balance)

cleaned_amount_added = amount_added.replace("kes", "")

print("cleaned amaount added: ", cleaned_amount_added)


#Sum of cleaned balance
new_balance = int(cleaned_balance)+int(cleaned_amount_added)
print(f"new balance:{new_balance}")



#Assingment 
mpesa_message = "CONFIRMED you have recieved 40kes from phylip mugambi"
print(mpesa_message)

split_message = mpesa_message.split(" ")
print("The amount is: ",split_message[4])


amount_recieved = split_message[4]

cleaned_amount_recieved = amount_recieved.replace("kes", "")
print("Cleaned amount that was recieved is: ",cleaned_amount_recieved)

original_amount =200

new_amount = (int(cleaned_amount_recieved)) + (int(original_amount))

print("Your new balance is: ", new_amount)






