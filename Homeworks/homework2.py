correctusername="Admin"
correctpassword=123456
username=input("Please enter your username: ")
password=int(input("Please enter your password: "))
if (username==correctusername and password==correctpassword):
 print("Congratulations! That was correct!!")
elif (username!=correctusername and password==correctpassword):
 print("You typed the username wrong")
elif (username==correctusername and password!=correctpassword):
 print("You typed the password wrong")
else:
 print("You typed both the username and the password wrong")
 
 
##############Extrapart
print("Now let's check it using a dictionary!")
dictionary = {"Admin":123456,"MyUsername":2021,"TestUsername":111222333,"dunno":987456}
username=input("Please enter your username: ")
password=int(input("Please enter your password: "))
if (username in dictionary.keys() and password==dictionary[username]):
 print("Congratulations! That was correct!!")
elif not (username in dictionary.keys()):
 print("This username does not exist")
else:
 print("You've entered the password wrong. Try it again!")
