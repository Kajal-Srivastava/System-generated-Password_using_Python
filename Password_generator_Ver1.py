#importing random library to use choice() function
import random

#creating a list of all possible aphabets/digit/special characters used for password generation,alphabets are created using ascii code
small_alpha = [chr(i) for i in range(97, 123)]
Caps_alpha = [chr(i) for i in range(65, 90)]
digits = ['0','1','2','3','4','5','6','7','8','9']
special_char = ['!','^','%','$','#','@','&','*','+','_','-','|','~']

#Taking input from user
user_val1 = input("Do you want to generate a random password for your convenience?Enter Yes or No ")
user_val1 = user_val1.upper()

#Initializing system_created_password & user_entered_password as empty string to validate final check in case user enters no in first turn
system_created_password = " "
user_entered_password = " "

#Password generation by system using random library's choice method.
if(user_val1 == "YES"):
    system_created_password = (
        random.choice(small_alpha)
        + random.choice(Caps_alpha)
        + random.choice(digits)
        + random.choice(special_char)
        +random.choice(small_alpha)
        + random.choice(Caps_alpha)
        + random.choice(digits)
        + random.choice(special_char))
    print("System Generated password is = "+system_created_password)
else:
    #Here user is asked to enter the password and save the entered password.
    user_val2 = input("Do you want to enter your own password ? Enter Yes or No ")
    user_val2 = user_val2.upper()
    
    if(user_val2 == "YES"):
        #user enters the password and it's stored in a variable
        user_entered_password = input("Enter your password :")
        print("You have entered :"+user_entered_password)             
    else:
        print("Thanks! See you next time.")

#Printing the final password
if (system_created_password!=" "):
    print("Your final selected password is :"+system_created_password)
if (user_entered_password!=" "):
    print("Your final selected password is :"+user_entered_password)
else:
    print("You haven't selected or entered any password. See You Again!")
        
