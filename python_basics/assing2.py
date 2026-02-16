# Name : Gabriel Egan Gakere
# Date : 13/02/2026
# STRING AND REPLACE



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






