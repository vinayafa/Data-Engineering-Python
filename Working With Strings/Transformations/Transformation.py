price = "12345,67"
print(price.replace(",","."))

phone = "176-1234-56"
print(phone.replace("-",""))

price = "$1299.99"
print(price.replace("$","").replace(",", ""))

#Assighment 
#Convert the messe phone number into a clean number format with only digits 
#The number is "49(176)123-4567"

phoneNumber = "+49 (176) 123-4567"
print(phoneNumber.replace("+","00").replace("(","").replace(")","").replace("-",""))