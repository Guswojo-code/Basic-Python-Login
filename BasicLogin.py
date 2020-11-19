import getpass


print ("Hello World!")

username = "User" #Here you enter Username
password = "User"#Here you enter password
print ("Login")

ucheker = input("Username please: ")
if ucheker == username:
    print ("Correct")
else:
    print("WRONG!!!")
    quit()
pcheker = getpass.getpass("Password please: ")

if pcheker == password:
  print("Correct")
  input(
    "End? (PRESS ENTER)"
)
else:
    print("WRONG!!!")
    quit()
    
