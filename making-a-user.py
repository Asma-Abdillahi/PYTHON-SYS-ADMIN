from os import system


def new_user(): 
 confirm = "N"
 while confirm != "Y": 
    username = input("Enter the name of the user to add: ") 
    print("Use the username '" + username + "'? (Y/N)") 
    confirm = input().upper()
system("adduser " + username)

name = "John"
print("Hello " + name + ".")
age = 40
print(name + " is " + str(age) + " years old.")