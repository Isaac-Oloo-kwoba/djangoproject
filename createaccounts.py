import re
import strings
def create_account():
    with open("details.txt","a") as f:
        accountnumber = (input("Enter your account number:"))
        username = (input("enter your name:"))
        secretkey = (input("enter your password:"))
        secretkey1 = (input("re-enter your password to confirm:"))
        
        if len(secretkey) < 8:
            print(f"the password should contain at least 8 a characters")
        secretkey = (input("enter password:"))
        secretkey1 = (input("re-enter password:"))
        
        elif not re.search(r."[A-Z]", secretkey):
        print("Password must have at least one upper case letter")
        secretkey = input("Enter a password: ")
        secretkey1 = input("Reenter the password: ")
        
        elif not re.search(r"[a-z]", secretkey):
        print ("Password must contain atleast one lower case letter")
        secretkey = input("Enter a password: ")
        secretkey1 = input("Reenter the password: ")
        
        elif not re.search(r"[0-9]", secretkey):
        print ("The password must have atleast one Number")
        secretkey = input("Enter a password: ")
        secretkey1 = input("Reenter the password: ")
        
        elif not any(c in string.punctuation for c in secretkey):
        print ('password must contain one special character')
        secretkey = input("Enter a password: ")
        secretkey1 = input("Reenter the password: ")
        
        elif "" in secretkey :
        print ("Cannot use spaces in the password")
        secretkey = input("Enter a password: ")
        secretkey1 = input("Reenter the password: ")
        

        while secretkey != secretkey1:

            print("The passwords don't match. Try again.")
            secretkey = input("Enter a password: ")
            secretkey1 = input("Reenter the password: ")


        balance = input("Deposit some initial amount: ")
        f.write(f'{accountnumber},{username},{secretkey},{balance}\n')
        print("Account created successfully")


        
        
        
    
