import re
import strings
balance = 0.0
def create_account():
    with open("details.txt","a") as f:
        
        accountnumber = input("enter your account number:")
        
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
        
        elif not any(r in string.punctuation for r in secretkey):
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
            
        f.write(f'{accountnumber},{username},{secretkey},{balance}\n')
        print("Account created successfully")
        
        
        #verify password function
        def security(key):
            with open("details.txt", "r") as f:
                for line in f:
                    accountnumber, username, secretkey, balance = line.strip().split(',')
                    if key == secretkey:
                        return [accountnumber, username, secretkey, float(balance)]  
            print("The password is incorrect")
            return None     
        
        
        #view account details function
        def view_account(accno):
            with open("details.txt", 'r') as f:
                for line in f:
                    accountnumber, username, secretkey, balance = line.strip().split(',')
                    if accno == accountnumber:
                        print(f"Account Number: {accountnumber}")
                        print(f"Username: {username}")
                        print(f"Balance: {balance}")
                        return
                print("Account not found.")
                return None
            
            
            #update account balance function
            define update_account(accno, new_balance):
            lines = []
    with open('details.txt', 'r') as f:
        for line in f:
            accountNumber, userName, secretkey, amount = line.strip().split(',')
            if accno == accountNumber:
                lines.append(f'{accountNumber},{userName},{secretkey},{newBalance}\n')
            else:
                lines.append(line)
                return None
            
            #deposit function
            def deposit():
                with open("details.txt", "r") as f:
                    accountnumber = input("Enter your account nnumber: ")
                    key = input("Enter your password: ")
                    account = viewAccount(accno)
                    auth = security(key)
                    if account and auth:
                        if account[0] == auth[0]:
                            amount = float(input("Enter amount to deposit: "))
                            newBalance = account[3] + amount
                            updateAccount(accno, newBalance)
                            print(f"Deposit successful. New balance is {newBalance}")
                        else:
                            print("Account number and password do not match.")
                    else:
                        print("Deposit failed due to invalid account or password.")
                        
                        
                        #withdraw function
                        def withdraw():
                            with open("details.txt", "r") as f:
                                accountnumber = input("Enter your account number: ")
                                key = input("Enter your password: ")
                                account = viewAccount(accno)
                                auth = security(key)
                                if account and auth:
                                    if account[0] == auth[0]:
                                        amount = float(input("Enter amount to withdraw: "))
                                        if amount > account[3]:
                                            print("Insufficient balance for this withdrawal.")
                                        else:
                                            newBalance = account[3] - amount
                                            updateAccount(accno, newBalance)
                                            print(f"Withdrawal successful. New balance is {newBalance}")
                                    else:
                                        print("Account number and password do not match.")
                                else:
                                    print("Withdrawal failed due to invalid account or password.")
                                    def check():
                                        with open("details.txt", "r") as f:
                                            accountnumber = input("Enter your account number: ")
                                            key = input("Enter your password: ")
                                            account = viewAccount(accno)
                                            auth = security(key)
                                            if account and auth:
                                                if account[0] == auth[0]:
                                                    print(f"Account Number: {account[0]}")
                                                    print(f"Username: {account[1]}")
                                                    print(f"Balance: {account[3]}")
                                                else:
                                                    print("Account number and password do not match.")
                                            else:
                                                print("Check failed due to invalid account or password.")
                                                
                                                #return statements for functions
                                                while True:
                                                    choice = input("Choose an option: 1.Create Account 2.Deposit 3.Withdraw 4.Check Balance 5.Exit: ")
                                                    if choice == '1':
                                                        create_account()
                                                    elif choice == '2':
                                                        deposit()
                                                    elif choice == '3':
                                                        withdraw()
                                                    elif choice == '4':
                                                        check()
                                                    elif choice == '5':
                                                        print("Exiting the program.")
                                                        break
                                                    else:
                                                        print("Invalid choice. Please try again.")
                                                        
                                                        
    
            
            
            
